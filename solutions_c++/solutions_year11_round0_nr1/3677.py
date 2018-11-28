#include<iostream>
#include<cstdio>
#include<string.h>
#include<cstdlib>
#include<algorithm>
using namespace std;

int main()
{
    int n,time,t,on,bn,optr,bptr;

    int a[110];
    int B[110];
    int O[110];
    char c[110][10];
    freopen("1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%d",&n);
        on = 0;
        bn = 0;
        optr = 0;
        bptr = 0;
        for(int i=0;i<n;i++)
        {
            scanf("%s%d",c[i],&a[i]);
            if(c[i][0] == 'O')
                O[on++] = a[i];
            else B[bn++] = a[i];
        }
        int o=1,b=1;
        int ans = 0;
        for(int i=0;i < n;i++)
        {
            if(strcmp(c[i],"O") == 0)
            {
                time = abs(a[i] - o) + 1;
                ans += time;
                o = a[i];
                if(time < abs(B[bptr] - b))
                {
                    if(B[bptr] > b) b += time;
                    else b -= time;
                }
                else b = B[bptr];
                optr++;
            }
            else
            {
                time = abs(a[i] - b) + 1;
                ans += time;
                b = a[i];
                if(time < abs(O[optr] - o))
                {
                    if(O[optr] > o) o += time;
                    else o -= time;
                }
                else o = O[optr];
                bptr++;
            }
        }
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
