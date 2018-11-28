#include <cstdio>
#include <cstring>
using namespace std;

const int MAXS = 105, STR = 105;

int N, S, Q, next, count, ans, seen [MAXS];
char engine [MAXS][STR], query [STR];

inline int efind (char *str)
{
    for (int i = 0; i < S; i++)
        if (strcmp (str, engine [i]) == 0)
            return i;

    return -1;
}

int main ()
{
    scanf ("%d", &N);

    for (int t = 0; t < N; t++)
    {
        scanf ("%d\n", &S);

        for (int i = 0; i < S; i++)
            gets (engine [i]);

        memset (seen, -1, sizeof (seen));
        next = count = ans = 0;

        scanf ("%d\n", &Q);

        for (int i = 0; i < Q; i++)
        {
            gets (query);

            if (seen [efind (query)] != next)
            {
                seen [efind (query)] = next;
                count++;

                if (count == S)
                {
                    ans++;
                    seen [efind (query)] = ++next;
                    count = 1;
                }
            }
        }

        printf ("Case #%d: %d\n", t + 1, ans);
    }

    return 0;
}
