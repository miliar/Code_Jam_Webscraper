#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

#define REP(i, n) for((i); (i) < (n); (i)++)
#define gout cout << "Case #" << kase << ": "; cout
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define SCANT scanf("%d", &t);
#define MAX 1040


typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef long int LI;
typedef unsigned long int ULI;

int t, n;
ULI ans;
vector<int> leftie;
vector<int> rightie;
bool hasInter[MAX][MAX];

void solve()
{
    int i = 0;
    REP(i, n)
    {
        int j = 0;
        REP(j, n)
        {
            if(j == i) continue;
            if((leftie[i] < leftie[j] && rightie[i] > rightie[j]) || (leftie[i] > leftie[j] && rightie[i] < rightie[j]))
            {
                //cout << hasInter[i][j] << " " << hasInter[j][i] << endl;
                ans += !hasInter[i][j] ? 1 : 0;
                hasInter[i][j] = true; hasInter[j][i] = true;
                //cout << "Here! " << leftie[i] << " " << leftie[j] << " " << rightie[i] << " " << rightie[j] << " " << endl;
            }
        }
    }
}

int main()
{
    SCANT
    int kase = 1;
    REP(kase, t+1)
    {
        ans = 0;
        leftie.clear(); rightie.clear();
        int m = 0; int g = 0;
        int i = 0;
        scanf("%d",&n);
        REP(m, MAX) {
            REP(g, MAX)
               { hasInter[m][g] = false; }
        }
        REP(i, n) {
            int tl, tr;
            scanf("%d %d", &tl, &tr);
            leftie.pb(tl);
            rightie.pb(tr);
        }
        solve();
        gout << ans << endl;
    }
}
