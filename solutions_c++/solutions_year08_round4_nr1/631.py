#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

FILE * in=fopen("in1.txt","r");
FILE * out=fopen("out1.txt","w");

struct node {
    int gate;
    bool change, isLeaf;
    node( int g, bool c, bool il ) { gate=g; change=c; isLeaf=il; }
    node() { gate=-1; }
};

int T;
typedef long long ll;
const int MAXM=10001, INF=100000;

int main() {

    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        int M, V;
        node tree[MAXM];
        int dp[MAXM][2];

        fscanf(in,"%d %d",&M,&V);
        for( int i=1; i<=(M-1)/2; i++ ) {
            int G,C;
            fscanf(in,"%d %d",&G,&C);
            tree[i] = node(G,C,false);
        }
        for( int i=(M-1)/2+1; i<=M; i++ ) {
            int I;
            fscanf(in,"%d",&I);
            tree[i]=node(I,false,true);
        }

        for( int i=0; i<=M; i++ ) dp[i][1] = dp[i][0] = INF;

        for( int i=(M-1)/2+1; i<=M; i++ ) {
            dp[i][tree[i].gate]=0;
            dp[i][!tree[i].gate]=INF;
        }
        for( int i=(M-1)/2; i>=1; i-- ) {
            if( tree[i].gate == 1 ) {

                dp[i][1] = min(dp[i][1],dp[i*2][1] + dp[i*2+1][1]);
                dp[i][0] = min(dp[i*2][0] + dp[i*2+1][1], dp[i*2][1] + dp[i*2+1][0]) ;
                dp[i][0] = min(dp[i][0], dp[i*2][0] + dp[i*2+1][0]);
            }
            else {
                dp[i][1] = min( min(dp[i][1],dp[i*2][1] + dp[i*2+1][1]), dp[i*2][1] + dp[i*2+1][0] );
                dp[i][1] = min( dp[i][1], dp[i*2][0] + dp[i*2+1][1] );
                dp[i][0] = min(dp[i][0],dp[i*2][0] + dp[i*2+1][0]);
            }

            if( tree[i].change ) {
                if( tree[i].gate==1 ) {
                    dp[i][1] = min( min(dp[i][1],dp[i*2][1] + dp[i*2+1][1]+1), 1+dp[i*2][1] + dp[i*2+1][0] );
                    dp[i][1] = min( dp[i][1], 1+dp[i*2][0] + dp[i*2+1][1] );
                    dp[i][0] = min(dp[i][0],1+dp[i*2][0] + dp[i*2+1][0]);
                }
                else {
                    dp[i][1] = min( dp[i][1], dp[i*2][1] + dp[i*2+1][1] + 1 );
                    dp[i][0] = min( min( dp[i][0], dp[i*2][0] + dp[i*2+1][1]+1 ), dp[i*2][1] + dp[i*2+1][0]+1) ;
                    dp[i][0] = min(dp[i][0], dp[i*2][0] + dp[i*2+1][0]+1);
                }
            }

        }


        if( dp[1][V] != INF ) fprintf(out,"Case #%d: %d\n",test,dp[1][V]);
        else fprintf(out,"Case #%d: IMPOSSIBLE\n",test);
    }

    return 0;
}
