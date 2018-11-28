#pragma comment(linker, "/STACK:1024000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

#define NMAX 55

int dx[6] = {0, 1, 1, 0, -1, -1};
int dy[6] = {1, 1, 0, -1, -1, 0};

bool matr[2 * NMAX][2 * NMAX];
bool used[2 * NMAX][2 * NMAX];

int empty = 0;
int alls = 0;
int s;

bool valid(int x, int y)
{
    return x >= 1 && x <= 2 * s - 1 && 
    ((x <= s && y >= 1 && y <= x + s - 1) ||
    (x > s && y >= x - s + 1 && y <= 2 * s - 1));
}

void dfs(int x, int y)
{
    if (empty == alls) return;
    if (used[x][y] || matr[x][y] == 1) return;

    used[x][y] = true; 
    empty++;

    forn(i, 6)
    {
        if (valid(x + dx[i], y + dy[i])) dfs(x + dx[i], y + dy[i]);
    }
}

bool ring(int t, vector<pii>& moves)
{
    forn(i, t + 1)
    {
        matr[moves[i].first][moves[i].second] = 1;        
    }    
    memset(used, 0, sizeof(used));

    empty = 0;
    alls = 3 * s * s - 3 * s + 1 - t - 1;
    for1(x, s)
    {
        dfs(1, x);
        dfs(x, 1);
    }
    for1(x, s - 1)
    {
        dfs(x + s, x + 1);
        dfs(x + 1, x + s);
        dfs(2 * s - 1, s + x);
        dfs(s + x, 2 * s - 1);
    }

    forn(i, t + 1)
    {
        matr[moves[i].first][moves[i].second] = 0;        
    }

  //  cerr << "ring\n";
    return empty < alls;
}

void dfs2(int x, int y)
{
    if (used[x][y] || matr[x][y] == 0) return;
    used[x][y] = true;
    forn(i, 6)
    {
        if (valid(x + dx[i], y + dy[i])) dfs2(x + dx[i], y + dy[i]);        
    }
}

bool bridge(int t, vector<pii>& moves)
{
    forn(i, t + 1)
    {
        matr[moves[i].first][moves[i].second] = 1;        
        used[moves[i].first][moves[i].second] = 0; 
    }    

    vector<pii> cent;
    cent.pb(mp(1, 1));
    cent.pb(mp(1, s));
    cent.pb(mp(s, 1));
    cent.pb(mp(2 * s - 1, s));
    cent.pb(mp(s, 2 * s - 1));
    cent.pb(mp(2 * s - 1, 2 * s - 1));

    bool ok = false;
   forv(i, cent)
   {
       dfs2(cent[i].first, cent[i].second);
       int usc = 0;
       for (int j = i + 1; j < 6; j++)
       {
        if (matr[cent[j].first][cent[j].second] == 1 && used[cent[j].first][cent[j].second]) usc++;
       }
       if (usc > 0)
       {
        ok = true;
        break;
       }
   } 

    forn(i, t + 1)
    {
        matr[moves[i].first][moves[i].second] = 0;        
    }

    return ok;
}

int get_mask(int x, int y)
{
    if (x == 1)
    {
        if (y > 1 && y < s) return 1;
        else return 0;
    }

    if (y == 1)
    {   if (x > 1 && x < s) return 2;
        else return 0;
    }

    if (x == 2 * s - 1)
    {
        if (y > s && y < 2 * s - 1) return 4;
        else return 0;        
    }

    if (y == 2 * s - 1)
    {
        if (x > s && x < 2 * s - 1) return 8;
        else return 0;
    }

    if (y - x == s - 1)
    {
        return 16;
    }

    if (x - y == s - 1)
    {
        return 32;
    }
    return 0;

}
int dfs3(int x, int y)
{
    if (used[x][y] || matr[x][y] == 0) return 0;
    used[x][y] = true;
    int mask = get_mask(x, y);

    forn(i, 6)
    {
        if (valid(x + dx[i], y + dy[i])) 
        {
            mask |= dfs3(x + dx[i], y + dy[i]);        
        }
    }
    return mask;
}

bool good(int mask)
{
    int cnt = 0;
    forn(i, 6)
    {
        if (mask & (1 << i)) cnt++;
    }
    return cnt >= 3;
}



bool fork(int t, vector<pii>& moves)
{
    forn(i, t + 1)
    {
        matr[moves[i].first][moves[i].second] = 1;        
        used[moves[i].first][moves[i].second] = 0; 
    }


    bool ok = false;
    for (int x = 2; x < s; x++)
    {
        if (ok) break;
        if (good(dfs3(1, x))) ok = true;
        if (good(dfs3(x, 1))) ok = true;
    }
    for (int x = 1; x < s - 1; x++)
    {
        if (ok) break;
        if (good(dfs3(x + s, x + 1))) ok = true;
        if (good(dfs3(x + 1, x + s))) ok = true;
        if (good(dfs3(2 * s - 1, s + x))) ok = true;
        if (good(dfs3(s + x, 2 * s - 1))) ok = true;
    }

    forn(i, t + 1)
    {
        matr[moves[i].first][moves[i].second] = 0;
    } 

    return ok;
}

int a[2 * NMAX][2 * NMAX];
void solve(int test)
{
    printf("Case #%d: ", test);

    cerr << test << endl;
    int m;
    scanf("%d %d", &s, &m);
    vector<pii> moves(m);
    forn(i, m)
    {
        scanf("%d %d", &moves[i].first, &moves[i].second);        
    }
  
    
    memset(a, 0, sizeof(a));
    forn(i, m)
    {
        a[moves[i].first][moves[i].second] = 1;
    }    

/*    cout << endl;
    for1(x, s)
    {
        for1(y, x + s)
        {
            cout << a[x][y] << " ";
        } 
        cout << endl;
    }
    for (int x = s + 1; x <= 2 * s - 1; x++)
    {
        for (int y = x - s + 1; y <= 2 * s - 1; y++)
        {
            cout << a[x][y] << " ";
        }
        cout << endl;
    }
    cout << endl;
  */

    int L = 0, R = m - 1;

  /*  while (R - L > 1)
    {
        int mid = (L + R) / 2;
//        cerr << mid << endl;
        if (ring(mid, moves) || bridge(mid, moves) || fork(mid, moves))
        {
            R = mid;
        }
        else
        {
            L = mid + 1;
        }
    }
    */
    int rng = m + 1;
    int br = m + 1;
    int fk = m + 1;

    
    for (int i = L; i <= R; i++)
    {
        if (bridge(i, moves))
        {
            br = i + 1;            
        }
        if (ring(i, moves)) 
        {
            rng = i + 1;            
        }               
        if (fork(i, moves))
        {
            fk = i + 1;
        }

        if (br < m + 1 || fk < m + 1|| rng < m + 1) break;
    }

    
    int ans = min(br, min(rng, fk));

    if (ans == m + 1)
    {
        cout << "none\n";
        return;
    }

    string str = "";
    if (br == ans) str += "bridge";
    if (fk == ans)
    {
        if (str != "") str += '-';
        str += "fork";
    }
    if (rng == ans)
    {
        if (str != "") str += "-";
        str += "ring";
    }

    cout << str << " in move " << ans << endl;
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}