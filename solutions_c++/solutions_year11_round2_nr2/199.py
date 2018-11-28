#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) (int)v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const i64 inf = 1LL<<61;
const double eps = 1e-9;

int C,D;

const int MAXN = 500;

i64 p[MAXN],v[MAXN];



bool can(i64 t)
{
	i64 lim = -inf;
	FOR(i,0,C)
		FOR(j,0,v[i])
	{
		if(lim <= p[i])
			lim = max(lim,p[i] - t);
		else
		{
			if(lim > p[i] + t)
				return false;
		}
		lim+=D;
	}


	return true;
}


int main()
{
#ifdef HOME_PC
	//freopen ("input.txt","r",stdin);
	freopen ("B-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		
		
		cin>>C>>D;

		D*=2;
		FOR(i,0,C)
		{
			cin>>p[i]>>v[i];
			p[i]*=2;
		}

		i64 l = 0, r = 1LL<<59;

		while(l<r)
		{
			i64 mid = (l+r)/2;
			if(can(mid))
				r = mid;
			else
				l = mid+1;
		}

		

		printf("Case #%d: ",cas);
		cout<<r/2;
		if(r%2)
			cout<<".5";
		puts("");
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

