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

LL M=100003;
LL c[502][502];
LL dp[502][502];
LL C(int n,int k)
{
	if (k>n) return 0;
	if (k==0 || k==n) return 1;
	if (c[n][k]<0) c[n][k]=(C(n-1,k)+C(n-1,k-1))%M;
	return c[n][k];
}
LL f(int n,int k)
{
//	cout<<n<<' '<<k<<endl;
	if (n<2) return 0;
	if (k==1) return 1;
	if (k>=n) return 0;
	if (dp[n][k]>=0) return dp[n][k];
	int t;
	LL ans=0;
	for (t=1;t<k;++t) {
		ans=(ans+f(k,t)*C(n-k-1,k-t-1))%M;
	}
	dp[n][k]=ans;
//	cout<<n<<' '<<k<<' '<<ans<<endl;
	return ans;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int _T,T;
	scanf("%d",&_T);
	memset(c,-1,sizeof(c));
	memset(dp,-1,sizeof(dp));
	REP(T,_T) {
		printf("Case #%d: ",T+1);
		int n;
		scanf("%d",&n);
		int k;
		LL ans=0;
		for (k=1;k<n;++k) ans=(ans+f(n,k))%M;
		printf("%d\n",int(ans));
	}
}
