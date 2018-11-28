#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

FILE * in=fopen("in1.txt","r");
FILE * out=fopen("out1.txt","w");

int T;
typedef long long ll;
int main() {

    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        int P, K, L;
        int avail[1001], freq[1001];
        fscanf(in,"%d %d %d",&P,&K,&L);
        //for( int i=0; i<K; i++ ) avail[i]=P;
        for( int i=0; i<L; i++ ) fscanf(in,"%d",&freq[i]);
        sort( freq, freq+L );
        reverse( freq, freq+L );
        ll ans=0;
        for( int i=0; i<L; i++ ) {
            ll mult=(i/K+1);
            ans+=mult*(long long)freq[i];
        }
        fprintf(out,"Case #%d: %I64d\n",test,ans);

    }

    return 0;
}
