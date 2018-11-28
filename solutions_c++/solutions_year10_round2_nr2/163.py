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
using namespace std;

#pragma comment(linker,"/stack:16000000")

#define ALL(v) v.begin(),v.end()
#define SZ(v) v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=start;i<N;++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

int main()
{
	freopen ("B-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("B-large.out","w",stdout);

	int tt;
	cin>>tt;
	for(int cas = 1;cas<=tt;++cas)
	{
		i64 N,K,B,T;
		cin>>N>>K>>B>>T;
		vector<i64> x(N),v(N);
		FOR(i,0,N)
			cin>>x[i];
		FOR(i,0,N)
			cin>>v[i];
		
		int ans = 0;
		vector<bool> can(N,false);
		REPSZ(i,x)
			if((B-x[i])<=v[i]*T)
				can[i] = true;

		if(count(ALL(can),true)<K)
		{
			printf("Case #%d: IMPOSSIBLE\n",cas);
			continue;
		}

		for(int i = can.size()-1;i>=0 && K>0;--i)
			if(can[i])
			{
				K--;
				ans+=count(can.begin()+i,can.end(),false);
			}
			
				

		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

