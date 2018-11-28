//be name oo
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		int n;
		scanf("%d", &n);
		int allXor = 0, minV = 1 << 25, sum = 0;
		for(int j = 0; j < n; j++){
			int a;
			scanf("%d", &a);
			allXor ^= a;
			minV = min(minV, a);
			sum += a;
		}
		printf("Case #%d: ", i);
		if(allXor == 0)
			printf("%d\n", sum - minV);
		else	printf("NO\n");
	}
	return 0;
}

