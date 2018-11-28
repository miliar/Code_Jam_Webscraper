#include<stdio.h>
#include<string.h>
int pow2[32];
int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int n, k;
	int tcase;
	int flagcase = 0;
	for(int i = 0; i < 32; i++ ){
		pow2[i] = (1<<i);
	}
	scanf("%d",&tcase);
	while(tcase--){
		scanf("%d%d",&n,&k);
		if(k%pow2[n] == pow2[n]-1){
			printf("Case #%d: ON\n",++flagcase);
		}else{
			printf("Case #%d: OFF\n",++flagcase);
		}
	}
	return 0;
} 
