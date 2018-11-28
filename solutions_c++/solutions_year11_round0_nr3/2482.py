#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void result(int t, int res) {
    cout<<"Case #"<<(t+1)<<": ";
    if(res == -1) cout<<"NO"<<endl;
    else cout<<res<<endl;
}

int main() {
	int T;
	cin>>T;
    for(int t = 0; t < T; ++t) {
        int N;
        cin>>N;
        vector<int> V(N);
        int xo = 0;
        for(int n = 0; n < N; ++n) {
        	cin>>V[n];
            xo ^= V[n];
        }
        if(xo != 0) result(t,-1);
        else {
            sort(V.begin(),V.end());
            int sum = 0;
            for(int i = 1; i < (int)V.size(); ++i) sum += V[i];
            result(t,sum);
        }
    }
    return 0;
}
