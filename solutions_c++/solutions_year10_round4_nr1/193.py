#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int ss[400];

class Diamond{
    int k;
    vector <vector <int> > a;
    public:
        Diamond(int K = 0) : k(K)
        {
            REP(i, k)
            {
                a.pb(vector <int> ());
                REP(j, 2 * k - 1)
                    a.back().pb(-1);
                REP(j, i + 1)
                    scanf("%d", &a.back()[k - 1 - i + j * 2]);
            }
            FOR(i, k, 2 * k - 1)
            {
                a.pb(vector <int> ());
                REP(j, 2 * k - 1)
                    a.back().pb(-1);
                REP(j, k - (i - k) - 1)
                    scanf("%d", &a.back()[(i - k + 1) + j * 2]);
            }
        }
        bool symm(int X, int Y)
        {
            int rt = 0;
            REP(i, 2 * k - 1)
                REP(j, 2 * k - 1)
                    if (a[i][j] != -1)
                    {
                        int x = X + (X - i);
                        int y = Y + (Y - j);
                        if (x >= 0 && x < 2 * k - 1)
                            if (a[x][j] != -1 && a[x][j] != a[i][j])
                                return 0;
                        if (y >= 0 && y < 2 * k - 1)
                            if (a[i][y] != -1 && a[i][y] != a[i][j])
                                return 0;
                    }
            return 1;
        }
        int find_max(int x, int y)
        {
            int mx = 0;
            REP(i, 2 * k - 1)
                REP(j, 2 * k - 1)
                    if (a[i][j] != -1)
                        mx = max(mx, abs(x - i) + abs(y - j));
            return mx;
        }
        int minCost()
        {
            int mn = 999999;
            REP(i, 2 * k - 1)
                REP(j, 2 * k - 1)
                    if (symm(i, j))
                    {
                        int t = find_max(i, j) * 2 + 1;
                        mn = min(mn, ss[t] - ss[k * 2 - 1]);
                    }
            return mn;
        }
        void out()
        {
            REP(i, 2 * k - 1)
            {
                REP(j, 2 * k - 1)
                    printf("%2d", a[i][j]);
                printf("\n");
            }
        }
};

int main()
{
    int n;
    scanf("%d", &n);
    ss[1] = 1;
    FOR(i, 3, 400)
        ss[i] = ss[i - 2] + (i / 2) + (i / 2 + 1), i++;
    REP(ii, n)
    {
        int k;
        scanf("%d", &k);
        Diamond d = Diamond(k);
        //d.out();
        printf("Case #%d: %d\n", ii + 1, d.minCost());
    }
    return 0;
}
