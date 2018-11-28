#define _CRT_SECURE_NO_DEPRECATE
//
//
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const double zero=1e-6;
const double limit=1e8;
#define SZ(x) (int(x.size()))
typedef long long int64;
typedef unsigned long long uint64;
template<class T> T sqr(T x) {return x*x;}
template<class T> T gcd(T a,T b){ if(a<0) return gcd(-a,b);if(b<0) return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(T a,T b){ return a*(b/gcd(a,b));}
int64 toInt64(string s){ istringstream sin(s); int64 t; sin>>t;return t;}
int toInt(string s){ istringstream sin(s); int t; sin>>t; return t;}
template<class T> string toString(T x){ ostringstream sout; sout<<x; return sout.str();}


ifstream inf("in.txt");
#define cin inf
ofstream outf("out.txt");
#define cout outf

set<pair<int,int> > st[2];
int main(int argc, char* argv[])
{

	int T;
	cin>>T;
	for(int tt=1; tt<= T;tt++)
	{
		st[0].clear();
		int r;
		cin>>r;
		int x1,x2,y1,y2;
		for(int i=0;i<r;i++)
		{
			cin>>x1>>y1>>x2>>y2;
			for(int fi=y1;fi<=y2;fi++)
			{
				for(int j=x1;j<=x2;j++)
					st[0].insert(make_pair(fi,j));
			}
		}
		int nw = 0;
		int ret = 0;
		while(!st[nw].empty())
		{
			int nx = 1-nw;
			st[nx].clear();
			for(set< pair<int,int>> ::iterator it = st[nw].begin();it!=st[nw].end();++it)
			{
				int x = (*it).first;
				int y = (*it).second;
				if(st[nw].find(make_pair(x-1,y)) != st[nw].end() || st[nw].find(make_pair(x,y-1)) != st[nw].end())
					st[nx].insert(*it);
				if(st[nw].find(make_pair(x+1,y-1)) != st[nw].end())
					st[nx].insert(make_pair(x+1,y));
			}
			nw = nx;
			ret++;
		}
		cout<<"Case #"<<tt<<": "<<ret<<endl;
	}
}
