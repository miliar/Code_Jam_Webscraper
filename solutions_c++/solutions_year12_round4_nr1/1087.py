#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
ll d[11111],l[11111];
ll dp[11111];
int n;
int main()
{
	freopen("C:\\Users\\daizhy\\Downloads\\A-large (6).in","r",stdin);
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		rep(i,n)cin>>d[i]>>l[i];
		ll e;cin>>e;
		ll r=2*d[0];
		memset(dp,0,sizeof(dp));
		dp[0]=r;
		int ok=0;
		for (i=0;i<n;i++)
		{
			for (j=i+1;j<n;j++)
			{
				if (d[j]<=dp[i])
				{
					dp[j]=max(dp[j],d[j]+min(d[j]-d[i],l[j]));
				}
				if (dp[j]>=e)ok=1;
				if (ok)break;
			}
			if (dp[i]>=e)ok=1;
			if (ok)break;
		}
		printf("Case #%d: ",++cc);	
		puts(ok?"YES":"NO");
	}
	return 0;
}
