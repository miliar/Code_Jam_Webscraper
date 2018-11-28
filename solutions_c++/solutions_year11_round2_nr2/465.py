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
	filename << file << "-small.";
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
	int C, D;
	fin >> C >> D;
	vector<double> V;
	vector<double> P;
	for(int i=0;i<C;i++)
		{
		int p, v;
		fin >> p >> v;
		P.push_back(p);
		V.push_back(v);
		}

	double prev_time=0;
	double prev_coord=-100000000;
	for(int g=0;g<C;g++)
		{
		double spread_time = D*(V[g]-1)/2;
		double spread_lmost = P[g] - spread_time;
		double spread_rmost = P[g] + spread_time;

		double mintime = max(prev_time, spread_time);
		double leftmost_mintime = P[g]-mintime;
		if(leftmost_mintime >= prev_coord - (mintime-prev_time))
			{
			prev_time=mintime;
			prev_coord= leftmost_mintime+2*spread_time+D;
			continue;
			}

		double rightmost_mintime = spread_lmost + (mintime-spread_time);
		if(rightmost_mintime <= prev_coord - (mintime-prev_time))
			{
			prev_time=mintime + 
				((prev_coord - (mintime-prev_time)) - rightmost_mintime)/2;
			prev_coord= P[g] + prev_time+D;
			continue;
			}

		prev_coord += D*V[g];
		}

	char buffer[100];
	sprintf(buffer, "%f", prev_time);
	
	fout << buffer << endl;
	return; 
	}
