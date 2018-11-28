#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <algorithm>
using namespace std;
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int _; scanf("%d", &_); _;})
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF 1e8
#define MAX 104
typedef vector<int> VI;

int n, m, mp[MAX][MAX], color[MAX][MAX], dx[] = {-1,0,0,1}, dy[]={0,-1,1,0}, col, match[100002];
#define ok(x,y) (x>=0 && y>=0 && x<n && y<m)


int go(int x, int y) {
    int bestnd = INF, nextstep = -1;
    REP(k,4) if(ok(x+dx[k], y+dy[k])) {
        int nd = mp[x+dx[k]][y+dy[k]], d = mp[x][y];
        if(nd < d && nd < bestnd) nextstep = k, bestnd = nd;
    }
    if(nextstep == -1) {
        if(color[x][y] == -1) color[x][y] = col++;
        return color[x][y];
    }
    return color[x][y] = go(x+dx[nextstep], y+dy[nextstep]);   
}

int main() {
    int testcases = GI;
    FOR(kase,1,testcases+1) {
        n = GI, m = GI;
        REP(i,n) REP(j,m) mp[i][j] = GI, color[i][j] = -1;
        col = 1;
        REP(i,n) REP(j,m) if(color[i][j] == -1) {
            go(i, j);
        }
        col = 0;
        memset(match,-1,sizeof(match));
        REP(i,n) REP(j,m) if(match[color[i][j]] == -1) {
            match[color[i][j]] = col++;            
        }
        printf("Case #%d:\n", kase);
        REP(i,n) {
            REP(j,m) printf("%c ", 'a' + match[color[i][j]]);
            printf("\n");
        }
    }
    





}





			
