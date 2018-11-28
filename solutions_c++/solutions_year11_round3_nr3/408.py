#include <iostream>
using namespace std;

int main() {
	int ntc;

	scanf("%d",&ntc);
	
	for (int tc = 1; tc <= ntc; ++tc) {
		int n, l, h;
		scanf("%d %d %d", &n, &l, &h);
		
		int arr[n];
		
		for (int i = 0; i < n; ++i){
			scanf("%d", &arr[i]);
		}
		
		int result = -1;
		for (int i = l; i <= h; ++i) {
			if (i <= 0) continue;
			result = i;
			for (int j = 0; j < n; ++j) {
				if (i % arr[j] == 0 || arr[j] % i == 0) continue;
				
				result = -1;
				break;
			}
			
			if (result != -1)
				break;
		}
		
		printf("Case #%d: ", tc);
		if (result == -1) {
			printf("NO\n");
		} else {
			printf("%d\n", result);
		}
	}
	return 0;
}
