#include <cmath>
using namespace std;
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>

//By chyx111
typedef long long ll;
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)

const int MAXN = 2048;
int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		int R, K, n;
		scanf("%d%d%d", &K, &R, &n);
		int arr[n*2];
		Rep(i,n)scanf("%d", arr+i);
			
		Rep(i,n)arr[i+n] = arr[i];

		int dp[MAXN];
		ll sum[MAXN];
		int t;

		Rep(i,n){
			dp[i] = i;
			sum[i] = 0;
			for (int j = i; ; j++) {
				if( j < i + n && sum[i] + arr[j] <= R ){
					sum[i] += arr[j];
				}else{
					dp[i] = j % n;
					break;
				}
			}
		}

		ll gain[MAXN];
		memset(gain, 0, (sizeof gain) );

		int pnt[MAXN];
		memset(pnt,-1,(sizeof pnt));

		int cur = 0;
		ll ans;
		gain[0] = 0;
		for(int i = 1; i <= K; ++i){
			gain[i] = gain[i-1] + sum[cur];
			if( pnt[cur] != -1 ){
				int p = pnt[cur];
				int period = i - p;
				ans = (gain[i] - gain[p]) * ((K-p) / period) + gain[ p + (K-p) % period ];
				break;
			}

			pnt[ cur ] = i;
			cur = dp[cur];
			ans = gain[i];
		}

		printf("Case #%d: %lld\n", ica+1, ans);
	}
	return 0;
}

