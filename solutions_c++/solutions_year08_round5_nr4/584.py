#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <numeric>
using namespace std;

FILE * in=fopen("in4.txt","r");
FILE * out=fopen("out4.txt","w");

int T;
const int dx[2]={-1,-2}, dy[2]={-2,-1};

int main() {
    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        int H,W,R;
        fscanf(in,"%d %d %d",&H,&W,&R);
        long long dp[101][101];
        for( int i=0; i<101; i++ ) for( int j=0; j<101; j++ ) dp[i][j]=0;
        for( int i=0; i<R; i++ ) {
            int r,c;
            fscanf(in,"%d %d",&r,&c);
            dp[r][c] = -1;
        }
        dp[1][1]=1;
        for( int y=1; y<=H; y++ ) {
            for( int x=1; x<=W; x++ ) {
                if( dp[y][x] == -1 ) continue;
                for( int k=0; k<2; k++ ) {
                    if( y+dy[k]>=1 && y+dy[k]<=H && x+dx[k]>=1 && x+dx[k]<=W && dp[y+dy[k]][x+dx[k]]!=-1 ) {
                        dp[y][x] += dp[y+dy[k]][x+dx[k]];
                        dp[y][x]%=10007;
                    }
                }
            }
        }




        fprintf(out,"Case #%d: %I64d\n",test,dp[H][W]);

    }

    return 0;
}
