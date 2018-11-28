#include <cstdio>
#include <queue>
#include <cstring>
#include <map>
using namespace std;

int main() {
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;++t) {
		int R, K, N;
		scanf("%d%d%d",&R,&K,&N);
		queue<pair<int,int> > q;
		for(int n=0;n<N;++n) {
			int g;
			scanf("%d",&g);
			q.push(make_pair(g,n));
		}
		int lastvisit[1010];
		long long lastprofit[1010];
		memset(lastvisit, 255, sizeof(lastvisit));
		memset(lastprofit, 255, sizeof(lastprofit));
		long long profit = 0;
		int r = 0;
		for(;r<R;++r) {
			if(lastvisit[q.front().second]>=0) break;
			lastvisit[q.front().second] = r;
			lastprofit[q.front().second] = profit;
			int k=K;
			for(int n=0;n<N && q.front().first<=k;++n) {
				k-=q.front().first;
				q.push(q.front());
				q.pop();
			}
			profit += K-k;
		}
		if(r<R) { // Fast forward
			int d_time = r-lastvisit[q.front().second];
			long long d_profit = profit - lastprofit[q.front().second];
			int steps = (R-r)/d_time;
			r+=steps*d_time;
			profit+=steps*d_profit;
		}
		for(;r<R;++r) {
			int k=K;
			for(int n=0;n<N && q.front().first<=k;++n) {
				k-=q.front().first;
				q.push(q.front());
				q.pop();
			}
			profit += K-k;
		}
		printf("Case #%d: %lld\n", t+1, profit);
	}
}