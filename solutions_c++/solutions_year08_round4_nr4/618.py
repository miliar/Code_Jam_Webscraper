#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <numeric>
using namespace std;

FILE * in=fopen("in3.txt","r");
FILE * out=fopen("out3.txt","w");

int T;

int main() {
    fscanf(in,"%d",&T);
    for( int test=1; test<=T; test++ ) {
        int K;
        string S;
        char buf[10000];
        fscanf(in,"%d",&K);
        fscanf(in,"%s",buf);
        S = buf;
        int perm[10];
        for( int i=0; i<K; i++ ) perm[i]=i;
        int best=INT_MAX;
        do {
            string newS=S;
            for( int i=0; i<S.size()/K; i++ ) {
                for( int j=0; j<K; j++ ) {
                    newS[i*K+j] = S[i*K+perm[j]];
                }
            }
            //cout << newS << " vs " << S << endl;
            int count=0;
            for( int i=0; i<newS.size(); i++ ) {
                int j=i+1;
                while( j<newS.size()&&newS[j]==newS[j-1] ) j++;
                i=j-1;
                count++;
            }
            if(count<best) best=count;

        } while(next_permutation(perm,perm+K));

        fprintf(out,"Case #%d: %d\n",test,best);

    }

    return 0;
}
