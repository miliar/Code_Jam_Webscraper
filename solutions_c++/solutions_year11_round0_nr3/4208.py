#include <iostream>
using namespace std;

int main(){ 
	int ntc;
	
	scanf("%d", &ntc);
	for (int tc = 1; tc <= ntc; ++tc) {
		int n;
		scanf("%d", &n);
		int num, temp;
		
		scanf("%d", &num);
		int sum = num;
		int minim = num;
		for (int i = 1; i < n; ++i) {
			scanf("%d", &temp);
			minim = min(minim, temp);
			num = num ^ temp;
			//printf("%d\n", num);
			sum += temp;
		}
		
		printf("Case #%d: ", tc);
		
		if (num != 0) {
			printf("NO\n");
		} else {
			printf("%d\n", sum - minim);
		}
	}

	return 0;
}
