#include "bignum.h"
#include<iostream>
#include<list>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<cstring>
#include<algorithm>
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,a,b) for(i=(a);i<(b);++i)
#define PB push_back
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<LL> VLL;
const int dx[]={-1,0,1,0,-1,-1,1,1};
const int dy[]={0,1,0,-1,-1,1,-1,1};

LL f[11][1100][11];
int m[1100];
int p[11][1100];
int n;
const LL MX=100000000000LL;
LL dp(int i,int j,int cnt)
{
	if (i==n) {
		if (cnt>=n-m[j]) return 0;
		else return MX;
	}
	if (f[i][j][cnt]>=0) return f[i][j][cnt];
	LL &ans=f[i][j][cnt];
	ans=p[i][j]+dp(i+1,j*2,cnt+1)+dp(i+1,j*2+1,cnt+1);
	ans=min(ans,dp(i+1,j*2,cnt)+dp(i+1,j*2+1,cnt));
	return ans;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int _T,T;
	scanf("%d",&_T);
	REP(T,_T) {
		printf("Case #%d: ",T+1);
		memset(f,-1,sizeof(f));
		scanf("%d",&n);
		int i,j;
		REP(i,(1<<n)) scanf("%d",&m[i]);
		for (i=n-1;i>=0;--i) {
			REP(j,(1<<i)) {
				scanf("%d",&p[i][j]);
			}
		}
		printf("%d\n",dp(0,0,0));
	}
}
