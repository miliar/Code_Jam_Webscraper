/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
#include <cmath>
#include <set>
#include <deque>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <glpk.h> // http://www.gnu.org/software/glpk
using namespace std;
int bitct(long long r) {return r == 0 ? 0 : (bitct(r>>1) + (r&1));}
long long gcd(long long x, long long y) {return x ? gcd(y%x,x) : y;}
template<typename T> ostream& operator << (ostream &o,vector<T> v) {o<<"{";
	int i=0,s=v.size();for(;i+1<s;i++)o<<v[i]<<", ";if(s)o<<v[i];o<<"}";return o;}
long long choose(long long n, long long q)
{ if(n==0 || q==0) return 1;
	if (q==1) return n; else return ( choose(n, q-1) * (n-q+1 ) /q); }
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); ++i)
//int dx[8] = {0,  1,  1,  1,  0, -1, -1, -1}
//int dy[8] = {1,  1,  0, -1, -1, -1,  0,  1}
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

void calc(ifstream &, ofstream &);
main() { stringstream filename, fnamein, fnameout;
	string file("B");
	filename << file << "-large.";
	fnamein << filename.str() << "in"; fnameout << filename.str() << "out";
	ifstream fin(fnamein.str().c_str()); ofstream fout(fnameout.str().c_str());
	int count;
	fin >> count;
	for(int i=0;i<count;i++) {
		fout << "Case #" << (i+1) << ": ";
		calc(fin, fout);
		fout.flush(); }
	fin.close(); fout.close(); }

void calc(ifstream &fin, ofstream &fout)
	{
	int P;
	fin >> P;
	vector<int> misses;
	for(int i=0;i< (1<<P);i++)
		{
		int x;
		fin >> x;
		misses.push_back(x);
		}

	vector<int> costs;
	for(int i=0;i< (1<<P)-1;i++)
		{
		int x;
		fin >> x;
		costs.push_back(x);
		}


	glp_prob *lp = glp_create_prob();
	glp_set_obj_dir(lp, GLP_MIN); //set max or min goal

	glp_add_cols(lp, 2+costs.size()); //remember, all arrays indexed from 1!
	glp_add_rows(lp, 2+(1<<P));

	for (int i=0;i<costs.size();i++)
		{
		glp_set_col_bnds(lp, 1+i, GLP_DB, 0, 1);
		glp_set_obj_coef(lp, 1+i, costs[i]);
		}


	for( int i=0;i<misses.size();i++)
		{
		glp_set_row_bnds(lp, 1+i, GLP_LO, P-misses[i], 100000000); 

		int teamidx = i/2;
		int start = 0;
		int ind[P+1];//games
		double val[P+1];//all ones
		for(int j=1;j<=P;j++)
			{
			ind[j] = 1+teamidx+start; //figure!
			val[j]=1.0;

			start += (1<< (P-j));
			teamidx = teamidx/2;
			}
		glp_set_mat_row(lp, i+1, P, ind, val);
		}

	/*
		 glp_smcp parm;
		 glp_init_smcp(&parm);
		 parm.msg_lev = GLP_MSG_OFF;
	 */

	glp_simplex(lp, NULL);

	/*
	for(int r=0;r<R;r++)
		for(int c=0;c<C;c++)
			{
			cout << r << "," << c <<  endl;
			cout << glp_get_col_prim(lp, 1+3*(r*C+c))<< endl;
			cout << glp_get_col_prim(lp, 2+3*(r*C+c))<< endl;
			cout << glp_get_col_prim(lp, 3+3*(r*C+c))<< endl;
			}
			*/

	char buffer[100];
	sprintf (buffer, "%.0f", glp_get_obj_val(lp));
	fout << buffer  << endl;
	glp_delete_prob(lp);
	return; 
	}
