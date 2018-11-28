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
	string file("C");
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
	int N, K;
	fin >> N >> K ;
	vector<vector<int> > D(N, vector<int>(K));
	for(int i=0;i<N;i++)
		for(int j=0;j<K;j++)
			{
			int a;
			fin >> a;
			D[i][j]=a;
			}
	
	vector<vector<int> > conf(N, vector<int>(N));
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			{
			bool ok=true;
			int dir=1;
			if(D[i][0] < D[j][0])
				dir=0;

			for(int t=0;t<K;t++)
				{
				if(D[i][t] == D[j][t])
					ok=false;
				if(dir && D[i][t] < D[j][t] || (!dir) && D[i][t] > D[j][t])
					ok=false;
				}
			conf[i][j] = ok;
			conf[j][i] = ok;
			}

	vector<int> groups;
	set<int> gs;
	for(int i=(1<<N);i-->1;)
		{
		bool ok=true;
		for(int b=0,m=1;b<N;b++,m=m<<1)
			{
			if(m&i)
				for(int bb=b+1,mm=(m<<1);bb<N;bb++,mm=mm<<1)
					{
					if(mm&i)
						if(!conf[b][bb])
							ok=false;
					}
			}
		if(ok)
			foreach(g, gs)
				if(((*g)&i) == i)
					ok=false;
		if(ok)
			{
			groups.push_back(i);
			gs.insert(i);
			}
		}
	//cout << groups << endl;;

	vector<int> best(1+(1<<N), 1000);
		
		for(int i=0;i<(1<<N);i++)
			{
				if(gs.end() != gs.find(i))
					best[i]=1;
			}

		for(int i=0;i<(1<<N);i++)
			{
			if(i==1000)
				continue;
			for(int j=0;j<groups.size();j++)
				{
				if((i|groups[j]) > i)
					best[(i|groups[j])] = min(best[(i|groups[j])], best[i]+1);
				}
			}

	fout << best[(1<<N)-1] << endl;


	return; 
	}
