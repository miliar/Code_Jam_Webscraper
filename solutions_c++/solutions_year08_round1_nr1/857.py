// pro1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
//#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

//#if defined (__GNUC__) && (__GNUC__ <= 2)
//#include <hash_map>
//#include <hash_set>
//#else
//#include <ext/hash_map>
//#include <ext/hash_set>
//using namespace __gnu_cxx;
//#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
const int maxn=10;
int n;
int map[maxn][maxn],lx[maxn],ly[maxn],match[maxn];
bool x[maxn],y[maxn];
int up[maxn],down[maxn];
const int maxin=100000000;
bool find(int k)
{
	int i,t;
	x[k]=true;
	for(i=0;i<n;i++)
	{
		if(!y[i]&&lx[k]+ly[i]==map[k][i])
		{
			y[i]=1;
			t=match[i];
			match[i]=k;
			if(t==-1||find(t)) return true;
			match[i]=t;
		}
	}
	return false;
}
int cal()
{
	int sum=0;
	for(int i=0;i<n;i++)
		sum+=map[match[i]][i];
	return -sum;
}

int main()
{
	//freopen("test.txt","r",stdin);
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	/*freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);*/
	int T,k;
	cin>>T;
	int i,j,d;
	for(int cases=1;cases<=T;cases++)
	{
		cin>>n;
		REP(i,n)
			cin>>up[i];
		REP(i,n)
			cin>>down[i];
		REP(i,n)
			REP(j,n)
		{
			map[i][j]=-up[i]*down[j];
		}

		memset(match,-1,sizeof(match));
		//memset(map,0,sizeof(map));
		memset(lx,-maxin,sizeof(lx));
		//for(i=0;i<num;i++) lx[i]=-maxin;
		memset(ly,0,sizeof(ly));
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(map[i][j]>lx[i]) lx[i]=map[i][j];
		for(k=0;k<n;k++)
		{
			while(1)
			{
				memset(x,0,sizeof(x));
				memset(y,0,sizeof(y));
				if(find(k)) break;
				d=maxin;
				for(i=0;i<n;i++)
					if(x[i])
						for(j=0;j<n;j++)
						{
							if(!y[j])
								if(lx[i]+ly[j]-map[i][j]<d) d=lx[i]+ly[j]-map[i][j];
						}
						for(i=0;i<n;i++) if(x[i]) lx[i]-=d;
						for(j=0;j<n;j++) if(y[j]) ly[j]+=d;
			}

		}

		cout<<"Case #"<<cases<<": "<<cal()<<endl;
	}
	return 0;
}

