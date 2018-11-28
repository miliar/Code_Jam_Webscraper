#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

FILE * in=fopen("in.txt","r");
FILE * out=fopen("out.txt","w");

/*
struct state {
    int sE, curProc, used;
    state( int s, int c, int u ) {
        sE=s; curProc=c; used=u;
    }
    bool operator<( const state & s ) const {
        return used > s.used;
    }
};
*/
const int MAXQ=1501, MAXS=151, INF=(1<<28);
int N;


int main() {
    fscanf(in,"%d",&N);
    for( int i=0; i<N; i++ ) {
        int numProc, numSearch;
        map<string,int> lookUp;
        map<int,string> rev;
        int proc[MAXQ], dp[MAXS][MAXQ];
        fscanf(in,"%d\n",&numSearch);
        for( int j=0; j<numSearch; j++ ) {
            char buf[1000];
            fscanf(in,"%[^\n]\n",buf);
            lookUp[buf]=j;
            rev[j]=buf;
            cout << buf << endl;
        }

        fscanf(in,"%d\n",&numProc);
        for( int j=0; j<numProc; j++ ) {
            char buf[1000];
            fscanf(in,"%[^\n]\n",buf);
            cout << buf << endl;
            proc[j]=lookUp[buf];
            cout << j << " proc is " << proc[j] << endl;
        }

        for( int j=0; j<numSearch; j++ ) dp[j][0]=(proc[0]==j)?INF:0; //base cases

        for( int j=1; j<numProc; j++ ) {
            for( int k=0; k<numSearch; k++ ) {
                dp[k][j]=INF;
                if( proc[j]==k ) continue;
                for( int l=0; l<numSearch; l++ )
                    if(k==l) dp[k][j]=min(dp[k][j], dp[l][j-1]);
                    else dp[k][j]=min(dp[l][j-1]+1, dp[k][j]);
            }
        }
        int ans=INF;
        if( numProc > 0 ) {
            for( int j=0; j<numSearch; j++ ) ans=min(ans,dp[j][numProc-1]);
        }
        else ans=0;

        fprintf(out,"Case #%d: %d\n",i+1,ans);

    }
    return 0;
}








