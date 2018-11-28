#include <cstdio>

int main(){
	freopen("input.txt", "rb", stdin);
	freopen("output.txt", "wb", stdout);
	int tst, n, k;
	scanf("%d", &tst);
	for (int i=1; i<=tst; i++){
		scanf("%d %d", &n, &k);
		printf("Case #%d: ", i);
		k %= (1 << n);
		if (k + 1 != (1<<n))
            printf("OFF\n");
        else
            printf("ON\n");
	}
	return 0;
}
