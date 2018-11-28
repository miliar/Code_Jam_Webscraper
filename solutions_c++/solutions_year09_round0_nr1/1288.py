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

#define clr(a) memset(a,0,sizeof(a))
#define pb push_back
#define sz size()
#define ld long double
#define ll long long
#define istr istringstream

const ld eps=1e-9;
const ld PI=3.1415926535897932384626433832795;

string s[5000];
string ss;


int main()
{
    freopen("small.in","rt",stdin);
    freopen("small.out","wt",stdout);
    
    int l, d, n, res;
    
    cin >> l >> d >> n;
    for (int i = 0; i < d; ++i)
    {
        cin >> s[i];
    }
    
    for (int tc = 0; tc < n; ++tc)
    {
        res = 0;
        cin >> ss;
        for (int i = 0; i < d; ++i)
        {
            int k = 0, b = 1;
            for (int j = 0; j < l; ++j)
            {
                if (ss[k] != '(' && s[i][j] != ss[k])
                {
                    b = 0;
                    break;
                }
                if (ss[k] == '(')
                {
                    k++;
                    int boo = 0;
                    while (ss[k] != ')')
                    {
                        if (ss[k++] == s[i][j]) boo = 1;
                    }
                    if (!boo)
                    {
                        b = 0;
                        break;
                    }
                }
                k++;
            }
            
            if (b) res++;
        }
        cout << "Case #" << tc + 1 << ": " << res << endl;
    }

    return 0;
}
