#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
const int N = 20;
int gi[N];
int T;
int r,n,k;
__int64  sum[N][N];
void init()
{
    for (int i=0;i<n;i++)
    {

        for (int j=0;j<n;j++)
        {
            __int64 ans = gi[i];
            if (i==j)
            {
                sum[i][j] = ans;
                continue;
            }
            int st = (i+1)%n;
            while (st!=j)
            {
             //   printf("ans %d\n",ans);
                ans+=gi[st];
                st = (st+1)%n;
            }
            sum[i][j] = ans+gi[j];
          //  printf("sum[%d][%d]:%d\n",i,j,sum[i][j]);
        }

    }
}
int main()
{
    freopen("d:\\C-small-attempt0.in","r",stdin);
    freopen("d:\\t.out","w",stdout);
    scanf("%d",&T);
    for (int i=1;i<=T;i++)
    {
        memset(sum,0,sizeof(sum));
        scanf("%d%d%d",&r,&k,&n);
        for (int j=0;j<n;j++)
        {
            scanf("%d",gi+j);
        }
        init();
        if(sum[0][n-1]<=k)
        {
           printf("Case #%d: %I64d\n",i,r*sum[0][n-1]);
           continue;
        }
        int index = 0;
        int p = 0;
        __int64 ans = 0;
        int tp=0,tindex=0;
        int cnt =0;
        while (true)
        {
            if (sum[index][p]<=k)
            {
               // printf("tp %d\n",tp);
                tp = p;
                p = (p+1)%n;
            }
            else
            {
                cnt++;
                if(cnt>r)
                {
                    break;
                }
                //printf("tt %d\n",tindex);
                tindex = index;
                ans+=sum[tindex][tp];
                index = (tp+1)%n;
            }
        }
          printf("Case #%d: %I64d\n",i,ans);
    }


    return 0;
}
