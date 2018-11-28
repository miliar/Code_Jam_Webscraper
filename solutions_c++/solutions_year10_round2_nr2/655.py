#include<cstdio>
#include<map>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

#define SIZE 55

typedef pair<int,int> pii;
pii arr[SIZE];

int main(){
	int TC, X, i, N, K, B, T, ret, cnt, cant;

	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	scanf("%d", &TC);

	for(X = 1; X<=TC; ++X){
		scanf("%d%d%d%d", &N, &K, &B, &T);

		for( i = 0; i<N; ++i){
			scanf("%d", &arr[i].first);
		}
		for( i = 0; i<N; ++i){
			scanf("%d", &arr[i].second);
		}

		ret = 0; cant = 0;
		for( i =N-1, cnt = 0; i>=0 && cnt < K; --i){
			if( arr[i].first + T*arr[i].second >= B){ // can reach barn
				ret += cant;
				cnt++;
			}
			else cant++;
		}

		printf("Case #%d: ", X);
		if( cnt >= K) printf("%d\n", ret);
		else puts("IMPOSSIBLE");
	}

	return 0;
}