#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;

int getsteps(int l, int r, int C)
{
  fprintf(stderr, "%d %d %d\n", l, r, C);
  if((ll)l*C >=r ) return 0;

  int m = (int)sqrt(((long double) l)*r);
  if( max(1.0*r/m,1.0*m/l) > max(1.0*r/(m+1), 1.0*(m+1)/l) ) m++;

  if(1.0*r/m < 1.0*m/l) return 1+getsteps(l, m, C);
  else return 1+getsteps(m, r, C);
}

int main()
{
  int cases;
  scanf("%d", &cases);
  for(int T=1; T<=cases; T++){
    printf("Case #%d: ", T);
    int l, r, C;
    scanf("%d%d%d", &l, &r, &C);
    printf("%d\n", getsteps(l, r, C));
  }
  return 0;
}
