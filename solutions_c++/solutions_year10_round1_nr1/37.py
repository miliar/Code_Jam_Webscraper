#include <iostream>
using namespace std;
char grid[60][60];
int N,K;
int delta[4][2] = {{1,0},{1,1},{1,-1},{0,1}};
bool yes(char c) {
    for (int i=0; i<N; i++)
    for (int j=0; j<N; j++)
    for (int k=0; k<4; k++) {
        bool ok = true;
        int ti = i;
        int tj = j;
        for (int l=0; l<K; l++) {
            if (ti<0 || tj<0 || ti>=N || tj>=N || grid[ti][tj]!=c) {
                ok = false;
                break;
            }
            ti += delta[k][0];
            tj += delta[k][1];
        }
        if (ok) return true;
    }
    return false;
}
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        scanf("%d %d",&N,&K);
        for (int i=0; i<N; i++) {
            scanf("%s",grid[i]);
        }
        for (int i=0; i<N; i++) {
            // move row i to the right
            int cur = N-1;
            for (int j=N-1; j>=0; j--) {
                if (grid[i][j]!='.') {
                    grid[i][cur--]=grid[i][j];
                }
            }
            while (cur>=0) grid[i][cur--]='.';
        }
        bool red = yes('R');
        bool blue = yes('B');
        if (red && blue) printf("Both\n");
        else if (red) printf("Red\n");
        else if (blue) printf("Blue\n");
        else printf("Neither\n");
    }
}
