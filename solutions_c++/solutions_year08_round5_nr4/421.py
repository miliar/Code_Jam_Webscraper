// GCJ '08 R3
// Question D
// Solution by sql_lall
#include <map>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int ways[1001][1001];

int solve(){
    int H, W, R;
    scanf("%d %d %d", &H, &W, &R);
    //if( (W - 1 + H - 1) % 3) return 0;
    for(int i = 0; i < H; i++) for(int j = 0; j < W; j++) ways[i][j] = 0;
    for(int i = 0; i < R; i++){
        int r, c; scanf("%d %d", &r, &c); 
        ways[r-1][c-1] = -1;
    }
    for(int i = H - 1; i >= 0; i--)
        for(int j = W - 1; j >= 0; j--){
            if(i == H - 1 && j == W - 1){ ways[i][j] = 1; continue; }
            int &w = ways[i][j];
            if(w == -1) continue;
            int p1 = -1, p2 = -1;
            if(i + 2 < H && j + 1 < W) p1 = ways[i+2][j+1];
            if(i + 1 < H && j + 2 < W) p2 = ways[i+1][j+2];
            if(p1 == -1 && p2 == -1){ w = -1; continue; }
            if(p1 == -1) {w = p2; continue; }
            if(p2 == -1) {w = p1; continue; }
            w = (p1 + p2) % 10007;
        }
    return ways[0][0] == -1 ? 0 : ways[0][0];
}

int main(){
    int nCases; scanf("%d", &nCases);
    for(int c = 1; c <= nCases; c++)
        printf("Case #%d: %d\n", c, solve());
}
