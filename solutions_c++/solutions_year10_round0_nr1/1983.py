#include<cstdio>
#include<algorithm>
using namespace std;
int T,N,K;
int main()
{
  int a,b,tc;
  scanf("%d",&T);
  for(tc=1;tc<=T;++tc)
  {
    scanf("%d %d",&N,&K);
    printf("Case #%d: ",tc);
    a=(1<<N)-1;b=(1<<N);
    if(K<a)printf("OFF\n");
    else
    {
      if((K-a)%b==0)printf("ON\n");
      else printf("OFF\n");
    }
  }
  return 0;
}