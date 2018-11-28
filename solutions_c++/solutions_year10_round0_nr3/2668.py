#include <iostream>
#include <queue>

using namespace std;

int R,k,N;
int s[100];

int solve() {
	int tmp[20];
	int ret = 0;
	queue<int>q;
	for(int i = 0;i < N;++i) {
		q.push(s[i]);
	}
	while(R--) {
		int cnt = 0;
		int ind = 0; 
		while(!q.empty()) {
			if( cnt + q.front() <= k ) {
				tmp[ind++] = q.front();
				q.pop();
				cnt += tmp[ind - 1];
			} else break;
		}
		ret += cnt;
		for(int i = 0;i < ind;++i) {
			q.push(tmp[i]);
		}
	}
	return ret;
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,cas = 1;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d%d",&R,&k,&N);
		for(int i = 0;i < N;++i) {
			scanf("%d",&s[i]);
		}
		printf("Case #%d: %d\n",cas++,solve());
	}	
	return 0;
}
