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

#define MOD 100003

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    ll choose[501][501];
    for (int i = 0; i <= 500; i++)
    {
        choose[i][0] = choose[i][i] = 1;
        for (int j = 1; j < i; j++)
            choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD;
    }

    ll dp[501][501];
    for (int i = 2; i <= 500; i++)
    {
        dp[i][1] = 1;
        for (int s = 2; s < i; s++)
        {
            ll v = 0;
            // s - m - 1 <= i - s - 1 <=> m >= 2 * s - i
            for (int m = max(1, 2 * s - i); m < s; m++)
                v = (v + choose[i - s - 1][s - m - 1] * dp[s][m]) % MOD;
            dp[i][s] = v;
        }
    }

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int N;
        cin >> N;
        ll ans = 0;
        for (int s = 1; s < N; s++)
            ans = (ans + dp[N][s]) % MOD;
        printf("Case #%d: %lld\n", cas + 1, ans);
    }
    return 0;
}
