#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX_N = 1009;
int N;
int as[MAX_N];

int solve(){
	int mi = 1<<29, tot = 0, x = 0;
	for(int i=0; i<N; i++){
		mi = min(mi, as[i]);
		tot += as[i];
		x ^= as[i];
	}
	return x?-1:(tot-mi);
}

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		scanf("%d",&N);
		for(int i=0; i<N; i++){
			scanf("%d",as+i);
		}
		printf("Case #%d: ",c);
		int ans = solve();
		if(ans<0){
			puts("NO");
		}
		else{
			printf("%d\n",ans);
		}
	}
	return 0;
}
