#include<stdio.h>
#include<stdlib.h>
int g[2048];
int used[2048];
int next[2048];
int earn[2048];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int R,k,N;
		int total = 0;
		scanf("%d %d %d",&R,&k,&N);
		for(int i=0;i<N;i++){
			scanf("%d",&g[i]);
			total += g[i];
			g[N + i] = g[i];
			used[i] = -1;
		}
		for(int i=0;i<N;i++){
			int now = 0;
			for(int j=i;;j++){
				now += g[j];
				if(now > k || j == (i + N)){
					next[i] = j % N;
					earn[i] = now - g[j];
					break;
				}
			}
		}

		int now_lo = 0;
		int ans = 0;
		for(int i=0;i<R;i++){
			used[now_lo] = 1;
			ans += earn[now_lo];
			now_lo = next[now_lo];
		}
		printf("Case #%d: %d\n",t + 1 , ans);
		

	}
	return 0;
}
