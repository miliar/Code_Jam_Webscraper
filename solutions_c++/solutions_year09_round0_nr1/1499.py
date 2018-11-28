#include <cstdio>
#include <cstring>
using namespace std;

const int MAXL = 16, MAXD = 5005;

int L, D, N;
char words [MAXD][MAXL];
bool ok [MAXL][26];

inline bool good (int num)
{
    for (int i = 0; i < L; i++)
        if (!ok [i][words [num][i] - 'a'])
            return false;

    return true;
}

int main ()
{
    scanf ("%d %d %d", &L, &D, &N);

    for (int i = 0; i < D; i++)
        scanf ("%s", words [i]);

    for (int n = 1; n <= N; n++)
    {
        memset (ok, false, sizeof (ok));

        for (int i = 0; i < L; i++)
        {
            char c; scanf (" %c", &c);

            if (c == '(')
            {
                scanf (" %c", &c);

                do
                {
                    ok [i][c - 'a'] = true;
                    scanf (" %c", &c);
                }
                while (c != ')');
            }
            else
                ok [i][c - 'a'] = true;
        }

        int total = 0;

        for (int i = 0; i < D; i++)
            if (good (i))
                total++;

        printf ("Case #%d: %d\n", n, total);
    }

    return 0;
}
