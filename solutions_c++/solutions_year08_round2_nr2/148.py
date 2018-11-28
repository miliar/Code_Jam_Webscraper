
#include <cstdio>
#include <vector>
using namespace std;

int big [1024];
int g [1024][1024];
bool mark [16384];

long long gcd (long long a, long long b)
{
    return (b == 0 ? a : gcd (b, a % b));
}
inline bool prime (int n)
{
    if (n == 2)
        return true;
    if (n % 2 == 0)
        return false;
    for (int j = 2; j * j <= n; ++j)
        if (n % j == 0)
            return false;
    return true;
}
void dfs (int at)
{
    mark [at] = true;
    for (int j = 0; j <= 1000; ++j)
        if (g [at][j] == 1 && !mark [j])
            dfs (j);
}
int main ()
{
    vector <int> primes;
    for (int i = 2; i <= 1000; ++i)
        if (prime (i))
        {
            primes.push_back (i);
//            printf ("%d\n", i);
        }
    // what about 1
    for (int i = 2; i <= 1000; ++i)
        for (int j = primes.size () - 1; j >= 0; --j)
        {
            if (i % primes [j] == 0)
            {
                big [i] = primes [j];
                break;
            }
        }
    int C;
    scanf ("%d", &C);
    for (int t = 0; t < C; ++t)
    {
        int a, b, p;
        scanf ("%d %d %d", &a, &b, &p);
        /*
        memset (mark, 0, sizeof (mark));
        for (int i = a; i <= b; ++i)
        {
            if (!mark [i])
            {
                //printf ("%d ", i);
                ++res;
            }
            puts ("");
            for (int j = i + 1; j <= b; ++j)
                if (big [gcd (i, j)] >= p)
                {
                    printf ("%d -> %d\n", i, j);
                    mark [j] = true;
                }
        }*/
        memset (g, 0, sizeof (g));
        for (int i = a; i <= b; ++i)
            for (int j = a; j <= b; ++j)
                g [i][j] = (big [gcd (i, j)] >= p ? 1 : 0);
        long long res = 0;
        memset (mark, 0, sizeof (mark));
        for (int i = a; i <= b; ++i)
            if (!mark [i])
            {
                ++res;
                dfs (i);
            }
        printf ("Case #%d: %lld\n", t + 1, res);
    }
    return 0;
}