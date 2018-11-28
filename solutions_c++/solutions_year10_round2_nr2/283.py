#include <iostream>
using namespace std;

int N, K, B, T;
int X[200], V[200];
bool poss[200];

int cnt(int cix) {
    int res = 0;
    for (int i=cix+1; i<N; i++) {
        if (!poss[i]) res++;
    }
    return res;
}


int main() {
    int C; cin>>C;
    for (int c=1; c<=C; c++) {
        cin>>N>>K>>B>>T;
        for (int i=0; i<N; i++) cin>>X[i];
        for (int i=0; i<N; i++) cin>>V[i];
        
        if (K==0) {
            cout<<"Case #"<<c<<": 0"<<endl;
            continue;
        }
        
        for (int i=0; i<N; i++) {
            poss[i] = X[i] + ((long long)T)*V[i] >= B;
        }
        
        int result = 0x7fffffff;
        if (K==1) {
            for (int c0=0; c0<N; c0++)
                if (poss[c0])
                    result = min(result, cnt(c0));
        }
        else if (K==2) {
            for (int c0=0; c0<N; c0++)
                if (poss[c0])
                    for (int c1=c0+1; c1<N; c1++)
                        if (poss[c1])
                            result = min(result, cnt(c0)+cnt(c1));
        }
        else if (K==3) {
            for (int c0=0; c0<N; c0++)
                if (poss[c0])
                    for (int c1=c0+1; c1<N; c1++)
                        if (poss[c1])
                            for (int c2=c1+1; c2<N; c2++)
                                if (poss[c2])
                                    result = min(result, cnt(c0)+cnt(c1)+cnt(c2));
        }
        
        if (result!=0x7fffffff)
            cout<<"Case #"<<c<<": "<<result<<endl;
        else
            cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
    }
    
    return 0;
}
