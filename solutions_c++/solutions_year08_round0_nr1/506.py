
#include <map>
#include <string>
#include <iostream>
using namespace std;

const int MAXS = 128;
const int MAXQ = 1024;
const int INF = 0x3f3f3f3f;

int S, Q;
int best [MAXQ][MAXS];

string query [MAXQ];
string engine [MAXS];

int solve ()
{
    map <string, int> id;
    for (int i = 0; i < S; ++i)
        id [engine [i]] = i;
    memset (best, 0x3f, sizeof (best));
    for (int i = 0; i < S; ++i)
        best [0][i] = 0;
    for (int i = 0; i < Q; ++i)
        for (int j = 0; j < S; ++j)
            if (best [i][j] < INF)
            {
                int bid = (id.count (query [i]) ? id [query [i]] : -1);
                for (int k = 0; k < S; ++k)
                    if (k != bid)
                        best [i + 1][k] = min (best [i + 1][k], best [i][j] + (j != k ? 1 : 0));
            }
    int res = INF;
    for (int i = 0; i < S; ++i)
        res = min (res, best [Q][i]);
    return res;
}
int main ()
{
    int N;
    scanf ("%d\n", &N);
    
    for (int i = 1; i <= N; ++i)
    {
        scanf ("%d\n", &S);
        for (int j = 0; j < S; ++j)
            getline (cin, engine [j]);
        scanf ("%d\n", &Q);
        for (int j = 0; j < Q; ++j)
            getline (cin, query [j]);
        printf ("Case #%d: %d\n", i, solve ());
    }
    
    return 0;
}
