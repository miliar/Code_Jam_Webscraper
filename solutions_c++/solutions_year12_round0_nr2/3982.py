#include<stdio.h>
#include<stdlib.h>
int t[121];
int count[121];
int min(int a,int b){
	return a > b ? b : a;
}
int main(){
	int T;
	int N,S,p;
	scanf("%d",&T);
	for(int ca=0;ca<T;ca++){
		scanf("%d %d %d",&N,&S,&p);
		for(int i=0;i<=30;i++)count[i] = 0;
		for(int i=0;i<N;i++){
			scanf("%d",&t[i]);
			count[t[i]] ++;
		}
		printf("Case #%d: ",ca + 1);
		int ans = 0;
		int lower = p * 3 - 2;
		if(lower < 0) lower = 0;
		for(int i=lower;i <= 30;i++){
			ans += count[i];
		}
		int tmp = 0;
		if(lower - 1 > 0)tmp += count[lower - 1];
		if(lower - 2 > 0)tmp += count[lower - 2];
		ans += min(S, tmp);
		printf("%d\n",ans);
	}
	return 0;
}

