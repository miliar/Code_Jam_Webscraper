#include <stdio.h>

int main() {
	int n; scanf("%d\n", &n);
	for(int i = 0; i < n; i++){
		int t; scanf("%d\n", &t);
		int position = 0;
		for(int j = 0; j < t; j++) {
			int temp; scanf("%d", &temp);
			if(temp == j + 1) position++;
		}
		printf("Case #%d: %d\n", i+1, t - position);
	}
	return 0;
}
