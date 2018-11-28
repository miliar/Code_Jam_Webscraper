#include <iostream>
#include <string>
#include <set>

using namespace std;


int a[1100], b[1100];


int sgn(int v)
{
     if(v > 0)
     {
          return 1;
     }
     if(v < 0)
     {
          return -1;
     }
     return 0;
}


int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);
     int t;
     scanf("%d", &t);
     for(int i = 0; i < t; i++)
     {
          int res = 0;
          printf("Case #%d: ", i + 1);
          int n;
          scanf("%d", &n);
          for(int j = 0; j < n; j++)
          {
               scanf("%d%d", &a[j], &b[j]);
          }
          for(int j = 0; j < n; j++)
          {
               for(int k = j + 1; k < n; k++)
               {
                    int v1 = sgn(a[j] - a[k]);
                    int v2 = sgn(b[j] - b[k]);
                    if(v1 * v2 < 0)
                    {
                         res++;
                    }
               }
          }
          printf("%d", res);
          printf("\n");
     }
     return 0;
}
