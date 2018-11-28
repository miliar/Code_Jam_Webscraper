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


int a[128][128];
int b[128][128];
char c[128][128];
int ch;
int z, n, m;

int dfs(int i, int j)
{
    if (b[i][j]) return b[i][j];
    int ii = i, jj = j;
    if (i && a[i - 1][j] < a[ii][jj])
    {
        ii = i - 1;
        jj = j;
    }
    if (j && a[i][j - 1] < a[ii][jj])
    {
        ii = i;
        jj = j - 1;
    }
    if (j + 1 < m && a[i][j + 1] < a[ii][jj])
    {
        ii = i;
        jj = j + 1;
    }
    if (i + 1 < n && a[i + 1][j] < a[ii][jj])
    {
        ii = i + 1;
        jj = j;
    }
    if (ii == i && jj == j)
        b[i][j] = z++;
    else
        b[i][j] = dfs(ii, jj);
    return b[i][j];
}

void mark(int i, int j, char col)
{
    c[i][j] = col;
    if (i && c[i - 1][j] == ' ' && b[i - 1][j] == b[i][j])
        mark(i - 1, j, col);
    if (i + 1 < n && c[i + 1][j] == ' ' && b[i + 1][j] == b[i][j])
        mark(i + 1, j, col);
    if (j && c[i][j - 1] == ' ' && b[i][j - 1] == b[i][j])
        mark(i, j - 1, col);
    if (j + 1 < m && c[i][j + 1] == ' ' && b[i][j + 1] == b[i][j])
        mark(i, j + 1, col);
}

int main()
{
    freopen("small.in","rt",stdin);
    freopen("small.out","wt",stdout);
    
    int tcn;
    cin >> tcn;
    for (int tc = 0; tc < tcn; ++tc)
    {
        clr(b);
        cin >> n >> m;
        ch = 'a';
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                cin >> a[i][j];
            }
        }
        z = 1;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                c[i][j] = ' ';
                if (!b[i][j]) dfs(i, j);
            }
        }
        
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (c[i][j] == ' ') mark(i, j, ch++);
            }
        }
    
        cout << "Case #" << tc + 1 << ":" << endl;
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < m; ++j)
            {
                if (j) cout << " ";
                cout << c[i][j];
            }
            cout << endl;
        }
    }

    return 0;
}
