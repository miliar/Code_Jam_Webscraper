#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int t;
int money;
int p,n;
int m[1105];
int check[1105];

void search(int l,int h)
{
    int i,j,k,mid,flag=0;
    for(i=l;i<=h;i++)
    {
        if(check[i]+m[i]<p)
            flag=1;
    }
    if(flag==1)
    {
        money++;
        for(i=l;i<=h;i++)
            check[i]++;
        mid=(l+h)/2;
        search(l,mid);
        search(mid+1,h);
    }
    return;
}

int main()
{
    int i,j,k;
    freopen("B-small-attempt0.in","r",stdin);
  //   freopen("A-small-attempt1.in","r",stdin);
  //  freopen("A-small-attempt2.in","r",stdin);
  //  freopen("A-large.in","r",stdin);
   freopen("Bout.txt","w",stdout);
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        memset(check,0,sizeof(check));
        scanf("%d",&p);
        n=1;
        for(i=0;i<p;i++)
            n*=2;
        for(i=0;i<n;i++)
            scanf("%d",&m[i]);
        for(i=0;i<n-1;i++)
            scanf("%d",&m[1103]);
        money=0;
        search(0,n-1);
        printf("Case #%d: %d\n",k,money);
    }
    return 0;
}
