#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <fstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

const int inf=1000000;

int dp[20000][2];
int g[200000],c[200000];

int main()
{
        int T;
        cin>>T;
        REP(cas,T)
        {
                int M,V;
                cin>>M>>V;
                REP(i,(M-1)/2)
                {
                        cin>>g[i+1]>>c[i+1];
                }
                REP(i,(M+1)/2)
                {
                        int j=i+(M-1)/2+1;
                        cin>>g[j];
                        c[j]=2;
                }
                REP(i,M+10)
                        dp[i][0]=dp[i][1]=0;
                REP(i,M+10)
                        dp[i][0]=dp[i][1]=inf;
                for (int i=M;i>=1;i--)
                {
                        if (c[i]==2)
                        {
                                dp[i][0]=dp[i][1]=inf;
                                dp[i][g[i]]=0;
                        }
                        else
                        {
                                REP(t2,2)
                                        REP(t3,2)
                                        {
                                                if (g[i]==1)
                                                        dp[i][t2&t3]=min(dp[i][t2&t3],dp[i*2][t2]+dp[i*2+1][t3]);
                                                if (g[i]==0)
                                                        dp[i][t2|t3]=min(dp[i][t2|t3],dp[i*2][t2]+dp[i*2+1][t3]);
                                                if (g[i]==0 && c[i]==1)
                                                        dp[i][t2&t3]=min(dp[i][t2&t3],1+dp[i*2][t2]+dp[i*2+1][t3]);
                                                if (g[i]==1 && c[i]==1)
                                                        dp[i][t2|t3]=min(dp[i][t2|t3],1+dp[i*2][t2]+dp[i*2+1][t3]);
                                        }
                        }
                        //out<<i<<' '<<dp[i][0]<<' '<<dp[i][1]<<endl;
                }
                printf("Case #%d: ",cas+1);
                if (dp[1][V]==inf)
                        puts("IMPOSSIBLE");
                else
                        printf("%d\n",dp[1][V]);
        }
        return 0;
}
