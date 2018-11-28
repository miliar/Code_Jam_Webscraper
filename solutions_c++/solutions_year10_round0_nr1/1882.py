#include<stdio.h>
#include<algorithm>

using namespace std;

int a[50];

int main()
{
    int t,n,k,ks=1,i;
    a[1]=1;

    for(i=2;i<33;i++)
        a[i] = a[i-1]*2+1;
    freopen("a.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        if(a[n]==k)
            printf("Case #%d: ON\n",ks++);
        else if( k>a[n] && (k-a[n])%(a[n]+1)==0)
            printf("Case #%d: ON\n",ks++);
        else printf("Case #%d: OFF\n",ks++);
    }

    return 0;
}
