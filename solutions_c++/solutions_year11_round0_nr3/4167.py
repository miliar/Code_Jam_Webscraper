#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main(){
	int ca, x = 0, n, val, ans, sum, low;
	scanf("%d", &ca);
	while (ca--){
		scanf("%d", &n);
		low = 1000000000;
		ans = sum = 0;
		for (int i = 0; i < n; i++){
			scanf("%d", &val);
			ans ^= val;
			sum += val;
			if (val < low) low = val;
		}
		printf("Case #%d: ", ++x);
		if (ans != 0) printf("NO\n");
		else printf("%d\n", sum - low);
	}
}
