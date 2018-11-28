#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define TynKogep TOPCODER
#define bublic public:
#define clr(a) memset(a,0,sizeof(a))
#define pb push_back
#define sz size()
#define ld long double
#define ll long long
#define istr istringstream

const ld eps=1e-9;
const ld PI=3.1415926535897932384626433832795;

string s;
string w = "welcome to code jam";
int d[512][32];

int main()
{
    freopen("small.in","rt",stdin);
    freopen("small.out","wt",stdout);
    
    int tcn, n, m = w.sz;
    cin >> tcn;
    getline(cin, s);
    for (int tc = 0; tc < tcn; ++tc)
    {
        getline(cin, s);
        n = s.sz;
        clr(d);
        for (int i = 0; i < n; ++i)
        {
            if (s[i] == w[0]) d[i][0] = 1;
        }
        
        for (int j = 1; j < m; ++j)
        {
            for (int i = 1; i < n; ++i)
            {
                if (s[i] == w[j])
                {
                    for (int k = 0; k < i; ++k)
                    {
                        if (s[k] == w[j - 1])
                            d[i][j] = (d[i][j] + d[k][j - 1]) % 10000;
                    }
                }
            }
        }
        
        int res = 0;
        for (int i = 0; i < n; ++i)
        {
            res = (res + d[i][m - 1]) % 10000;
        }
        printf("Case #%d: %04d\n", tc + 1, res);
    }

    return 0;
}
