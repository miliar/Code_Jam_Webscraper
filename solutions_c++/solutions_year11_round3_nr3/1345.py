#include<stdio.h>
int main(){
int T,cases=0;
scanf("%d",&T);
while(T--){
	cases++;
	int N, L, H, freq[10000];
	scanf("%d%d%d", &N, &L, &H);
	for(int i = 0; i < N; i++){
		scanf("%d", &freq[i]);
	}
	printf("Case #%d: ",cases);
	bool isPoss = false;
	for(int i = L; i <= H; i++){
		bool isHarmony = true;
		for(int j = 0; j <  N; j++){
			if(freq[j]%i == 0 || i%freq[j] == 0){
			}else{
				isHarmony = false;
				break;
			}
		} 
		if(isHarmony){
			printf("%d\n",i);
			isPoss = true;
			break;
		}
	}
	if(!isPoss){
		printf("NO\n");
	}
}
return 0;
}
