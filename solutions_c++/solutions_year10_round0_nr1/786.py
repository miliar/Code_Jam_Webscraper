#include <cstdio>

int n, k, ncas, cas = 0;

bool isOn(int n, int k){
	if (k & 1){
		if (n > 1)
			return isOn(n-1, k >> 1);
		else
			return true;
	}
	return false;
}

int main(){
	scanf("%d", &ncas);
	while (ncas--){
		scanf("%d %d", &n, &k);
		if (isOn(n, k))
			printf("Case #%d: ON\n", ++cas);
		else
			printf("Case #%d: OFF\n", ++cas);
	}
	return 0;
}
