#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

void solve()
{
     int N, M, A;
     scanf("%d%d%d", &N, &M, &A);
     
     for (int x1 = 0; x1 <= N; x1++)
      for (int x2 = 0; x2 <= N; x2++)
       for (int y1 = 0; y1 <= M; y1++)
        for (int y2 = 0; y2 <= M; y2++)
        {
            if (abs(x1*y2 - x2*y1) == A)
            {
                 printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
                 return;
            }
        }
     printf("IMPOSSIBLE\n");
}
int main()
{
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
