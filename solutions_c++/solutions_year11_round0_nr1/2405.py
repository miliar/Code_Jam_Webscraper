#include <stdio.h>
#include <iostream>
#include <string>
#include <queue>

using namespace std;

#define MAXN 110
#define INF 1000*1000*1000
#define CODE(O, B, K) ((O) * MAXN * MAXN + (B) * MAXN + (K))
#define GETO(C) ((C) / MAXN / MAXN)
#define GETB(C) (((C) % (MAXN * MAXN)) / MAXN)
#define GETK(C) ((C) % MAXN)

int t, n, a[MAXN][MAXN][MAXN], btn[MAXN];
string who[MAXN];
queue<int> q;

void go(int O, int B, int K, int steps, bool pushed)
{
        if (who[K] == "B" && btn[K] == B)
        {
                if (a[O][B][K+1] > steps + 1)
                {
                        a[O][B][K+1] = steps + 1;
                        q.push(CODE(O, B, K + 1));
                }
        }
        int nxt = pushed ? 1 : 0;
        if (a[O][B][K+nxt] > steps + 1)
        {
                a[O][B][K+nxt] = steps + 1;
                q.push(CODE(O, B, K+nxt));
        }
        if (B > 1)
        {
                if (a[O][B-1][K+nxt] > steps + 1)
                {
                        a[O][B-1][K+nxt] = steps + 1;
                        q.push(CODE(O, B-1, K+nxt));
                }
        }
        if (B < 100)
        {
                if (a[O][B+1][K+nxt] > steps + 1)
                {
                        a[O][B+1][K+nxt] = steps + 1;
                        q.push(CODE(O, B+1, K+nxt));
                }
        }
}

void go(int O, int B, int K)
{
        if (who[K] == "O" && btn[K] == O)
                go(O, B, K, a[O][B][K], true);
        go(O, B, K, a[O][B][K], false);
        if (O > 1)
                go(O-1, B, K, a[O][B][K], false);
        if (O < 100)
                go(O+1, B, K, a[O][B][K], false);
}

int solve()
{
        cin >> n;
        for (int i = 0; i < n; i++)
                cin >> who[i] >> btn[i];
        while (!q.empty())
                q.pop();
        a[1][1][0] = 0;
        q.push(CODE(1, 1, 0));
        while (!q.empty())
        {
                int cur = q.front();
                q.pop();
                int O = GETO(cur);
                int B = GETB(cur);
                int K = GETK(cur);
                go(O, B, K);
        }

        int ans = INF;
        for (int i = 0; i < MAXN; i++)
                for (int j = 0; j < MAXN; j++)
                        ans = min(ans, a[i][j][n]);
        return ans;
}

int main()
{
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        cin >> t;
        for (int test = 1; test <= t; test++)
        {
                for (int i = 0; i < MAXN; i++)
                        for (int j = 0; j < MAXN; j++)
                                for (int k = 0; k < MAXN; k++)
                                        a[i][j][k] = INF;
                cout << "Case #" << test << ": " << solve() << endl;
        }
}