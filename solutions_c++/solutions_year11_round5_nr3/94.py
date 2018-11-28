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

static const int dr[4] = {0, 1, 1, 1};
static const int dc[4] = {1, 0, 1, -1};
static const char chars[] = "-|\\/";

#define MOD 1000003

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int R, C;
        cin >> R >> C;
        vector<vi> grid(R, vi(C));
        for (int i = 0; i < R; i++)
        {
            string line;
            cin >> line;
            for (int j = 0; j < C; j++)
            {
                int v = 0;
                while (line[j] != chars[v])
                    v++;
                grid[i][j] = v;
            }
        }

        int N = R * C;
        ll ans = 0;
        for (ll b = 0; b < (1 << N); b++)
        {
            vector<vi> vals(R, vi(C));
            for (int i = 0; i < R; i++)
                for (int j = 0; j < C; j++)
                {
                    int id = i * C + j;
                    bool on = (b & (1 << id));
                    int r = dr[grid[i][j]];
                    int c = dc[grid[i][j]];
                    if (on) r = R - r, c = C - c;
                    r = (r + i) % R;
                    c = (c + j) % C;
                    if (r < 0) r += R;
                    if (c < 0) c += C;
                    vals[r][c]++;
                    if (vals[r][c] > 1)
                        goto bad;
                }
            ans = (ans + 1) % MOD;
bad:;
        }
        printf("Case #%d: %lld\n", cas + 1, ans);
    }
    return 0;
}
