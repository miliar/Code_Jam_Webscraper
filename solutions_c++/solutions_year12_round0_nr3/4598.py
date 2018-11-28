#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main() {
	int n;
	scanf("%d", &n);

	int i;
	for(i = 0; i < n; i++) {
		int start, end;
		scanf("%d %d", &start, &end);

		int j;
		int count = 0;
		for(j = start; j < end; j++) {
			if(j > 9) {
				char str[6];
				itoa(j, str, 10);
				int len = strlen(str);
				int k;
				int check[2225] = {0,};
				for(k = 1; k < len; k++) {
					char temp[6];
					int s, index = 0;
					for(s = k; s < len; s++) {
						temp[index++] = str[s];
					}
					for(s = 0; s < k; s++) {
						temp[index++] = str[s];
					}
					temp[index] = '\0';

					int result = atoi(temp);

					if(result > j && result <= end && check[result] == 0) {
						check[result] = 1;
						count++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", i+1, count);
	}

	return 0;
}