#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
//    freopen("C-large.in","r",stdin);
//    freopen("C-large.out","w",stdout);
    int a,b;
    int d[10],dnum;
    int ans;
    int lastans[10],lastcnt;
    int tem;
    int t;
    scanf("%d",&t);
    for(int cases = 1;cases<=t;cases++)
    {
        ans = 0;
        scanf("%d%d",&a,&b);
        for(int i=a;i<=b;i++)
        {
            memset(lastans,-1,sizeof(lastans));
            lastcnt = 0;
            tem = i;dnum = 0;
            while(tem)
            {
                d[dnum++] = tem%10;
                tem/=10;
            }
            for(int j=0;j<dnum-1;j++)
            {
                tem = 0;
                for(int k=j;k>=0;k--)
                {
                    tem *= 10;tem += d[k];
                }
                for(int k=dnum-1;k>j;k--)
                {
                    tem *= 10;
                    tem += d[k];
                }
                if(tem >= a&& tem<= b&& i<tem)
                {
                    int k;
                    for(k = 0;k<lastcnt;k++)
                    {
                        if(tem == lastans[k]) break;
                    }
                    if(k<lastcnt) continue;
                    else {ans++;lastans[lastcnt++] = tem;}
                }
            }
        }
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
