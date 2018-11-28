#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#define NMAX 105
#define INF 1000000

int a[NMAX][NMAX];
bool used[NMAX][NMAX];
int fx[NMAX][NMAX], fy[NMAX][NMAX];
char ans[NMAX][NMAX];
int n, m;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

void get(int x, int y)
{
    if (fx[x][y] != -1) return;

    int mn = INF;
    int nx = -1, ny = -1;

    forn(i, 4)
    {
        int xx = x + dx[i];
        int yy = y + dy[i];
        if (xx < 0 || yy < 0 || xx >= n || yy >= m) continue;
        if (a[xx][yy] >= a[x][y]) continue;

        if (a[xx][yy] < mn)
        {
            mn = a[xx][yy];
            nx = xx;
            ny = yy;
        }
    }

    if (mn == INF)
    {
        fx[x][y] = x;
        fy[x][y] = y;
        return;
    }

    get(nx, ny);
    fx[x][y] = fx[nx][ny];
    fy[x][y] = fy[nx][ny];
}

void solve(int tc)
{
    printf("Case #%d:\n", tc);

    cin >> n >> m;
    forn(i, n)
    {
        forn(j, m)
        {
            cin >> a[i][j];
        }
    }

    memset(fx, 255, sizeof(fx));
    memset(fy, 255, sizeof(fy));

    forn(i, n)
    {
        forn(j, m)
        {
            get(i, j);
        }
    }

    memset(used, 0, sizeof(used));

    char c = 'a';
    forn(i, n)
    {
        forn(j, m)
        {
            if (used[i][j]) continue;

            forn(i1, n)
            {
                forn(j1, m)
                {
                    if (fx[i1][j1] == fx[i][j] && fy[i1][j1] == fy[i][j])
                    {
                        used[i1][j1] = true;
                        ans[i1][j1] = c;
                    }
                }
            }
            c++;
        }
    }

    forn(i, n)
    {
        forn(j, m)
        {
            if (j) printf(" ");
            printf("%c", ans[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    cin >> tc;
    for1(it, tc)
    {
        solve(it);
    }
    return 0;
}
            
