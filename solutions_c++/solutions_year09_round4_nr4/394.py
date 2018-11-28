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
	string file("D");
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
	int N;
	fin >> N;
	vector<int> x, y, r;
	for(int i=0;i<N;i++)
		{
		int a,b,c;
		fin >> a >> b >> c;
		x.push_back(a);
		y.push_back(b);
		r.push_back(c);
		}
	if(1==N)
		{
		fout << r[0] << endl;
		return;
		}
	if(2==N)
		{
		fout << max(r[1], r[0]) << endl;
		return;
		}

	long double rr=1000000.0;
	int f=0;
	int s=1;
	int t=2;
	long double test = sqrt((x[f]-x[s])*(x[f]-x[s]) + (y[f]-y[s])*(y[f]-y[s]));
	test+=r[f]+r[s];
	test=test/2;
	if(test < max(r[f], r[s]))
		test = max(r[f], r[s]);
	if(test < r[t])
		test = r[t];
	if(test < rr)
		rr=test;

	f=1;
	s=2;
	t=0;
	test = sqrt((x[f]-x[s])*(x[f]-x[s]) + (y[f]-y[s])*(y[f]-y[s]));
	test+=r[f]+r[s];
	test=test/2;
	if(test < max(r[f], r[s]))
		test = max(r[f], r[s]);
	if(test < r[t])
		test = r[t];
	if(test < rr)
		rr=test;

	f=2;
	s=0;
	t=1;
	test = sqrt((x[f]-x[s])*(x[f]-x[s]) + (y[f]-y[s])*(y[f]-y[s]));
	test+=r[f]+r[s];
	test=test/2;
	if(test < max(r[f], r[s]))
		test = max(r[f], r[s]);
	if(test < r[t])
		test = r[t];
	if(test < rr)
		rr=test;

	fout << rr << endl;



	return; 
	}
