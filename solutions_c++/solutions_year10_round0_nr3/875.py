#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;
typedef long long ll;

void solve(int ind, int R, int k, int N, vector<int> vec) {
	vector<ll> cash(N);
	vector<int> forw(N);
	for(int i = 0; i < N; ++i) {
		ll coll = 0;
		int cc = 0;
        while(cc < N) {
        	int val = vec[(cc + i) % N];
            if(coll + val <= k) {
            	coll += val;
                ++cc;
            } else break;
        }
        forw[i] = cc;
        cash[i] = coll;
    }

    //for(int i = 0; i < forw.size(); ++i) cout<<forw[i]<<endl;
    
    ll count = 0;
    int si = 0;
    for(int i = 0; i < R; ++i) {
        count += cash[si];
        si = si + forw[si];
        si %= N;
    }

    cout<<"Case #"<<ind<<": "<<count<<endl;
}

int main() {
	int C;
	cin>>C;
	for(int i = 1; i <= C; ++i) {
        int R,k,N;
        cin>>R>>k>>N;
        vector<int> vec(N);
        for(int j = 0; j < N; ++j) {
            cin>>vec[j]; 
        }
        solve(i,R,k,N,vec);
    }
    return 0;
}
