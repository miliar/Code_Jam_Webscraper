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

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int N;
        cin >> N;
        int mini[N];
        for (int i = 0; i < N; i++)
        {
            string line;
            cin >> line;
            int last = N - 1;
            while (last >= 0 && line[last] == '0')
                last--;
            mini[i] = last;
        }

        int shuffle[N];
        for (int i = 0; i < N; i++)
        {
            int j = 0;
            while (mini[j] > i) j++;
            assert(j < N);
            shuffle[i] = j;
            mini[j] = INT_MAX;
        }

        int ans = 0;
        for (int i = 0; i < N; i++)
            for (int j = i + 1; j < N; j++)
                if (shuffle[i] > shuffle[j]) ans++;

        printf("Case #%d: %d\n", cas + 1, ans);
    }
    return 0;
}
