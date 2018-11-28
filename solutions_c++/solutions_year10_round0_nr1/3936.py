#include <stdio.h>

long n,k,cnt[32];
bool on[40],light;
main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-small.out","w",stdout);
  long i,j,t;
  
  cnt[1] = 1;
  for(n=2;n<=30;n++)
  {
    cnt[n] = cnt[n-1]*2+1;
  }
  
  scanf("%d",&t);
  
  
  for(i=1;i<=t;i++)
  {
    scanf("%d %d",&n,&k);
    
    printf("Case #%d: ",i);
    k -= cnt[n];
    if( k < 0){ printf("OFF\n"); continue; }
    if( k == 0){ printf("ON\n"); continue; }
    k = k%(cnt[n]+1);
    if( k > 0){ printf("OFF\n"); continue; }
    if( k == 0){ printf("ON\n"); continue; }
  }
}
