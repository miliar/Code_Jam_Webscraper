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
        int n, m;
        scanf("%d %d\n", &n, &m);
        vector< vector<char> > a(n, vector<char>(m));
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
                scanf("%c", &a[i][j]);
            scanf("\n");
        }
        for (int i = 0; i < n - 1; ++i)
            for (int j = 0; j < m - 1; ++j)
            {
                if (a[i][j] == '#' && a[i + 1][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j + 1] == '#')
                {
                    a[i][j] = '/';
                    a[i][j + 1] = '\\';
                    a[i + 1][j] = '\\';
                    a[i + 1][j + 1] = '/';
                }
            }
        bool isBroken = false;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (a[i][j] == '#')
                    isBroken = true;
        printf("Case #%d:\n", testCase);
        if (isBroken)
            puts("Impossible");
        else
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = 0; j < m; ++j)
                    printf("%c", a[i][j]);
                printf("\n");
            }
        }
    }
    return 0;
}

