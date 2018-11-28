#include <iostream>
#include <set>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

int C,N,K,B,T;

int main(){
    cin>>C;
    for(int CC=1;CC<=C;++CC){
        cin>>N>>K>>B>>T;
        vector<int> X(N),V(N),psum(N),able(N);

        for(int i=N-1;i>=0;--i) cin>>X[i];
        for(int i=N-1;i>=0;--i) cin>>V[i];

        int poss=0;
        for(int i=0;i<N;++i) {
            if(ceil((B-X[i])/(double)(V[i]))<=T) able[i]=1; else able[i]=0;
            psum[i]=psum[max(0,i-1)];
            psum[i]+=able[i];
        }
        if(psum[N-1]<K) { cout<<"Case #"<<CC<<": IMPOSSIBLE"<<endl; continue;}

        long long poc=0;
        for(int i=0;i<N;++i) {
            if(able[i]==0 && psum[i]<K){
                poc+=K-psum[i];
            }
        }

        cout<<"Case #"<<CC<<": "<<poc<<endl;
        }
    return 0;
}
