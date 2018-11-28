#include <iostream>
#include <cstdlib>
using namespace std;

int cmp(long long a,long long b)
{
   return a>b;   
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a-large.txt","w",stdout);
    
    long long a[801],re,b[801];
    int cas,sen,t,tt,n;
    scanf("%d",&cas);
    for(sen=1;sen<=cas;sen++)
    {
        scanf("%d",&n);
        for(t=0;t<n;t++)
            scanf("%I64d",a+t);   
        for(t=0;t<n;t++)
            scanf("%I64d",b+t);
        sort(a,a+n);
        sort(b,b+n,cmp);        
        re=0;
        for(t=0;t<n;t++)
            re+=a[t]*b[t];
        printf("Case #%d: %I64d\n",sen,re);
    }
    //system("pause");
    return 0;   
}
