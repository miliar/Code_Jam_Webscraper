#include<iostream>
using namespace std;
int t,i,j,n,c,x,mini,tmp,tot;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        tot=x=0; mini=100000000;
        for(j=1;j<=n;j++)
        {
            scanf("%d",&tmp);
            x^=tmp;
            tot+=tmp;
            mini=(tmp<mini?tmp:mini);
        }
        if(x==0)
            printf("Case #%d: %d\n",i,tot-mini);
        else
            printf("Case #%d: NO\n",i);
    }
}
