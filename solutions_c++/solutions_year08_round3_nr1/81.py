#include<stdio.h>
#include<algorithm>
using namespace std;

int a[1010],i1,n1,i,k,p,l,n;
long long tot;

bool pr(int a1,int a2)
{
    return a1>a2;
}

int main()
{

    scanf("%d",&n1);
    for(i1=1;i1<=n1;i1++)
    {
        scanf("%d %d %d",&p,&k,&l);
        for(i=1;i<=l;i++)
        {
            scanf("%d",&a[i]);
        }    
        printf("Case #%d: ",i1);
        if(p*k<l)
        {
            printf("Impossible\n");
            continue;
        }
        sort(a+1,a+1+l,pr);
        tot=0;
        for(i=1;i<=l;i++)
        {
            n=(i-1)/k+1;
            tot+=(long long)(a[i])*n;
        }
        printf("%lI64d\n",tot);
    }
    return 0;
}
