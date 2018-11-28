#include <cstdio>

int i,j,n,k,t,x,a[40];
int main()
{
  freopen("file.in","r",stdin);
  freopen("file.out","w",stdout);
  scanf("%d",&t);
  a[1]=1;
  for(i=2;i<=30;i++)
  a[i]=2*a[i-1]+1;
  for(i=1;i<=30;i++)
  a[i]++;
  for(j=0;j<t;j++)
  {
     scanf("%d%d",&n,&k);
     if (n==1)
     {
        if (k%2) printf("Case #%d: ON\n",j+1); else printf("Case #%d: OFF\n",j+1);        
     } else
     {
     if (k==a[n]-1) printf("Case #%d: ON\n",j+1); else
     {
         if (k%a[n]==a[n]-1) printf("Case #%d: ON\n",j+1); else printf("Case #%d: OFF\n",j+1);
     }
     }
  }
  return 0;
}
