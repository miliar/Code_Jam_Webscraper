#include <iostream>
#include <assert.h>

using namespace std;

const int MAX_M = 11000;
const int INF = MAX_M*2;

int M, K, V;
int G[MAX_M];
int C[MAX_M];
int d[MAX_M][2];

int calcg(int g, int v1, int v2)
{
    if (g == 0)
        return v1||v2;
    else if (g == 1)
        return v1&&v2;

    assert(0);
    return -1;
}

int calc(int i, int v)
{
    assert(i < M);
    assert(v == 0 || v == 1);

    if (d[i][v] == -1)
    {
        int& res = d[i][v];
        res = INF;

        if (i >= K)
            res = (v == G[i] ? 0 : INF);
        else
        {
            for (int s1=0; s1 < 2; s1++)
                for (int s2=0; s2 < 2; s2++)
                    for (int g=0; g < 2; g++)
                        if (calcg(g, s1, s2) == v && (g == G[i] || C[i]))
                        {
                            int cur = calc(2*i+1, s1) + calc(2*i+2, s2) + (g != G[i]);
                            if (cur < res)
                                res = cur;
                        }
        }
    }

    return d[i][v];
}

void solve()
{
    cin >> M >> V;
    K = (M-1)/2;

    for (int i=0; i < K; i++)
        cin >> G[i] >> C[i];

    for (int i=K; i < M; i++)
        cin >> G[i];

    memset(d, -1, sizeof(d));
    int res = calc(0, V);
    if (res < INF)
        cout << res;
    else
        cout << "IMPOSSIBLE";
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;

    for (int i=1; i <= T; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
}
