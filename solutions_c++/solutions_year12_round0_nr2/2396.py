#include<stdio.h>
#include<string.h>

int score[101], point[101], used[101];

int main(){
	int T, cnt;
	cnt = 0;
	scanf("%d", &T);
	while(T--){
		int ans, N, S, p;
		scanf("%d %d %d", &N, &S, &p);
		ans = 0;
		memset(used, 0, sizeof(used));
		for(int i = 0; i < N; i++) scanf("%d", &score[i]); 
		for(int i = 0; i < N; i++){
			if(score[i]%3 == 0) point[i] = score[i]/3;
			else point[i] = score[i]/3 + 1;
			if(point[i] >= p) ans++, used[i]++;
		}
		for(int i = 0; i < N; i++){
			if(!used[i]){
				if(score[i] == 0 || score[i] == 1 || score[i] == 29 || score[i] == 30) continue;
				else if(score[i]%3 != 1 && point[i]+1 >= p && S > 0) ans++, S--; 
			}
		}
		
		printf("Case #%d: %d\n",++cnt, ans);
	}

	return 0;
}
