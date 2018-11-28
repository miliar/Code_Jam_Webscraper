#include <cstdio>

int main(){
	int T, ca = 0;
	scanf("%d", &T);
	while (T--){
		int n, k,c=0,i=0;
		scanf("%d%d", &n, &k);

		while (k != 0){
			if ((k & 1) != 1) break;
			else c++;
			if (++i == n) break;
			k = k >> 1;
		}

		printf("Case #%d: ", ++ca);
		if (c == n) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
