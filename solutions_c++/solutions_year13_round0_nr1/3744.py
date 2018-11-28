#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for (int i=0; i<(n); ++i)
#define TR(i,x) for(typeof(x.begin()) i=x.begin(); i!=x.end(); ++i)
#define ALL(x) x.begin(), x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x, 0, sizeof(x))
#define FIIL(x,c) memset(x, c, sizeof(x))

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

char g[10][10];

bool check(char c) {
    int cnt;
    REP(i,4) {
        cnt=0;
        REP(j,4) if (g[i][j]==c || g[i][j]=='T') ++cnt;
        if (cnt==4) return true;
    }
    REP(i,4) {
        cnt=0;
        REP(j,4) if (g[j][i]==c || g[j][i]=='T') ++cnt;
        if (cnt==4) return true;
    }
    cnt=0;
    REP(i,4) {
        if (g[i][i]==c || g[i][i]=='T') ++cnt;
    }
    if (cnt==4) return true;
    cnt=0;
    REP(i,4) {
        if (g[i][3-i]==c || g[i][3-i]=='T') ++cnt;
    }
    if (cnt==4) return true;
}

int main() {
    int cas;
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin>>cas;
    for (int T=1; T<=cas; ++T) {
        bool flag=false;
        REP(i,4) {
            scanf("%s", g[i]);
            REP(j,4) if (g[i][j]=='.') flag=true;
        }
        printf("Case #%d: ", T);
        if (check('X')) puts("X won");
        else if (check('O')) puts("O won");
        else if (flag) puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}
