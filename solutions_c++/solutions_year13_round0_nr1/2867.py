#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <bitset>
#include <utility>

using namespace std;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define SZ(c) ((int)(c).size())
#define ITER(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FIND(x,c) ((c).find((x))!=(c).end())
#define MP(x,y) make_pair((x),(y))

typedef long long ll;
const int INF=2147483647;
const int MOD=(int)1e9+7;
char a[10][10];
bool isfull() {
    REP(i,4) REP(j,4) if (a[i][j]=='.') return false;
    return true;
}
bool check(char c) {
    REP(i,4) {
        int cnt=0;
        REP(j,4) {
            if (a[i][j]==c || a[i][j]=='T')
                cnt++;
        }
        if (cnt==4) return true;
    }
    REP(j,4) {
        int cnt=0;
        REP(i,4) {
            if (a[i][j]==c || a[i][j]=='T')
                cnt++;
        }
        if (cnt==4) return true;
    }
    int cnt=0;
    REP(i,4) {
        if (a[i][i]==c || a[i][i]=='T')
            cnt++;
    }
    if (cnt==4) return true;
    cnt=0;
    REP(i,4) {
        if (a[i][3-i]==c || a[i][3-i]=='T')
            cnt++;
    }
    if (cnt==4) return true;
    return false;
}

//const int MAX=
int main() {
    int T;
    scanf("%d",&T);
    REP(t,T) {
        REP(i,4) scanf("%s",a[i]);
        printf("Case #%d: ",t+1);
        if (check('O')) puts("O won");
        else if (check('X')) puts("X won");
        else if (isfull()) puts("Draw");
        else puts("Game has not completed");
    }
    return 0;
}
