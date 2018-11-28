#include<iostream>
#include<cstring>
#include<math.h>

using namespace std;

int main(void){
	int cas, n;
	int sum, key, tot, gmin;
	freopen("C2.in", "r", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++){
		scanf("%d", &n);
		tot = 0, sum = 0, gmin = 10000000;
		for (int i = 0; i < n; i++){
			scanf("%d", &key);
			if (key < gmin)	gmin = key;
			sum += key;
			tot ^= key;
		}
		printf("Case #%d: ", t);
		if (tot)	printf("NO\n");
		else	printf("%d\n", sum-gmin);
	}
	return 0;
}