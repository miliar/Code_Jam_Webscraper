#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int T, H, W;

int A[100][100];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

char B[100][100] = {};

char seq;

char mark(int x, int y) {
    if(B[x][y]) return B[x][y];
    int p = -1, val = A[x][y];
    for(int d = 0; d < 4; ++d) {
        int xx = x + dx[d];
        int yy = y + dy[d];
        if(xx >= 0 && xx < H && yy >= 0 && yy < W && A[xx][yy] < val) {
            p = d;
            val = A[xx][yy]; 
        }
    }
    if(p == -1) {
        return B[x][y] = seq++;
    }
    else {
        return B[x][y] = mark(x+dx[p], y+dy[p]);
    }
}

int main() {
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
  
    scanf("%d", &T);
        
    for(int c = 1; c <= T; ++c) {
        
        scanf("%d%d", &H, &W);
        
        for(int h = 0; h < H; ++h) {
            for(int w = 0; w < W; ++w) {
                scanf("%d", &A[h][w]);
            }
        }
        
        memset(B, 0, sizeof(B));
        seq = 'a';
        for(int h = 0; h < H; ++h) {
            for(int w = 0; w < W; ++w) {
                mark(h, w);
            }
        }
        printf("Case #%d:\n", c);
        for(int h = 0; h < H; ++h) {
            for(int w = 0; w < W; ++w) {
                if(w) putchar(' ');
                cout << B[h][w];
            }
            cout << endl;
        }
    }
    return 0;
}
