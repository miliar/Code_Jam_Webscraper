#include <iostream>
#include <cmath>

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

using namespace std;

int i,j,k,l;
int n_tests,test;
int N,M,A;
int X1,Y1,x2,y2,x3,y3,possible;

int main()
{
  scanf("%d",&n_tests);
  for_to(test,1,n_tests)
  {
    scanf("%d %d %d",&N,&M,&A);
    X1=Y1=0;
    possible=0;
    for_to(x2,0,N)
    {
      if (possible) break;
      for_to(y2,0,M)
      {
        for_to(x3,0,N)
        {
          for_to(y3,0,M)
          {
            if (abs(x2*y3-x3*y2)==A)
            {
              if (!possible)
              {
                printf("Case #%d: %d %d %d %d %d %d\n",test,X1,Y1,x2,y2,x3,y3);
              }
              possible=1;
            }
          }
        }
      }
    }
    if (!possible) printf("Case #%d: IMPOSSIBLE\n",test);
  }

  return 0;
}
