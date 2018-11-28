#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define FOR(k,a,b) for(LL k(a); k < (b); ++k)
#define FORD(k,a,b) for(int k(b-1); k >= (a); --k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))


int main()
{
#ifdef HOME
	clock_t start=clock();
	freopen ("A-large.in","r",stdin);
	freopen ("A-large.out","w",stdout);
#endif
	int T,N,D;
	scanf("%d",&T);
	vector<pair<int,int> > v;
	v.reserve(10000);
	vector<int> dp(10000);
	FOR(testcase,1,T+1)
	{
		scanf("%d",&N);
		v.clear();
		v.resize(N);
		dp.clear();
		dp.resize(N);

		REP(ii,N)
		{
			scanf("%d %d",&(v[ii].first),&(v[ii].second));
		}
		scanf("%d",&D);
		dp[0]=v[0].first;
		REP(i,N)
		FOR(j,i+1,N)
		{
			if(v[i].first+dp[i]>=v[j].first)
			{
				dp[j]=max(dp[j],min(min(dp[i],v[j].first-v[i].first),v[j].second));
			}
			else
				break;
		}
		int mx=0;
		REP(i,N)
			if(mx<v[i].first+dp[i])
				mx=v[i].first+dp[i];
		if(mx>=D)
			printf("Case #%d: YES\n",testcase);
		else
			printf("Case #%d: NO\n",testcase);
	}
	
#ifdef HOME
	fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
#endif
	return 0;
} 