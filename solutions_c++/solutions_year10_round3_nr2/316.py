#include<iostream>
#include<cstdio>
using namespace std;

__int64 l,p,c,k,a,t,ans,bla;

int main()
{
    scanf("%I64d",&t);
    for(;t;t--)
    {
        bla++;
        k=0;
        scanf("%I64d%I64d%I64d",&l,&p,&c);
        while(l*c<p)
        {
            l*=c;
            k++;
        }
        ans=0;
        while(k)
        {
            k--;
            k=(k/2)+(k&1);
            ans++;
        }
        printf("Case #%I64d: %I64d\n",bla,ans);
    }
}
