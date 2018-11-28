#include<stdio.h>
#include<stdlib.h>
int a[1024];
int pre[1024];
int la[1024];
int min(int a,int b){
	if(a <  b)return a;
	return b;
}
int L,t,N,C;
int tmp;
int main(){
	int T;
	tmp = scanf("%d",&T);
	for(int ca=0;ca<T;ca++){
		tmp = scanf("%d %d %d %d",&L,&t,&N,&C);
		for(int i=0;i<C;i++){
			tmp = scanf("%d",&a[i]);
		}
		pre[0] = 0;
		for(int i=1;i<=N;i++){
			pre[i] = pre[i-1] + a[((i - 1 ) % C)];
		}
		int total = pre[N];

		la[N] = 0;
		for(int i=N-1;i>=0;i--){
			la[i] = la[i + 1] + a[(i) % C];
		}
		/*
		for(int i=0;i<=N;i++){
			printf("%d ",pre[i]);
		}
		printf("\n");
		for(int i=0;i<=N;i++){
			printf("%d ",la[i]);
		}
		printf("\n");
		*/
		int ans = 2147483647;
		if(L == 0){
			ans = pre[N] * 2;
		}else if(L == 1){
			for(int i=0;i<N;i++){
				int now = a[ (i)  % C ];
				int time = 0;
				if(t < pre[i] * 2){
					time = pre[i] * 2 + now + (la[i + 1]) * 2;
				}else{
					int need = t / 2 - pre[i];
					time = pre[i] * 2  + (la[i + 1]) * 2;
				//	printf("need = %d)",need);
					if(need <= now){
						time += need * 2 + (now - need);
					}else{
						time += now * 2;
					}
				}
				//printf("%d,",time);
				ans = min(ans,time);
			}
		
		
		}else{
			for(int i=0;i<N;i++){
				int first_now = a[(i) % C];
				int first_time = 0;
				if(t < pre[i] * 2){
					first_time = pre[i] * 2 + first_now;
				}else{
					int need = t / 2 - pre[i];
					first_time = pre[i] * 2;
					if(need <= first_now){
						first_time += need * 2 + (first_now - need);
					}else{
						first_time += first_now * 2;
					}
				}
				//printf("i = %d,first_time = %d\n",i,first_time);
				for(int j= i + 1;j<N;j++){
					int second_now = a[(j) % C];
					int second_time = 0;
					second_time = first_time + 2 * (pre[j] - pre[i + 1]);
					//printf("second_time = %d ",second_time);
					if(t < second_time){
						second_time += second_now;
					}else{
						int need_time = t - second_time;
						if(need_time <= second_now * 2){
							second_time += need_time + (second_now - need_time / 2);
						}else{
							second_time += second_now * 2;
						}
					}
					second_time += la[j + 1] * 2;
					//printf("(%d,%d) = %d\n",i,j,second_time);
					ans = min(ans,second_time);


				}
			}
		}
		printf("Case #%d: %d\n",ca + 1,ans);
		
	}
}
