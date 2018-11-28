#include<stdio.h>
  
  
main()
{
  freopen("h.in","r",stdin);
  freopen("h.out","w",stdout);
      
  int a1,b,t,T,i,x,j,y,k,a[10],p;
  
  scanf("%d",&T);
  
  for(t=1;t<=T;t++)
  {
    scanf("%d%d",&a1,&b);
    int s=0;
    for(i=a1;i<b-1;i++)
    {
      x=i;
      j=0;
      while(x>0)
      {
        j++;
        a[j]=x%10;
        x/=10;
      }
      bool bo[2000001]={0};
      for(y=1;y<j;y++)
      {
        p=a[y];
        for(k=y-1;k>=1;k--)
          p=p*10+a[k];
        for(k=j;k>y;k--)
          p=p*10+a[k];
        if(i<p && p<=b && bo[p]==0){s++;bo[p]=1;}
      }
    }
    printf("Case #%d: %d\n",t,s);
  }
}
