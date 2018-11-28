#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int t, n, s, p,l=0;
int x, ans;
void mainwork()
{
        l++;
        scanf("%d%d%d", &n, &s, &p);
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &x);
            if (x == 0 && p == 0) ans++;
            if (x >= 1 && (x + 2) / 3 >= p) ans++;
            else
            {
                if (s > 0 && x >= 2 && (x + 4) / 3 >= p)
                {
                    ans++;
                    s--;
                }
            }
        }
        printf("Case #%d: %d\n", l, ans);
}
int main()
{
  //  freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    while (t--) mainwork();
    return 0;
}
