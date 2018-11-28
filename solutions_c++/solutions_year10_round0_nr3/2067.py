#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		ll r,k,n;
		scanf("%lld%lld%lld", &r, &k, &n);
		vector<ll> que(n);
		ll sum = 0;
		for(int i = 0; i < n; i++) scanf("%lld",&que[i]), sum+=que[i];

		ll leftRides = r, leftSeats = 0;
		ll res = 0;
		int next = 0;
		vector<ll> mleft(n,-1), mres(n,-1);
		while(leftRides > 0){
			if(mleft[next]!=-1){
				ll took = mleft[next]-leftRides, cash = res - mres[next];
				ll fit = leftRides/took;
				leftRides -= fit*took;
				res += fit*cash;
				//printf("Been, done, redo %lld rides\n", fit);
			}
			mleft[next] = leftRides;
			mres[next] = res;
			if(leftRides == 0) break;
			leftSeats = min(k, sum);
			//printf("left %lld", leftSeats);
			while(leftSeats > 0){
				if(leftSeats >= que[next]){
					//printf("take: %d\n", next);
					res += que[next];
					leftSeats -= que[next];
					next = (next+1)%n;
				}
				else leftSeats = 0;
			}
			leftRides--;
			//printf("left: %lld, cash: %lld, next: %d\n", leftRides, res, next);
		}
		printf("Case #%d: %lld\n", cnt, res);
	}
	return 0;
}
