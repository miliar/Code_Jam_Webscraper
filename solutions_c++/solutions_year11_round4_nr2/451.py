#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define FIL(c,n) memset(c,n,sizeof(c))

#define R 510

int w[R][R];
long long gsx[R][R],gsy[R][R];
long long gx[R][R],gy[R][R];
long long sum[R][R];

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ct=1;ct<=t;ct++)
    {
        int r,c,d;
        FIL(sum,0);
        FIL(gsx,0);
        FIL(gsy,0);
        FIL(w,0);
        scanf("%d%d%d",&r,&c,&d);
        for(int i=1;i<=r;i++)
        {
            char s[1000];
            scanf("%s",s);
            for(int j=1;j<=c;j++)
            {
                w[i][j]=s[j-1]-'0'+d;
                gx[i][j]=w[i][j]*i;
                gy[i][j]=w[i][j]*j;
                sum[i][j]=sum[i-1][j]+sum[i][j-1]+w[i][j]-sum[i-1][j-1];
                gsx[i][j]=gsx[i-1][j]+gsx[i][j-1]+gx[i][j]-gsx[i-1][j-1];
                gsy[i][j]=gsy[i-1][j]+gsy[i][j-1]+gy[i][j]-gsy[i-1][j-1];
            }
        }
        int ans=0;
        for(int i=1;i<=r;i++)
            for(int j=1;j<=c;j++)
                for(int k=2;i+k<=r&&j+k<=c;k++)
                {
                    long long sijk=sum[i+k][j+k]-sum[i-1][j+k]-sum[i+k][j-1]+sum[i-1][j-1];
                    sijk-=w[i][j]+w[i+k][j]+w[i][j+k]+w[i+k][j+k];
                    long long sx=sijk*(i+i+k),sy=sijk*(j+j+k);
                    long long gxx=gsx[i+k][j+k]-gsx[i-1][j+k]-gsx[i+k][j-1]+gsx[i-1][j-1];
                    gxx-=gx[i][j]+gx[i+k][j]+gx[i][j+k]+gx[i+k][j+k];
                    long long gyy=gsy[i+k][j+k]-gsy[i-1][j+k]-gsy[i+k][j-1]+gsy[i-1][j-1];
                    gyy-=gy[i][j]+gy[i+k][j]+gy[i][j+k]+gy[i+k][j+k];
                    if(gxx*2==sx&&gyy*2==sy)
                        ans=max(ans,k+1);
                }
        if(ans)
            printf("Case #%d: %d\n",ct,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",ct);
    }
    return 0;
}

