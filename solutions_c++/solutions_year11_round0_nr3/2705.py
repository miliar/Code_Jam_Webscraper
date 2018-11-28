#include <stdio.h>
#include <stdlib.h>

int main()
{
  freopen("hey.in","r",stdin);
  freopen("hey.out","w",stdout);
  int t,to=0;
  scanf("%d",&t);
  while(t--)
  {
    to++;
    printf("Case #%d: ",to);
    int n,s=1,i,a[1001];
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
      scanf("%d",&a[i]);
      s*=2;
    }
    bool b[102]={0};
    int too=0,max=0,j;
    while(1)
    {
      int rsum=0,sum1=0,sum2=0;
      too++;
      if(too>=(s-1)) break;
      if(b[n]==0) b[n]=1;
      else
      {
        b[n]=0;
        j=n;
        while(1)
        {
          j--;
          if(b[j]==1) b[j]=0;
          else if(b[j]==0)
          {
            b[j]=1;
            break;
          }
          else if(j<=0) break;
        }
      }
      for(i=1;i<=n;i++)
        {
          if(b[i]==0) {sum1^=a[i]; /*printf("0=%d %d ",a[i],sum1);*/}
          else if (b[i]==1){sum2^=a[i]; rsum+=a[i]; /*printf("1=%d %d ",a[i],sum2);*/}
        }
        //printf("\n");
        //printf("%d %d\n",sum1,sum2);
      if(sum2==sum1) 
      {
        if(rsum>max)
        max=rsum;
      }
    }
    if(max==0) printf("NO\n");
    else printf("%d\n",max);
  }
  return 0;
}
