#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

int i,j,n,t,k,s,rs;
int a[1005];

bool cmp(int x,int y)
{
    return x<y;
}

int main()
{
    freopen("C-large.in","r",stdin);freopen("c-large-out.out","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d",&n);
        s=0;rs=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            s=s^a[i];
            rs+=a[i];
        }
        if(s!=0)
            printf("Case #%d: NO\n",k);
        else
        {
            sort(a,a+n,cmp);
            printf("Case #%d: %d\n",k,rs-a[0]);
        }
    }
    
    return 0;
}
