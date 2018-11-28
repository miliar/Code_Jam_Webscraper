#include <cstdio>
#include <algorithm>

using namespace std;

const int A_MAX = 99999;
double t[A_MAX];

int main()
{
   int T;
   scanf("%d", &T);
   for(int i=1; i<=T; i++)
   {
      int A, B;
      scanf("%d %d", &A, &B);
      for(int j=0; j<A; j++)
	 scanf("%lf", &t[j]);
      double c = 1.0;
      double b = 1000000.0;
      for(int j=0; j<=A; j++)
      {
	 b = min(b, c*(A-2*j+B+1)+(1-c)*(A-2*j+2*(B+1)));
	 c *= t[j];
      }
      b = min(b, B+2.0);
      printf("Case #%d: %lf\n", i, b);
   }
   return 0;
}