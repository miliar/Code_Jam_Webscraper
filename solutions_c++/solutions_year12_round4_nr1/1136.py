#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<bitset>
#include<iostream>
#include<sstream>
#include<queue>
#include<cassert>
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define TWO(i) (1<<(i))
using namespace std;

typedef vector<int> VI;
typedef VI::iterator VIit;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef MII::iterator MIIit;
typedef set<int> SI;
typedef SI::iterator SIit;
typedef long long LL;
const int DX[8]={1,-1,0,0,1,1,-1,-1};
const int DY[8]={0,0,1,-1,1,-1,1,-1};
const int intmax=0x7fffffff;
const int mod=1000000007;
int d[10005],l[10005],dp[10005];

int main()
{
    freopen("al.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int mt=1;mt<=t;mt++)
    {
        int n,dis;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d%d",&d[i],&l[i]);
        scanf("%d",&dis);
        memset(dp,-1,sizeof(dp));
        dp[0]=2*d[0];
        for(int i=0;i<n;i++)
            for(int j=i+1;j<n;j++)
            {
                if (d[j]>dp[i]) break;
                dp[j]=max(dp[j],d[j]+min(d[j]-d[i],l[j]));
            }
        //for(int i=0;i<n;i++) printf("%d ",dp[i]);puts("");
        int maxd=0;
        for(int i=0;i<n;i++) maxd=max(dp[i],maxd);
        if (maxd>=dis) printf("Case #%d: YES\n",mt);
        else printf("Case #%d: NO\n",mt);
    }
}

