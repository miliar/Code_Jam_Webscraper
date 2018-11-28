#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int casen, n, m, a;

void init()
{
     scanf("%d%d%d", &n, &m, &a);
}

int calc(int x1, int y1, int x2, int y2)
{
     return abs(x1 * y2 - x2 * y1);
}


void check(int x1, int y1, int x2, int y2, int x3, int y3)
{
     if (x1 >= 0 && x1 <= n) {
        if (x2 >= 0 && x2 <= n) {
           if (x3 >= 0 && x3 <= n) {
              if (y1 >= 0 && y1 <= m) {
                 if (y2 >= 0 && y2 <= m) {
                    if (y3 >= 0 && y3 <= m) {
                       if (calc(x2 - x1, y2 - y1, x3 - x1, y3 - y1) == a) return;
                    }
                 }
              }
           }
        }
     }
     printf("Wrong!\n");
}

void work()
{
     for (int x1(-n); x1 <= n; ++x1)
     {
         for (int x2(x1); x2 <= min(n, x1 + n); ++x2)
         {
             for (int y1(-m); y1 <= m; ++y1)
             {
                 for (int y2(y1); y2 <= min(m, y1 + m); ++y2)
                 {
                     if (calc(x1, y1, x2, y2) == a) {
                        int deltax = abs(min(0, x1));
                        int deltay = abs(min(0, y1));
                        printf("%d %d %d %d %d %d\n", deltax, deltay, x1 + deltax, y1 + deltay, x2 + deltax, y2 + deltay);
                        
                        //check(deltax, deltay, x1 + deltax, y1 + deltay, x2 + deltax, y2 + deltay);
                        
                        
                        return;
                     }
                     if (calc(x1, y2, x2, y1) == a) {
                        int deltax = abs(min(0, x1));
                        int deltay = abs(min(0, y1));
                        printf("%d %d %d %d %d %d\n", deltax, deltay, x1 + deltax, y2 + deltay, x2 + deltax, y1 + deltay);
                        
                        //check(deltax, deltay, x1 + deltax, y2 + deltay, x2 + deltax, y1 + deltay);
                        
                        return;
                     }
                 }
             }
         }
     } 
                     
     printf("IMPOSSIBLE\n");
}
                     

int main()
{
    freopen("B-small.txt", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &casen);
    for (int i(1); i <= casen; ++i)
    {
        init();
        printf("Case #%d: ", i);
        work();
    } 
    return 0;
}
