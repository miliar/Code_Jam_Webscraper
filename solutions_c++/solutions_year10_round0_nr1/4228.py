#include <cstdio>


int main(){
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);
	int T, K, N, and;
	const int maxI = 30;
	int snap[maxI];
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		scanf("%d%d",&N,&K);
		//inicializa
		for (int i=0;i<N;i++)
			snap[i] = 0;
		//cambia los estados cada aplauso
		for (int k= 1;k<=K;k++){
			for (int n=N-1;n>0;n--){
				and =0;
				for (int x=0;x<n;x++)
					and = and + snap[x];
				if (and == n){
					if (snap[n]==0)
						snap[n]=1;
					else
						snap[n]=0;
				}
			}
			if (snap[0] == 0)
				snap[0] = 1;
			else
				snap[0] = 0;
		}
		and=0;
		for (int x=0;x<N;x++)
					and = and + snap[x];
		if (and == N)
		printf("Case #%d: ON\n",t);
		else
		printf("Case #%d: OFF\n",t);
	}

	return 0;
}