#include <vector>
#include <iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<queue>
#include <set>
#include<map>
#include<string>
#include<stdexcept>
#include<errno.h>

using namespace std;
template <class T> void show(T a, int n) { for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl; }
template <class T> void show(T a, int r, int l) { for (int i = 0; i < r; ++i) show(a[i], l); cout << endl; }
#define max(a, b) (a > b?a:b)
#define min(a, b) (a < b?a:b)

#define ms(a, v)    memset(a, v, sizeof(a))
#define pb push_back
#define mp make_pair
#define pii pair<int, int>

typedef long long LL;

const int N = 128 * 2;
const int M = 5000;
const int oo = 10000 * 10000 * 10;

const int n = 4;
char g[111][111];

bool win(char c)
{
    int i, j;
    for (i = 0; i < n;++i)
    {
        for (j = 0;j < n;++j)
            if (g[i][j] != c && g[i][j] != 'T')
                break;
        if (j == n)
            return true;
    }
    for (j = 0;j < n;++j)
    {
        for (i = 0; i < n;++i)
            if (g[i][j] != c && g[i][j] != 'T')
                break;
        if (i == n)
            return true;
    }

    for (i = 0; i < n;++i)
    {
        if (g[i][i] != c && g[i][i] != 'T')
            break;
    }
    if ( i == n)
        return true;

    for (i = 0; i < n;++i)
    {
        if (g[i][n - i - 1] != c && g[i][n - i - 1] != 'T')
            break;
    }
    if ( i == n)
        return true;

    return false;
}

bool draw()
{
    for (int i = 0; i < n;++i)
    {
        for (int j = 0;j < n;++j)
            if (g[i][j] == '.')
                return false;
    }
    return true;
}


int main()
{
        freopen("in", "r", stdin);
        freopen("out1","w",stdout); 
    int i, j, cas = 0;
    scanf("%d", &cas);
    for (int cc = 0; cc < cas;++cc)
    {
        for (int i = 0; i < n;++i)
            scanf("%s", g[i]);

        
        printf("Case #%d: ", cc + 1);
        if (win('X'))
            printf("X won\n");
        else if (win('O'))
            printf("O won\n");
        else if (draw())
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}

