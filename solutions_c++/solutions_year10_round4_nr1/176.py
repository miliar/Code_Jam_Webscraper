#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define UN(v) sort(all(v)),(v).erase(unique((v).begin(),(v).end()),(v).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

int iabs (int a) { return a<0 ? -a : a; }

int k, v[111][111];

int main()
{
#ifdef LocalHost
freopen("a-large.in", "r", stdin);//-small-attempt
freopen("a-large.out", "w", stdout);//-large
#endif
	int T;
	scanf("%d", &T);
REP(it, T)
{
	scanf("%d", &k);
	CL(v, -1);
	REP(i, k) REP(j, i+1)
	{
		scanf("%d", &v[i][k-i-1+2*j]);
		if(j<i) v[i][k-i-1+2*j+1]=-2;
	}
	FOR(i, k, 2*k-1) REP(j, 2*k-i-1)
	{
		scanf("%d", &v[i][i-k+1+2*j]);
		if(j<2*k-i-2) v[i][i-k+1+2*j+1]=-2;
	}
/*	REP(i, 20)
	{
		REP(j, 20)
		{
			if(v[i][j]==-1) printf("  ");
			else printf("%d ", v[i][j]);
		}
		printf("\n");
	}*/
	int ans=1000000000;
	FOR(i, 0, 2*k-1) FOR(j, 0, 2*k-1)
	{
		bool t=1;
		REP(ii, 2*k-1) REP(jj, 2*k-1) if(v[ii][jj]!=-1)
		{
			if(2*i-ii>=0 && 2*i-ii<2*k-1 && v[2*i-ii][jj]!=-1 && v[ii][jj]!=v[2*i-ii][jj]) { t=0; goto no; }
			if(2*j-jj>=0 && 2*j-jj<2*k-1 && v[ii][2*j-jj]!=-1 && v[ii][jj]!=v[ii][2*j-jj]) { t=0; goto no; }
		}
		no:;
		if(t)
		{
			int d = iabs(i-k+1) + iabs(j-k+1);
			ans = min(ans, d);
		}
	}
	printf("Case #%d: %d\n", it+1, (k+ans)*(k+ans) - k*k);
}
	return 0;
}
