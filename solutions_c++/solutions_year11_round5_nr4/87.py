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

static ll get_sqrt(ll x)
{
    ll t = (ll) roundl(sqrtl((long double) x));
    if (t * t == x)
        return t;
    else
        return -1;
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        string S;
        cin >> S;
        int L = SZ(S);
        ll bits = 0, mask = 0;
        for (int i = 0; i < L; i++)
        {
            if (S[i] == '1')
                bits |= 1LL << (L - 1 - i);
            else if (S[i] == '?')
                mask |= 1LL << (L - 1 - i);
        }

        ll ans = get_sqrt(bits);
        for (ll j = mask; ans == -1 && j != 0; j = (j - 1) & mask)
        {
            ans = get_sqrt(bits | j);
        }
        assert(ans != -1);
        printf("Case #%d: ", cas + 1);

        ans *= ans;
        ll LA = 63 - __builtin_clzll(ans);
        for (int i = LA; i >= 0; i--)
            printf("%lld", (ans >> i) & 1);
        printf("\n");
    }
    return 0;
}
