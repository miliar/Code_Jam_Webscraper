#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 1000005;

bool prime [MAX];
long long N;

void sieve ()
{
    memset (prime, true, sizeof (prime));
    prime [0] = prime [1] = false;

    for (int i = 2; i * i < MAX; i++)
        if (prime [i])
            for (int j = i * i; j < MAX; j += i)
                prime [j] = false;
}

void solve_case ()
{
    scanf ("%lld", &N);
    int count = N > 1 ? 1 : 0;

    for (int i = 2; (long long) i * i <= N; i++)
        if (prime [i])
        {
            long long p = i;

            while (p * i <= N)
            {
                p *= i;
                count++;
            }
        }

    printf ("%d\n", count);
}

int main ()
{
    sieve ();
    int T; scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        printf ("Case #%d: ", tc);
        solve_case ();
    }

    return 0;
}
