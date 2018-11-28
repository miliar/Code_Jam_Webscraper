#include <iostream>
using namespace std;

const int maxN = 20001;

int N, desire, ans;
int G[maxN], C[maxN], GG[maxN];
int input[maxN], output[maxN];

int calc()
{
    int ret = 0;
    for (int i = N; i>=1; i--)
    {
        if (i>(N-1)/2) output[i] = input[i];
        else
        {
            output[i] = GG[i] ? (output[i*2] & output[i*2+1]) : (output[i*2] | output[i*2+1]);
            ret += GG[i] != G[i];
        }
    }
    return output[1]==desire ? ret : N;
}

long long dp[maxN][2][2];

int Value(int g, int x, int y)
{
    return g ? (x & y) : (x | y);
}

void Update(int i, int g, int v, long long& ret, int dt)
{
    ret = N;
    for (int x = 0; x<=1; x++)  
        for (int y = 0; y<=1; y++)
        {
            if (Value(g, x, y)!=v) continue;
            ret <?= dt + (dp[i*2][x][0]<?dp[i*2][x][1]) + (dp[i*2+1][y][0] <? dp[i*2+1][y][1]);
        }
}

void Solve()
{
    for (int i = N; i>=1; i--)
    {
        if (i>(N-1)/2)
        {
            dp[i][input[i]][0] = dp[i][input[i]][1] = 0;
            dp[i][1-input[i]][0] = dp[i][1-input[i]][1] = N;
        }else
        {
            Update(i, G[i], 0, dp[i][0][G[i]], 0);
            Update(i, G[i], 1, dp[i][1][G[i]], 0);
            if (C[i])
            {
               Update(i, 1-G[i], 0, dp[i][0][1-G[i]], 1);
               Update(i, 1-G[i], 1, dp[i][1][1-G[i]], 1);
            }else
            {
                dp[i][0][1-G[i]] = dp[i][1][1-G[i]] = N;
            }
        }
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int task;
    cin >> task;
    for (int cc = 1; cc<=task; ++cc)
    {
        cout << "Case #" << cc << ": ";
        cin >> N >> desire;
        for (int i = 1; i<=(N-1)/2; i++)
        {
            cin >> G[i] >> C[i];
        }
        for (int i = (N-1)/2+1; i<=N; i++)
        {
            cin >> input[i];
        }
        ans = N;
        Solve();
            for (int y = 0; y<=1; y++)
                ans <?= dp[1][desire][y];
        if (ans<N) cout << ans << endl; 
        else cout << "IMPOSSIBLE" << endl;
    }
}
