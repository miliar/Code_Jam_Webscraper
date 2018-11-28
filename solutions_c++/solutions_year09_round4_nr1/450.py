/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
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
	string file("A");
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
	int N;
	fin >> N;

	vector<string> D;
	for(int i=0;i<N;i++)
		{
		string t;
		fin >> t;
		D.push_back(t);
		}

	vector<int> taken(N);
	int ct=0;
		for(int i=0;i<N;i++)
		{
			for(int poss=0;poss<N;poss++)
				{
				if(taken[poss])
					continue;

				bool good=true;
				for(int j=i+1;j<N;j++)
					if('1'==D[poss][j])
						good=false;
				if(good)
					{
					taken[poss]=1;
					break;
					}
				if(!good)
					ct++;
				}
		}
	fout << ct << endl;


	return; 
	}
