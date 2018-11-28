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
typedef vector<ll> vll;

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

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        ll R, K, N;
        ll T, ans;
        cin >> R >> K >> N;
        vll G(N);
        for (int i = 0; i < N; i++)
            cin >> G[i];
        T = accumulate(RA(G), 0LL);

        if (T <= K)
            ans = R * T;
        else
        {
            vi next(N);
            vll score(N);
            for (int i = 0; i < N; i++)
            {
                int k = K;
                int j = i;
                while (k >= G[j])
                {
                    k -= G[j];
                    if (++j == N) j = 0;
                }
                score[i] = K - k;
                next[i] = j;
            }

            int cur = 0;
            ans = 0;
            while (R > 0)
            {
                if (R & 1)
                {
                    ans += score[cur];
                    cur = next[cur];
                }
                vi next2(N);
                vll score2(N);
                for (int i = 0; i < N; i++)
                {
                    next2[i] = next[next[i]];
                    score2[i] = score[i] + score[next[i]];
                }
                next2.swap(next);
                score2.swap(score);
                R >>= 1;
            }
        }

        printf("Case #%d: %lld\n", cas + 1, ans);
    }
    return 0;
}
