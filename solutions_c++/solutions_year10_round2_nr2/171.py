#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int T;
	cin>>T;
	for(int Case = 1; Case <= T; ++Case) {
        int N,K,B,T;
        cin>>N>>K>>B>>T;
        vector<int> X(N);
        for(int i = 0; i < X.size(); ++i) cin>>X[i];
        vector<int> V(N);
        for(int i = 0; i < V.size(); ++i) cin>>V[i];

        vector<bool> WRG(N);

        for(int i = 0; i < N; ++i) {
            if(double(B - X[i]) / V[i] <= T) WRG[i] = true;
            else WRG[i] = false;
        }

        /*
        for(int i = 0; i < N; ++i) cout<<WRG[i]<<" ";
        cout<<endl;
        */

        int ctg = 0; // chicks to goal
        int swpc = 0; // swap counter
        int wnrgc = 0; // will not reach goal counter

        for(int i = N - 1; i >= 0; --i) {
            if(ctg >= K) break;
            if(WRG[i]) {
                ++ctg;
                swpc += wnrgc;
            } else {
                ++wnrgc;
            }
        }

        //cout<<ctg<<" "<<swpc<<" "<<wnrgc<<endl;

        if(ctg < K) {
            printf("Case #%d: IMPOSSIBLE\n",Case);
        } else {
            printf("Case #%d: %d\n",Case,swpc);
        }
    }
    return 0;
}
