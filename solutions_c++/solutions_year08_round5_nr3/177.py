#include <cstdio>
#include <cstdlib>

#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

char A[16][16];
int N, M;

void read_one()
{
    int i, j;

    cin >> M >> N;
    for (i = 1; i <= M; i++)
        scanf ("%s", A[i]);
}

inline int gb(const int& conf, const int& bit)
{
    return conf & (1 << bit);
}


int C[1 << 11], NC[1 << 11];
bool isbad[1 << 11][1 << 11];
int bitcount[1 << 11];

void solve_one()
{
    bool ok;
    int i, nxt, cur, k;
    memset (C, 0, sizeof(C));


    for (i = 1; i < (1 << N); i++)
        C[i] = -999999;

    for (i = 1; i <= M; i++) {
        memset (NC, 0, sizeof(NC));
        for (cur = 0; cur < (1 << N); cur ++)
        for (nxt = 0; nxt < (1 << N); nxt ++) {
            if (isbad[cur][nxt]) continue;
            ok = true;
            for (k = 0; k < N; k++)
                if (gb(nxt, k) && A[i][k] == 'x')
                    ok = false;
            if (! ok) continue;
            NC[nxt] = max(NC[nxt], C[cur] + bitcount[nxt]);
        }
        memcpy(C, NC, sizeof(NC));
    }

    int best = 0;
    for (i = 0; i < (1 << N); i++)
        best = max(best, C[i]);

    cout << best;
}


int main(void)
{
    int T, i, cur, nxt, k;

    for (cur = 0; cur < (1 << 10); cur ++) {
        for (k = 0; k < 10; k++)
            if (gb(cur,k))
                bitcount[cur] ++;
        for (nxt = 0; nxt < (1 << 10); nxt ++) {
            for (k = 0; k < 10; k++) 
            if (gb(nxt, k))
            {
                if (k - 1 >= 0 && (gb(nxt, k - 1) || gb(cur, k - 1))) {
                    isbad[cur][nxt] = true;
                    break;
                }
                if (k < 10 && (gb(nxt, k + 1) || gb(cur, k + 1))) {
                    isbad[cur][nxt] = true;
                    break;
                }
            }
        }
    }

    for(scanf("%d\n", &T), i = 1; i <= T; i++) {
        read_one();
        printf ("Case #%d: ", i);
        solve_one();
        printf ("\n");
    }
}

