#include<cstdio>

int T, ca, N, K;

int main(){
	scanf("%d", &T);
	while (T--){
		scanf("%d%d", &N, &K);
		bool ok = !((K+1)%(1<<N));
		printf("Case #%d: %s\n", ++ca, ok?"ON":"OFF");
	}
	return 0;
}
