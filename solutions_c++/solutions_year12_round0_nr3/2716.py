#include<iostream>
#include<cstdio>
#include<cstring>
#include<map>
using namespace std;
int main()
{
    int n,t=0;
    scanf("%d",&n);
    while(t++<n)
    {
        int a,b,br=0,i,p=1,x;
        scanf("%d%d",&a,&b);
        x=a;
        while(x/=10)
        p*=10;
        for(i=a;i<b;i++)
        {
            map<int,bool> mp;
            int t=p,v=10;
            while(t)
            {
                x=i%t*v+i/t;
                if(x<=b&&i<x)
                {
                    if(mp[x]==0)
                    br++;
                    mp[x]=1;
                }
                t/=10;
                v*=10;
            }
        }
        printf("Case #%d: %d\n",t,br);
    }
    return 0;
}
