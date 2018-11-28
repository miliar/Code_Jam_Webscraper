#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 1 << 15;

pair <long long, long long> ans[MAXN];
long long a[MAXN];
long long N, W, L;

bool check(pair <long long, long long> tmp, int pos){
	for(int i = 0; i < pos; i ++){
		if((tmp.first - ans[i].first) * (tmp.first - ans[i].first) + (tmp.second - ans[i].second) * (tmp.second - ans[i].second) <= (a[i] + a[pos]) * (a[i] + a[pos])){
			return false;
		}
	}

	return true;
}

bool DFS(int pos){
	if(pos == N){
		return true;
	}
	while(true){
		long long x = (long long) rand() * rand() % (W + 1);
		long long y = (long long) rand() * rand() % (L + 1);
		if(check(make_pair(x, y), pos)){
			ans[pos] = make_pair(x, y);
			if(DFS(pos + 1)){
				return true;
			}
		}
	}
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t ++){
		scanf("%d%d%d", &N, &W, &L);
		for(int i = 0; i < N; i ++){
			scanf("%I64d", &a[i]);
		}
		DFS(0);
		printf("Case #%d:", t);
		for(int i = 0; i < N; i ++){
			printf(" %I64d %I64d", ans[i].first, ans[i].second);
		}
		printf("\n");
	}

	return 0;
}