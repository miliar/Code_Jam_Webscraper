#include<cstdio>

unsigned long int power[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824};
int t,n,k;

int main() {
	scanf("%d",&t);
	for(int i=1;i<=t;++i) {
		scanf("%d %d",&n,&k);
		k++;
		printf("Case #%d: ",i);
		if(k%power[n]) {
			printf("OFF");
		} else {
			printf("ON");
		}
		printf("\n");
	}
}
