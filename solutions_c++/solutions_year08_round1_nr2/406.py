#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

FILE * in=fopen("in2.txt","r");
FILE * out=fopen("out2.txt","w");

int C;

int main() {
    fscanf(in,"%d",&C);
    for( int test=1; test<=C; test++ ) {
        int N, M;
        fscanf(in,"%d",&N);
        fscanf(in,"%d",&M);
        vector< pair<int,int> > sat[M+1];

        for( int i=0; i<M; i++ ) {
            int T;
            fscanf(in,"%d",&T);
            for( int j=0; j<T; j++ ) {
                int n, malt;
                fscanf(in,"%d %d",&n,&malt);
                sat[i].push_back( make_pair(n,malt) );
            }
        }

        int bestM = INT_MAX, found=-1;
        for( int bm=0; bm<(1<<N); bm++ ) {
            bool gOk=true;
            int malted=0;
            for( int i=0; i<N; i++ ) if( ((1<<i)&bm) != 0 ) malted++;

            for( int i=0; i<M; i++ ) {
                bool ok=false;
                for( int j=0; j<sat[i].size(); j++ ) {
                    if( ((bm&(1<<(sat[i][j].first-1))) != 0 && sat[i][j].second==1) ||
                        ((bm&(1<<(sat[i][j].first-1))) == 0 && sat[i][j].second==0)
                     ) {
                        ok=true;
                        break;
                    }
                }
                if(!ok) { gOk=false; break; }
            }
            if(gOk) {
                if( malted < bestM ) {
                    bestM=malted;
                    found=bm;
                }
            }
        }
        if( found == -1 ) {
            fprintf(out,"Case #%d: IMPOSSIBLE\n",test);
        }
        else {
            fprintf(out,"Case #%d: ",test);
            for( int i=0; i<N; i++ ) fprintf(out,(i==N-1)?"%d\n":"%d ",((found&(1<<i))!=0)?1:0);
        }
    }
    return 0;
}




