#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

FILE * in=fopen("in2.txt","r");
FILE * out=fopen("out2.txt","w");

int T;

int main() {
    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        int N, M, A;
        fscanf(in,"%d %d %d",&N,&M,&A);
        cout << test << endl;

        bool ok=false;
        for( int i=0; i<=N; i++ ) {
            for( int j=0; j<=M; j++ ) {
                for( int k=0; k<=N; k++ ) {
                    for( int l=0; l<=M; l++ ) {
                            if( abs( (k*j - i*l) ) == A ) {
                                fprintf(out,"Case #%d: %d %d %d %d 0 0\n",test,i,j,k,l);
                                ok=true;
                            }
                            if(ok) break;
                       }
                       if(ok) break;
                    }
                    if(ok) break;
                }
                if(ok) break;
            }

        if(!ok) fprintf(out,"Case #%d: IMPOSSIBLE\n",test);
    }


    return 0;
}
