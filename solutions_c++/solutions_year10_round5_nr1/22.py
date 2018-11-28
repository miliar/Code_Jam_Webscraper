#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) (x).begin(), (x).end()
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

static void redirect(int argc, const char **argv)
{
    if (argc > 1)
    {
        int fd = open(argv[1], O_RDONLY);
        if (fd == -1) { perror(argv[1]); exit(1); }
        if (-1 == dup2(fd, 0)) { perror(argv[1]); exit(1); }
        if (-1 == close(fd)) { perror(argv[1]); exit(1); }
    }

    if (argc > 2)
    {
        int fd = open(argv[2], O_WRONLY | O_CREAT, 0666);
        if (fd == -1) { perror(argv[2]); exit(1); }
        if (-1 == dup2(fd, 1)) { perror(argv[2]); exit(1); }
        if (-1 == close(fd)) { perror(argv[2]); exit(1); }
    }
}

static vector<int> primes;

static void make_primes()
{
    int N = 1000001;
    vector<bool> sieve(N, true);
    for (int i = 2; i < N; i++)
    {
        if (sieve[i])
        {
            primes.push_back(i);
            for (int j = i + i; j < N; j += i)
                sieve[j] = false;
        }
    }
}

static vector<int> factors(int x)
{
    vector<int> ans;
    for (int i = 0; i < SZ(primes); i++)
    {
        if (x == 1)
            break;
        int p = primes[i];
        if ((ll) p * p > x)
        {
            ans.push_back(x);
            break;
        }
        if (x % p == 0)
        {
            x /= p;
            while (x % p == 0)
                x /= p;
        }
    }
    return ans;
}

static ll mod(ll a, ll m)
{
    a %= m;
    if (a < 0) a += m;
    return a;
}

static ll inverse(ll a, ll m)
{
    if (a < 0) a += m;

    if (a == 1) return 1;
    return mod((1 - m * inverse(m % a, a)) / a, m);
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    make_primes();
    for (int cas = 0; cas < cases; cas++)
    {
        printf("Case #%d: ", cas + 1);

        ll D, K, S, A, B, prod;
        vector<ll> y;
        vi F;

        cin >> D >> K;
        int top = 1;
        for (int i = 0; i < D; i++)
            top *= 10;

        vector<ll> x(K + 1);
        for (int i = 0; i < K; i++)
            cin >> x[i];
        x[K] = -1;
        S = x[0];
        if (K <= 1) goto done;
        if (x[0] == x[1])
        {
            x[K] = x[0];
            goto done;
        }
        if (K <= 2)
            goto done;

        y.resize(K - 1);
        for (int i = 0; i + 1 < K; i++)
            y[i] = (x[i] - S * x[i + 1]);

        for (int i = 0; i < SZ(primes) && primes[i] <= top; i++)
        {
            ll out;

            ll P = primes[i];
            if (P <= x[0] || P <= x[1] || P <= x[2])
                continue;
            A = mod((x[1] - x[2]) * inverse(x[0] - x[1], P), P);
            B = mod(x[1] - A * S, P);

            for (int j = 1; j < K; j++)
                if (mod(x[j - 1] * A + B, P) != x[j])
                    goto bad;
            out = mod(x[K - 1] * A + B, P);
            if (x[K] != -1 && x[K] != out)
            {
                x[K] = -1;
                goto done;
            }
            x[K] = out;
bad:;
        }

done:
        if (x[K] != -1)
        {
            printf("%lld\n", x[K]);
            continue;
        }

        printf("I don't know.\n");
    }
    return 0;
}
