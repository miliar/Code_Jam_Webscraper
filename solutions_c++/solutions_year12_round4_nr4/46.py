
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;
#define maxn 13
int h, w;
bool t[maxn][maxn];
pair<int, int>gdzie[22];
set<vector<int> > bylo;
bool G[1000][maxn][maxn];
int move[1000];
bool dp[maxn][maxn];
bool isin(int x, int y) { return x >= 1 && x <= h && y >= 1 && y <= w; }

int dx[] = {-1, 0, 0};
int dy[] = {0, 1, -1};

int dx2[] = {+1, 0, 0};
int dy2[] = {0, 1, -1};

void go(int x, int y) {
    dp[x][y] = 1;
    fup(k, 0, 2) {
        int xx, yy;
        xx = x + dx[k];
        yy = y + dy[k];
        if (isin(xx, yy) && !dp[xx][yy] && !t[xx][yy]) {
            go(xx, yy);
        }
    }
}


bool brut(int lev) {
    vector<int> x;
    fup(i, 1, h) fup(j, 1, w) x.PB(G[lev][i][j]);
    if (bylo.find(x) != bylo.end()) return false;
    bylo.insert(x);

    int sum = 0;
    fup(i, 1, h) fup(j, 1, w) sum += G[lev][i][j];
    if (sum == 1) {
        /*
        cout << "TAK " << lev << endl;
        fup(i, 1, h) {
            fup(j, 1, w) cout << G[lev][i][j] << " ";
            cout << endl;
        }*/

        return true;
    }

    fup(k, 0, 2) {
        CLR(G[lev + 1]);
        bool ok = true;
        fup(i, 1, h) fup(j, 1, w) {
            int ii, jj;
            ii = i + dx2[k];
            jj = j + dy2[k];
            if (G[lev][i][j]) {
                if (t[ii][jj]) G[lev + 1][i][j] = 1;
                else {
                    if (!dp[ii][jj]) { ok = false; break; }
                    else G[lev + 1][ii][jj] = 1;
                }
            }
        }
        if (ok) {
            move[lev] = k;
            if (brut(lev + 1)) return true;
        }
    }    
    return false;
}

pair<int, int> doit(int x, int y) {
    CLR(dp);
    bylo.clear();
    //cout << "TT " << x << " " << y << endl;
    go(x, y);
    fup(i, 1, h) fup(j, 1, w) G[0][i][j] = dp[i][j];
    int sum = 0;
    fup(i, 1, h) fup(j, 1, w) sum += dp[i][j];
   /* 
    fup(i, 1, h) {
        fup(j, 1, w) cout << dp[i][j] << " ";
        cout << endl;
    }*/
    bool ok = brut(0);
    return MP(sum, ok);
}
int cas;
int main() {
    cin >> cas;
    fup(c, 1, cas) {
        printf("Case #%d:\n", c);
    cin >> h >> w;
    int sum = 0;
    CLR(t);
    fup(i, 1, h) fup(j, 1, w) { 
        char co; cin >> co; if (co == '.') t[i][j] = 0; else if (co == '#') t[i][j] = 1; else {
            //cout << "TAK " << co << " " << i << " " << j << endl;
            gdzie[co - '0'] = MP(i, j);
            ++sum;
        }
    }

    fup(i, 0, sum - 1) {
        pair<int, int> x = doit(gdzie[i].first, gdzie[i].second);
        if (x.second) printf("%d: %d Lucky\n", i, x.first);
        else printf("%d: %d Unlucky\n", i, x.first);;
    }
    }
    return 0;
}

