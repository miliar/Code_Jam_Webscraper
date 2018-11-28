#include <cstdio>
#include <cmath>
#define FOR(x,y,z) for(int x=y;x<z;x++)
using namespace std;

int main()
{
  int Z;
  scanf("%d",&Z);
  FOR(i,1,Z+1)
  {
    int n,k;
    scanf("%d%d",&n,&k);
    printf("Case #%d: ",i);
    printf(((k%(1<<n)==((1<<n)-1)))?"ON":"OFF");
    putchar('\n');
  }
  return 0;
}
