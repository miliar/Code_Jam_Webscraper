#include <iostream>
using namespace std;

int T, Ti, P, Q, ans;
bool res[101];
int r[7], a[7];
bool vis[7];

void init()
{
    int i;

    ans = 2000000000;
    cin >> P >> Q;
    for (i = 1; i <= Q; i++)
        cin >> r[i];
}

void check()
{
    int i, j, k, temp = 0, x = 0;

    memset(res, 0, sizeof(res));
    res[0] = res[P + 1] = true;
    for (i = 1; i <= Q; i++)
    {
        temp = 0;
        j = a[i] - 1;
        while (!res[j])
        {
            temp++;
            j--;
        }
        j = a[i] + 1;
        while (!res[j])
        {
            temp++;
            j++;
        }
        res[a[i]] = true;
        x += temp;
    }
    if (x < ans) ans = x;
}

void dfs(int dep, int p)
{
    if (vis[p]) return;
    a[dep] = r[p];
    if (dep == Q)
    {
        check();
        return;
    }
    vis[p] = true;
    int i;
    for (i = 1; i <= Q; i++) dfs(dep + 1, i);
    vis[p] = false;

}

void work()
{
    int i;

    memset(vis, 0, sizeof(vis));
    for (i = 1; i <= Q; i++)
    {
        dfs(1, i);
    }
    cout << "Case #" << Ti << ": " << ans << endl;
}

long long main()
{
    cin >> T;
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }

   // system("pause");
    return 0;
}
