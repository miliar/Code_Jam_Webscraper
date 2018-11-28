#include<cstdio>
#include<algorithm>

using namespace std;

#define SIZE 1009

typedef pair<int,int> pii;

pii arr[SIZE];

int main(){
	int T, X, i, j, ret, N;

	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for( X = 1; X<=T; ++X){
		scanf("%d", &N);

		for(i = 0; i<N; ++i){
			scanf("%d%d", &arr[i].first, & arr[i].second);
		}

		sort( arr, arr + N);

		ret = 0;
		for( i = 0; i<N; ++i){
			for( j = 0; j<i; ++j){
				if(arr[j].second > arr[i].second) ret++;
			}
		}

		printf("Case #%d: %d\n", X, ret);
	}

	return 0;
}