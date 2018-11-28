

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

const int MX = 1002;
long long A[MX];
long long cnt[MX];
long long speed[MX];
const long long MOD = 1000000007;

int main()
{
	int N;
	cin>>N;
	for(int _t=1;_t<=N;++_t)
	{
		int n,m;
		long long X,Y,Z;
		cin>>n>>m>>X>>Y>>Z;
		for(int i=0;i<m;++i)
			cin>>A[i];

		for(int i=0;i<n;++i){
			speed[i+1] = A[i%m];
			A[i%m] = (X*A[i%m]+Y*(i+1)) % Z;
		}

		memset(cnt,0,sizeof cnt);
		speed[0] = numeric_limits<int>::min();

		for(int i=1;i<=n;++i){
			cnt[i] = 1;
			for(int j=1;j<i;++j){
				if( speed[j] < speed[i] ){
					cnt[i] += cnt[j];
					cnt[i] %= MOD;
				}
			}
		}
		long long ans = 0;
		for(int i=1;i<=n;++i){
			ans += cnt[i];
			ans %= MOD;
		}
		cout<<"Case #"<<_t<<": "<<ans<<endl;
	}
}