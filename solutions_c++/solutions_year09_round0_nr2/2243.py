#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <map>
#include <sstream>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define LET(a,x) typeof(x) a(x)
#define FOR(x,a,b) for(LET(x,a);x!=b;x++)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,v.begin(),v.end())
#define DBG(x) cerr << #x << "-->"<<x<<"; "
#define DBE(x) cerr << #x << "-->"<<x<<";\n"
#define sz size()
#define pb push_back
#define SET0(a) memset(a,0,sizeof(a))

const int INF = (int)1e9;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define GI ({int t; scanf(" %d",&t); t;})

int d[200][200], H, W;
int dest[200][200];
char labels[200][200];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

#define OK(x,y) (0<=x and x<H and 0<=y and y<W)

int lookfor(int x, int y) {
    int v = d[x][y], m = -1;
    REP(i,4) 
	if(OK(x+dx[i], y+dy[i]) and d[x+dx[i]][y+dy[i]] < v) {
	    v = d[x+dx[i]][y+dy[i]];
	    m = i;
	}
    if (m == -1) return x*W + y;
    if (dest[x+dx[m]][y+dy[m]] == -1)
	return dest[x+dx[m]][y+dy[m]] = lookfor(x+dx[m], y+dy[m]);
    return dest[x+dx[m]][y+dy[m]];
}

int labelthis(int x, int y, char c) {
    //cerr << "c: " << c << endl;
    REP(i,H) REP(j,W) if(dest[x][y] == dest[i][j])
	labels[i][j] = c;
}


int main() {
    int T = GI;
    REP(kase, T) {
	memset(dest, -1, sizeof(dest)); 
	SET0(labels);
	H = GI, W = GI;
	REP(i, H) REP(j, W)
	    d[i][j] = GI;
	REP(i,H) REP(j,W) {
	    if (dest[i][j] != -1) continue;
	    dest[i][j] = lookfor(i,j);
	}
	char c = 'a';
	REP(i,H) REP(j,W) {
	    if (labels[i][j] != 0) continue;
	    labelthis(i,j, c);
	    c++;
	}
	cout << "Case #" << kase+1 << ":\n";
	REP(i,H) {
	    REP(j,W) cout << labels[i][j] << " ";
	    cout << endl;
	}
    }
    return 0;
}
