#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int list[10000];

void init()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++)
        scanf("%d", list + i);
}

void solve()
{
    int ret = 0;
    int sum = 0;
    for (int i = 0; i < n; i ++)
    {
        ret ^= list[i];
        sum += list[i];
    }

    sort(list, list + n);

    if (ret == 0)
    {
        printf("%d\n", sum - list[0]);
    }
    else
    {
        printf("NO\n");
    }

}

int main()
{
//    freopen("C-small-attempt0.in", "r", stdin);
//    freopen("C-small.out", "w", stdout);

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t ++)
    {
         printf("Case #%d: ", t);

         init();
         solve();
    }

    return 0;
}