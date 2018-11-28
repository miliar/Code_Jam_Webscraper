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

static void add_one(set<pii> &ones, int p)
{
    set<pii>::iterator it = ones.lower_bound(pii(p, INT_MIN));
    assert(it == ones.end() || it->first > p + 1);
    if (it != ones.begin())
    {
        --it;
        assert(it->second < p);
        if (it->second + 1 == p)
        {
            ones.insert(it, pii(it->first, it->second + 1));
            ones.erase(it);
            return;
        }
    }
    ones.insert(it, pii(p, p));
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        set<pii> ones;
        int N;
        map<int, int> vendors;
        cin >> N;
        for (int i = 0; i < N; i++)
        {
            int P, V;
            cin >> P >> V;
            vendors[P] = V;
        }

        map<int, int>::iterator i;
        i = vendors.begin();
        ll ans = 0;
        while (i != vendors.end())
        {
            int x = i->first;
            while (i->second >= 2)
            {
                ans++;
                vendors[x + 1]++;
                vendors[x] -= 2;
                bool back = false;
                if (!ones.empty())
                {
                    set<pii>::iterator last = ones.end();
                    --last;
                    if (last->second == i->first - 1)
                    {
                        back = true;
                        int left = last->first;
                        int right = last->second;
                        ans += right - left + 1;
                        if (left + 1 <= right)
                            ones.insert(pii(left + 1, right));
                        ones.erase(last);

                        add_one(ones, left - 1);
                        vendors[x]++;
                    }
                }
                if (!back)
                    add_one(ones, x - 1);
            }
            if (i->second == 1)
                add_one(ones, x);
            ++i;
        }

        printf("Case #%d: %lld\n", cas + 1, ans);
    }
    return 0;
}
