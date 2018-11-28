#include"cstdio"
int main()
{
  int t,n,k,c1;
  freopen("A-large.in","r",stdin);
  freopen("test.out","w",stdout);
  scanf("%d",&t);
  for(c1=0;t>c1;c1++)
  {
    scanf("%d %d",&n,&k);
    if(((1<<n)-1)==(k%(1<<n)))
      printf("Case #%d: ON\n",c1+1);
    else
      printf("Case #%d: OFF\n",c1+1);
  }
}
