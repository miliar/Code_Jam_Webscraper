#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
int a[102];
int B[102];
int O[102];
char c[102][2];
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,i,step,t,k,on,bn,oi,bi;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        on = bn = oi = bi = 0;
        for(i=0;i<n;i++)
        {
            scanf("%s%d",c[i],&a[i]);
            if(strcmp(c[i],"O") == 0) O[on++] = a[i];
            else B[bn++] = a[i];
        }
        int o=1,b=1;
        int ans = 0;
        for(i=0;i<n;i++)
        {
            if(strcmp(c[i],"O") == 0)
            {
                step = abs(a[i] - o) + 1;
                ans += step;
                o = a[i];
                if(step < abs(B[bi] - b))
                {
                    if(B[bi] > b) b += step;
                    else b -= step;
                }
                else b = B[bi];
                oi++;
            }
            else
            {
                step = abs(a[i] - b) + 1;
                ans += step;
                b = a[i];
                if(step < abs(O[oi] - o))
                {
                    if(O[oi] > o) o += step;
                    else o -= step;
                }
                else o = O[oi];
                bi++;
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
