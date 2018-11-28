#include<iostream>
using namespace std;
int cn,i,j,k,lef,n,m,ci;
int pre[1001000],next[1001000];
int a[1001000];

int main()
{
  freopen("c_small.out","w",stdout);
  scanf("%d",&cn);
  ci=0;
  while (cn--)
  {
    ci++;
    scanf("%d",&n);
    for (i=1;i<=n;i++) 
    {
      pre[i]=i-1;
      next[i]=i+1;
    }
    pre[1]=n;
    next[n]=1;
    next[0]=1;
    k=0;
    lef=n;
    for (i=1;i<=n;i++)
    {
      j=(i-1)%lef+1;
      
      if (j<=lef/2)
      {
        while (j--) k=next[k];
      }
      else
      {
        j=lef-j+1;
        while (j--) k=pre[k];
      }
      
      //while (j--) k=next[k];
      a[k]=i;
      next[pre[k]]=next[k];
      pre[next[k]]=pre[k];
      lef--;
    }
    printf("Case #%d:",ci);
    scanf("%d",&m);
    for (i=0;i<m;i++)
    {
      scanf("%d",&j);
      printf(" %d",a[j]);
    }
    printf("\n");
  }
  return 0;
}