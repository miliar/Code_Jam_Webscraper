#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))
#define pb push_back

typedef long double ldouble;
typedef pair<int, int> pii;
typedef long long llong;
typedef vector<int> vi;

const int inf = (int)1e9; 
const ldouble eps = 1e-7;

int main()
{
    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    int tests;
    cin >> tests;
    for (int testCase = 1; testCase <= tests; ++testCase)
    {
        int n, l, h;
        cin >> n >> l >> h;
        vector<int> a(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        for (int i = l; i <= h; ++i)
        {
            bool can = true;
            for (int j = 0; j < n; ++j)
                if (i % a[j] && a[j] % i)
                    can = false;
            if (can)
            {
                printf("Case #%d: %d\n", testCase, i);
                break;
            } else
            if (i == h)
                printf("Case #%d: NO\n", testCase);
        }
    }
    return 0;
}

