#include <cstdio>
using namespace std;

const int SIZE = 1000000;
bool ptable[SIZE];
int primes[SIZE];
int total;


void egcd(int a, int b, long long int& x, long long int& y, int p)
{
    if(!b)
    {
        x = 1;
        y = 0;
    }
    else
    {
        egcd(b, a % b, x, y, p);

        long long int t = x;
        x = y;
        y = (t - a / b * y) % p;
    }
}

long long int nev(int n, int p)
{
    long long int x, y;

    n %= p;
    if(n < 0)
        n += p;

    egcd(n, p, x, y, p);
    
    if(x < 0)
        x += p;

    return x;
}

void normal(long long int& n, int p)
{
    n %= p;
    if(n < 0)
        n += p;
}

int main()
{
    for(long long int i = 2; i < SIZE; i++)
        if(!ptable[i])
        {
            primes[total++] = i;
            for(long long int j = i * i; j < SIZE; j += i)
                ptable[j] = true;
        }

 
    int testcase;
    scanf("%d", &testcase);

    long long int ns[32];
    for(int casenum = 1; casenum <= testcase; casenum++)
    {
        printf("Case #%d: ", casenum);
        
        int D, K;
        scanf("%d%d", &D, &K);
        int bound = 1;
        while(D--)
            bound *= 10;

        for(int i = 0; i < K; i++)
            scanf("%lld", ns + i);

        if(K >= 2 && ns[0] == ns[1])
            printf("%lld\n", ns[0]);
        else if(K <= 2)
            printf("I don't know.\n");
        else
        {
            long long int A, B;
            int ansa, ansb;
            int ans = -1;
            int ansp;
            for(int i = 0; i < total && primes[i] <= bound; i++)
            {
                A = (nev(ns[0] - ns[1], primes[i]) * (ns[1] - ns[2]));
                normal(A, primes[i]);

                B = (ns[1] - A * ns[0]);
                normal(B, primes[i]);

                bool check = primes[i] > ns[0];
                for(int j = 0; check && j + 1 < K; j++)
                    if((ns[j] * A + B) % primes[i] != ns[j + 1])
                    {
                        check = false;
                        break;
                    }

                
                
                if(check)
                {
//printf("!%d\n", primes[i]);
                    int t = (A * ns[K - 1] + B) % primes[i];

                    if(ans != -1 && ans != t)
                    {

                        ans = -1;
                        break;
                    }
                    ansp = primes[i];
                    ansa = A;
                    ansb = B;
                    ans = t;//(A * ns[K - 1] + B) % primes[i];
                }
            }

        if(ans == -1)
            printf("I don't know.\n");
        else
        printf("%d\n", ans);//, ansa, ansb, ansp);
        }
    }
    return 0;
}
