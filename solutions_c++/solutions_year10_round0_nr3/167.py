#include <cstdio>

int main(){
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		int R, k, N, g[1000];
		scanf("%d %d %d", &R, &k, &N);
		for(int i=0; i<N; i++)
			scanf("%d", g+i);
		long long income[1000], next[1000];
		for(int i=0; i<N; i++){
			int j=i, filled=0;
			next[i]=i;
			do{
				if(filled+g[j]>k)
					break;
				filled+=g[j];
				j=(j+1)%N;
			}while(j!=i);
			income[i]=filled;
			next[i]=j;
		}
		long long total=0;
		int cur=0;
		for(int i=0; i<N && R>0; i++, R--){
			total+=income[cur];
			cur=next[cur];
		}
		int cnt=1;
		int start=cur;
		for(; R>0;){
			total+=income[cur];
			cur=next[cur];
			R--;
			if(cur==start)
				break;
			cnt++;
		}
		long long rep=R/cnt;
		for(int i=0; i<cnt; i++){
			total+=income[cur]*rep;
			cur=next[cur];
			R-=rep;
		}
		for(; R>0; R--){
			total+=income[cur];
			cur=next[cur];
		}
		printf("Case #%d: %lld\n", t, total);
	}
	return 0;
}