#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

long long n, r, k, sum, cnt;
int g, tc;
queue<int> que;

int main() {
	scanf("%d", &tc);
	int i;
	for(int t=1; t<=tc; t++){
		scanf("%lld%lld%lld", &r, &k, &n);
		while(!que.empty()) que.pop();
		for(i=0; i<n; i++){
			scanf("%d", &g);
			que.push(g);
		}
		sum = 0;
		while(r--){
			cnt = k;
			for(i=0; i<n; i++){
				g = que.front();
				if(cnt < g) break;
				cnt -= g;
				que.pop();
				que.push(g);
				sum += g;
			}
		}
		printf("Case #%d: %d\n", t, sum);
	}
	return 0;
}

