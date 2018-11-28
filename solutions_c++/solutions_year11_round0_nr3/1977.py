#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
int c[1010];
int main(){
	int i,j;
	int T;
	int sum;
	int flag;
	int cas = 1,N;
	scanf("%d",&T);
	while(T --){
		scanf("%d",&N);
		flag = 0;
		sum = 0;
		for(i = 0; i < N;i++){
			scanf("%d",&c[i]);
			flag ^= c[i];
			sum += c[i];
		}
		printf("Case #%d: ",cas++);
		if(flag != 0){
			printf("NO\n");
			continue;
		}else{
			sort(c,c+N);
			printf("%d\n",sum-c[0]);
		}
	}
	return 0;
}