#include<stdio.h>

main()
{
  freopen("h.in","r",stdin);
  freopen("h.out","w",stdout);
  
  int t,n,tt,nn,p,k,s,i,a;
  
  scanf("%d",&t);
  for(tt=1;tt<=t;tt++)
  {
    scanf("%d%d%d",&nn,&p,&k);
    s=0;
    for(i=1;i<=nn;i++)
    {
      scanf("%d",&a);
      if((a+2)/3>=k)s++;
        else if(a/3!=0 && (3*k-4)<=a && p>0)
        {
          p--;
          s++;
        }
    }
    printf("Case #%d: %d\n",tt,s);
  }
}
