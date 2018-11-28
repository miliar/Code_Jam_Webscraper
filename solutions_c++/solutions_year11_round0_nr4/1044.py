#include<cstdio>
int main(){

	int T;
	int N;
	
	scanf("%d",&T);
	for (int k=1;  k <= T; ++k){
		scanf("%d",&N);
		int res = 0;
		int x;
		for (int i=1;i <= N; ++i){ 
			scanf("%d",&x);
			if (i!=x) res++;
		}
		printf("Case #%d: %d.000000\n",k,res);
	}

	return 0;
}
