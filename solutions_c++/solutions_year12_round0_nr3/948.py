#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char str[150];
int init(int n)
{
    if(n<10)
       return 1;
    if(n<100)
       return 10;
    if(n<1000)
       return 100;
    if(n<10000)
       return 1000;
    if(n<100000)
       return 10000;
    if(n<1000000)
       return 100000;
    if(n<10000000)
       return 1000000;
}
int n,a,b;
int main()
{
    freopen("D:\\C-large.in", "r", stdin);
    freopen("D:\\out.txt", "w", stdout);
    scanf("%d",&n);
    for(int cas=1;cas<=n;cas++)
    {
        scanf("%d%d",&a,&b);
        int ans=0;
        for(int i=a;i<=b;++i)
        {
            int tb=init(i);
            int ta=(i%10)*tb+i/10;
            while(ta)
            {
                if(ta==i)
                   break;
                if(ta>i && ta>=a && ta<=b)
                {
                    ans++;
                }
                ta =(ta%10)*tb+ta/10;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
