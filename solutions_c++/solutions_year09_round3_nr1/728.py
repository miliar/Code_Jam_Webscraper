#include <cstdio>
#include <cstring>
using namespace std;

//#define DEBUG

#ifdef DEBUG
#define debug(what...) fprintf (stderr, "[DEBUG] " what) 
#else
#define debug(what...)
#endif // DEBUG

typedef long long llong;
typedef unsigned long long ullong;

//const ullong MOD = 1000000007;

void redirect () 
{
//    freopen ("A-test.in", "rt", stdin);
//    freopen ("A-small-attempt0.in", "rt", stdin);
//    freopen ("A-small-attempt0.out", "wt", stdout);
    freopen ("A-large.in", "rt", stdin);
    freopen ("A-large.out", "wt", stdout);
}

char s[62];
int d[36];
bool u[36];
int b;

int index (char c)
{
    return c <= '9' ? c - '0' : c - 'a' + 10;
}

int main () 
{
    redirect ();
    int tc, n_cases;
    scanf ("%d", &n_cases);
    for (int tc = 1; tc <= n_cases; ++tc) 
    {
        debug ("Case #%d:\n", tc);
        scanf ("%s\n", s);
        b = 0;
        memset (d, -1, sizeof (d));
        memset (u, 0, sizeof (u));
        for (char *p = s; *p; ++p)
        {
            int j = index (*p);
            debug ("pos %d: '%c' index = %d\n", p - s, *p, j);
            if (d[j] >= 0)
                continue;
            for (int i = 0; i < 36; ++i)
            {
                if (i == 0 && p == s || u[i])
                    continue;
                debug ("d[%d] == %d\n", j, d[j]);
                d[j] = i;
                u[i] = true;
                ++b;
                debug ("'%c' == %d, base = %d\n", *p, i, b);
                break;
            }
        }
        if (b < 2)
            b = 2;
        llong k = 0;
        for (char *p = s; *p; ++p)
            (k *= b) += d[index (*p)];
        printf ("Case #%d: %lld\n", tc, k);
    }
    return 0;
}
