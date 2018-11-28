#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int cases;
    scanf("%d", &cases);
    for(int caseno=1; caseno<=cases; caseno++)
    {
       printf("Case #%d: ", caseno);
       int c;
       scanf("%d", &c);
       int s = 0, x = 0, m = 1<<25;
       while (c--)
       {
           int r;
           scanf("%d", &r);
           s += r;
           x ^= r;
           m = min(m, r);
       }
       if (x != 0)
       {
           printf("NO\n");
       }
       else
       {
           printf("%d\n", s-m);
       }
    }
}
