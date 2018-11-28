#include<cstdio>
using namespace std;

int main()
{
  int t=0,tt; scanf("%d",&tt);
  while(t<tt)
  {
    int n,k; scanf("%d%d",&n,&k);
    int m=(1<<n)-1;
    printf("Case #%d: ",++t);
    if((k&m)==m) printf("ON\n"); else printf("OFF\n");
  }

  return 0;
}
