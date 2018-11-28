#include <iostream>
#include <vector>
#include <algorithm>

#define pb push_back
#define LL long long

using namespace std;

vector<int> get_cycle_lengths(const vector<int>& seq) {
	vector<int> ret;
	vector<bool> vis(seq.size(),false);
	for(int i=0;i<seq.size();++i) {
		if(vis[i]) continue;
		int l = 1;
		vis[i] = true;
		int next = seq[i];
		while(!vis[next]) {
			++l;
			vis[next] = true;
			next = seq[next];
		}
		ret.pb(l);
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for(int iter = 0; iter < T; ++iter) {
		int N;
		cin >> N;
		vector<int> n(N);
		for(int i=0;i<N;++i) cin>>n[i];
		for(int i=0;i<N;++i) n[i]--;
		double ans = 0;
		vector<int> c = get_cycle_lengths(n);
		for(int i=0;i<c.size();++i) if(c[i]!=1) ans+=c[i];
		cout<<"Case #"<<iter+1<<": "<<ans<<".000000\n";
	}
}
