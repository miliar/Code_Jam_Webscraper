/* --- Author: Vladimir Smykalov, enot.1.10@gmail.com --- */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define forit(it,v) for(typeof((v).begin()) it = v.begin() ; it != (v).end() ; ++it)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()

using namespace std;

typedef long long ll;
typedef double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;
                                                           
const int inf = (int)1e9;
const ld eps = 1e-9;

/* --- main part --- */

#define TASK "a"

const int dx[] = {1, 0, 1, 1};
const int dy[] = {0, 1, 1, -1};

char s[5][5];
int n = 4;

inline bool in(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < n;
}
bool win(char c)
{
    forn(x, n) forn(y, n)
    {
        forn(k, 4)
        {
            bool ok = true;
            forn(l, 4)
            {
                int x2 = x + dx[k] * l;
                int y2 = y + dy[k] * l;
                if(!in(x2, y2)) ok = false;
                if(s[x2][y2] != c && s[x2][y2] != 'T') ok = false;
                if(!ok) break;
            }
            if(ok) return true;
        }
    }
    return false;
}
int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(_, tn)
    {           
        printf("Case #%d: ", _ + 1);
        forn(i, n) scanf("%s", s[i]);
        if(win('X'))
        {
            printf("X won\n");
            continue;
        }
        if(win('O'))
        {
            printf("O won\n");
            continue;
        }
        bool ok = true;
        forn(i, n) forn(j, n) if(s[i][j] == '.') ok = false;
        if(ok) printf("Draw\n");
        else printf("Game has not completed\n");
    }             
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 