#include <string>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <set>
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

struct sculpt
{
    int N;
    vector<vector<int> > edges;
    vector<int> parent;
};

static int N;
static bool transit[101][101];
static int back[101];
static bool done[101];

static bool augment(int x)
{
    if (x == -1)
        return true;
    else if (done[x])
        return false;
    done[x] = true;
    for (int i = 0; i < N; i++)
        if (transit[x][i])
        {
            int old = back[i];
            back[i] = x;
            if (augment(old))
                return true;
            back[i] = old;
        }
    return false;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int K;
        cin >> N >> K;
        vector<vi> stocks(N);
        for (int i = 0; i < N; i++)
        {
            stocks[i].resize(K);
            for (int j = 0; j < K; j++)
                cin >> stocks[i][j];
        }

        memset(transit, 0, sizeof(transit));
        fill(back, back + N, -1);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
            {
                bool good = true;
                for (int k = 0; k < K; k++)
                    if (stocks[i][k] >= stocks[j][k])
                    {
                        good = false;
                        break;
                    }
                if (good)
                    transit[i][j] = true;
            }

        int ans = N;
        for (int i = 0; i < N; i++)
        {
            memset(done, 0, sizeof(done));
            if (augment(i))
                ans--;
        }

        printf("Case #%d: %d\n", cas + 1, ans);
    }
    return 0;
}
