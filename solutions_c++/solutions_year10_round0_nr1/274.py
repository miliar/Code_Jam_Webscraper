#include <stdio.h>

bool getac(int n, int k){
	return k % (1<<n) == (1<<n)-1;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <= T; TT++){
		int n,k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", TT, getac(n,k)?"ON":"OFF");
	}
}