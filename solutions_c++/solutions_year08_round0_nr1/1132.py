#include <cstdio>

#include <map>
#include <algorithm>
#include <string>

using namespace std;

void fix_string(char *s)
{
    for (; *s && *s != '\n'; s++);
    *s = 0;
}

string read_string()
{
    char buf[128];
    fgets(buf, 128, stdin);
    fix_string(buf);
    return string(buf);
}

string engines[128];
int best[128], nbest[128];

void solve_one(int T)
{
    int S, Q, i, j;

    scanf ("%d\n", &S);

    for (i = 0; i < S; i++)
        engines[i] = read_string();
    
    memset(best, 0, sizeof(best));

    scanf ("%d\n", &Q);
    for (; Q--;) {
        string query = read_string();
        for (i = 0; i < S; i ++) {
            if (query == engines[i]) {
                nbest[i] = 9999;
            } else {
                nbest[i] = best[i];
                for (j = 0; j < S; j++)
                    nbest[i] = min(nbest[i], 1 + best[j]);
            }
        }
        memcpy (best, nbest, sizeof(best));
    }

    int sol = 9999;
    for (i = 0; i < S; i++)
        sol = min(sol, best[i]);

    printf ("Case #%d: %d\n", T, sol);
}

int main()
{
    int N, i;
    scanf ("%d", &N);

    for (i = 1; i <= N; i++)
        solve_one(i);

    return 0;
}

