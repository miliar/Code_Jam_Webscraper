#include<cstdio>
using namespace std;

int main()
{
  int z,t=1;
  scanf("%d",&z);
  while(t<=z)
  {
    int n,k;
    scanf("%d %d",&n,&k);
    if(k%(1<<n)==(1<<n)-1)printf("Case #%d: ON\n",t);
    else printf("Case #%d: OFF\n",t);
    t++;
  }
  return 0;
}
