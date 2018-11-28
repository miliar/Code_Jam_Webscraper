#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
	int T,N,ans,
		Max,c[1001];

	scanf("%d",&T);
	for(int i=0; i<T; i++){
		ans = Max = 0;

		scanf("%d",&N);
		for(int j=0; j<N; j++){
			scanf("%d",c+j);
			ans ^= c[j];
		}
		if(ans!=0){
			printf("Case #%d: NO\n",i+1);
			continue;
		}
		sort(c,c+N);
		for(int j=1; j<N; j++) Max += c[j];

		printf("Case #%d: %d\n",i+1,Max);
	}
	return 0;
}
