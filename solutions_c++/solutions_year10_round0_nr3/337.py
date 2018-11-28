#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

int R; // times;
int k; // capacity
int N; // # of groups
__int64 group[1000];
int vis[1000];
int id[1000], next[1000];
__int64 gsum[1000];

int calnext(int a)
{
    int i = a;
    __int64 sum = group[a];
    int cnt = 1;
    while (1)
    {
        if (cnt == N) break;
        ++cnt;
        int j = (i + 1) % N;
        if (sum + group[j] > k) break;
        sum += group[j];
        i = j;
    }
    gsum[a] = sum;
    return (i + 1) % N;
}

void solve()
{
    fin >> R >> k >> N;
    for (int i = 0; i < N; ++i) fin >> group[i];
    for (int i = 0; i < N; ++i) next[i] = calnext(i);

    memset(vis, 255, sizeof(vis));
    vis[0] = 0;
    id[0] = 0;

    int i = 0;
    int M = 1;
    while (vis[next[i]] == -1)
    {
        i = next[i];
        vis[i] = M;
        id[M++] = i;
    }

    int n1 = vis[next[i]];
    int n2 = M - n1;

    __int64 ans = 0;
    if (R <= n1)
    {
        for (int i = 0; i < R; ++i) ans += gsum[id[i]];
        fout << ans << endl;
    }
    else
    {
        __int64 count[1000];
        count[0] = gsum[id[n1]];
        for (int i = 0; i < n1; ++i) ans += gsum[id[i]];
        for (int i = n1 + 1; i < M; ++i) count[i - n1] = count[i - n1 - 1] + gsum[id[i]];
        ans += (R - n1) / n2 * count[n2 - 1];
        if ((R - n1) % n2 > 0)
            ans += count[(R - n1) % n2 - 1];
        fout << ans << endl;
    }
}

int main()
{
    int T;
    fin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        fout << "Case #" << cas << ": ";
        solve();
    }
    return 0;
}
