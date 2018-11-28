#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

void solve()
{
    int k;
    scanf("%d", &k);

    int ret = 0;

    int when[2] = {0, 0};
    int pos[2] = {1, 1};
    char buf[10];
    int target;
    int x;

    while (k --)
    {
        scanf("%s%d", buf, &target);
        if (buf[0] == 'O') x = 0;
        else x = 1;
        
        int now = max(ret + 1, when[x] + abs(pos[x] - target) + 1 );
        ret = now;
        when[x] = now;
        pos[x] = target;
    }

    printf("%d\n", ret);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t ++)
    {
        printf("Case #%d: ", t);

        solve();
    }


    return 0;
}