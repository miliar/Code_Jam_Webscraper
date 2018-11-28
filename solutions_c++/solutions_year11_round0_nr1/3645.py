#include<cstdio>
#include<cstdlib>
int main()
{
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;++i)
  {
    int n,po=1,pb=1,to=0,tb=0,time=0;
    scanf("%d",&n);
    for(int j=0;j<n;++j)
    {
      char r;
      int p;
      scanf(" %c%d",&r,&p);
      if(r=='O')
      {
        int tmp=abs(p-po)-to;
        if(tmp<0)
          tmp=0;
        ++tmp;
        time+=tmp;
        to=0;
        tb+=tmp;
        po=p;
      }
      else
      {
        int tmp=abs(p-pb)-tb;
        if(tmp<0)
          tmp=0;
        ++tmp;
        time+=tmp;
        tb=0;
        to+=tmp;
        pb=p;
      }
    }
    printf("Case #%d: %d\n",i,time);
  }
  return 0;
}
