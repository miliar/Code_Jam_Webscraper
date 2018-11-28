#include <cstdio>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int primes[1000];

void gen_primes()
{
    primes[0] = 2;
    int n = 1;

    for (int i = 3; i < 10000000 && n < 1000; i += 2)
    {
        bool isPrime = true;
        for (int j = 0; isPrime && j < n; j++)
        {
            isPrime = (i % primes[j]);
        }

        if (isPrime)
        {
            primes[n++] = i;
        }
    }
}

int main( void )
{
    gen_primes();

    int N;
    scanf( "%d", &N );

    for (int tc = 0; tc < N; tc++)
    {
        int A, B, P;
        scanf( "%d%d%d", &A, &B, &P );

        int set[1010];
        for (int i = A; i <= B; i++) set[i] = i;

        int k = 0;
        while (primes[k] < P) k++;
        for (; primes[k] <= B; k++)
        {
            for (int i = A; i <= B; i++) if (i % primes[k] == 0)
            {
                for (int j = i+1; j <= B; j++) if (j % primes[k] == 0)
                {
                    int s = set[j];
                    for (int k = A; k <= B; k++) if (set[k] == s)
                    {
                        set[k] = set[i];
                    }
                }
                break;
            }
        }

        int cnt = 0;
        bool mark[1010];
        memset( mark, false, sizeof( mark ) );
        for (int i = A; i <= B; i++) if (!mark[set[i]])
        {
            mark[set[i]] = true;
            cnt++;
        }

        printf( "Case #%d: %d\n", tc+1, cnt );
    }
}
