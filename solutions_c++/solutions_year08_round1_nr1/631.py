#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

FILE * in=fopen("in1.txt","r");
FILE * out=fopen("out1.txt","w");

int T;

int main() {
    fscanf(in,"%d",&T);
    for( int i=1; i<=T; i++ ) {
        int N;
        fscanf(in,"%d",&N);
        vector<int> a, b;
        int t;
        for( int j=0; j<N; j++ ) {
            fscanf(in,"%d",&t);
            a.push_back(t);
        }
        for( int j=0; j<N; j++ ) {
            fscanf(in,"%d",&t);
            b.push_back(t);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        long long ans=0;
        for( int j=0; j<N; j++ ) ans+=(long long)a[j]*(long long)b[N-j-1];
        fprintf(out,"Case #%d: %ld\n",i,ans);
    }

    return 0;
}
