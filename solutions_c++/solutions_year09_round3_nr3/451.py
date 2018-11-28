#include <stdio.h>

long p,q,pr[10],ans,cans;
bool fix[200];
void GoPrisoner(long day)
{
  if(day==q+1)
  {
    if(ans>cans) ans = cans;
    return;
  }
  long i,tmp,j;
  for(i=0;i<q;i++)
    if(!fix[pr[i]])
    {
      fix[pr[i]]=true;
      tmp = cans;
      j = pr[i]+1;
      while(!fix[j] && j<=p) cans++,j++;
      j = pr[i]-1;
      while(j>0)
        if(fix[j])break;else cans++,j--;
      
      GoPrisoner(day+1);
      
      cans = tmp;
      fix[pr[i]]=false;
    }
}

main()
{
  freopen("file.in","r",stdin);
  freopen("file.out","w",stdout);
  long tc,t,i,j;
  scanf("%d\n",&t);
  for(tc=1;tc<=t;tc++)
  {
    scanf("%d %d",&p,&q);
    for(i=0;i<q;i++)
      scanf("%d",&pr[i]);
    for(i=0;i<150;i++)
      fix[i]=false;
    ans = 200000000; cans = 0;
    GoPrisoner(1);
    
    printf("Case #%d: %d\n",tc,ans);
  }
}
