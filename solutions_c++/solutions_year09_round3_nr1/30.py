#include <stdio.h>
#include <string.h>
#include <memory.h>
#define MOD 1000
int sol[100];
int symbol[256];
bool check[40];
bool ch[256];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	char dat[100];
	scanf("%d",&T);
	int t, len;
	for(t=1;t<=T;t++){
		scanf("%s",dat);
		len = strlen(dat);
		int i, j;
		for(i=0;i<256;i++) ch[i] = false;
		int base;
		base = 0;
		for(i=0;i<len;i++){
			if(!ch[ dat[i] ]) {
				ch[ dat[i] ] = true;
				base ++;
			}
		}
		if(base < 2) base = 2;
		for(i=0;i<40;i++) check[i] = false;
		for(i=0;i<256;i++) symbol[i] = -1;
		for(i=0;i<100;i++) sol[i] = 0;
		for(i=0;i<len;i++){
			if(symbol[ dat[i] ] == -1){
				for(j=(i==0)?1:0;check[j];j++);
				check[j] = true;
				symbol[ dat[i] ] = j;
			}
			int up;
			up = 0;
			for(j=0;j<100;j++){
				sol[j] = sol[j] * base + up;
				if(j == 0) sol[j] += symbol[dat[i]];
				up = sol[j] / MOD;
				sol[j] %= MOD;
			}
		}
		for(i=99;sol[i] == 0;i--);
		printf("Case #%d: %d", t,sol[i]);
		for(i--;i>=0;i--) printf("%03d",sol[i]);
		printf("\n");
	}
	return 0;
}