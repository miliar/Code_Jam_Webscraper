#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
ll M, F;
int N;
const int MN = 204;
typedef pair<ll,ll> P;
P ps[MN];

ll dp[2<<20];

int main() {
	int t;cin>>t;
	for(int a=1; a<=t; ++a) {
		cin>>M>>F>>N;
		for(int i=0; i<N; ++i) {
			ll p,s;cin>>p>>s;
			ps[i] = P(s,p);
		}
again:
		for(int i=0; i<N; ++i) {
			for(int j=0; j<N; ++j) {
				if (i==j) continue;
				P a = ps[i], b = ps[j];
				if (a.first<=b.first && a.second>=b.second) {
					ps[i] = ps[N-1];
					--N;
					goto again;
				}
			}
		}
		sort(ps,ps+N);

		for(int i=0; i<=M; ++i) {
			dp[i]=0;
			int m = i-F;
			if (m<0) continue;
			for(int j=0; j<N; ++j) {
				int last = ps[j].first + 1;
				int prev = j>0 ? ps[j-1].first + 1 : 0;
				int cnt = last - prev;
				int c = ps[j].second;
				bool end=0;
				if (cnt*c > m) {
					cnt = m/c;
					end=1;
				}
				m -= cnt*c;
				dp[i] = max(dp[i], prev+cnt + dp[m]);
//				cout<<"kk "<<i<<' '<<j<<' '<<dp[i]<<' '<<m<<' '<<cnt<<'\n';
				if (end) break;
			}
		}
		cout<<"Case #"<<a<<": "<<dp[M]<<'\n';
	}
}
