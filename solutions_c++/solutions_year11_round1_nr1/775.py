#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

#define MAXN 1024

vector<int> p;
char marca[MAXN];

void criva()
{
    memset(marca, 0, sizeof(marca));

    marca[1] = 1;
    p.push_back(2);

    for (int i = 3; i < 100; i += 2)
    {
        if (marca[i]) continue;
        p.push_back(i);

        for (int j = i * i; j < 100; j += i)
        {
            marca[j] = 1;
        }
    }
}

long long gcd(long long a, long long b)
{
    return b? gcd(b, a%b):a;
}

int main (void)
{
    int cases;

    scanf ("%d", &cases);

    for (int caso = 1; caso <= cases; ++caso)
    {
        printf ("Case #%d: ", caso);

        long long  n, g, d;
        scanf ("%lld %lld %lld", &n, &d, &g);

        long long hj, total;

        hj = 100 / gcd(d,100);

        bool pode = false;
        if (hj <= n)
        {
            pode = true;
        }

        /*
        total = 100 / gcd(g, 100);

        if (total < hj)
        {
            pode = false;
        }
        */

        if (g == 100 && d != 100)
        {
            pode = false;
        }
        else if (g == 0 && d != 0)
        {
            pode = false;
        }

        if (pode)
        {
            printf ("Possible\n");
        }
        else
        {
            printf ("Broken\n");
        }
    }

    return 0;
}

