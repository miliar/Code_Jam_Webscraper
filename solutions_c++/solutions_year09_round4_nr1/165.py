#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_N 41

int main(int argc, char* argv[]) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);	
	int cases;
	scanf("%d", &cases);
	int cas;
	for (cas = 1; cas <= cases; ++cas) {
		int n;
		scanf("%d", &n);
		char str[MAX_N][MAX_N];
		for (int i = 0; i < n; ++i)
			scanf("%s", str[i]);
		int res = 0;
		for (int r = 0; r < n; ++r) {
			int key = r;
			while (true) {
				bool ok = true;
				for (int i = r + 1; i < n; ++i)
					if (str[key][i] == '1') {
						ok = false;
						break;	
					}
				if (ok == true)
					break;	
				key++;
			}	
			//printf("key %d\n", key);
			res += key - r; 
			char tmp[MAX_N];
			strcpy(tmp, str[key]);
			for (int i = key; i > r; --i)
				strcpy(str[i], str[i - 1]);
			strcpy(str[r], tmp);
			
			//for (int i=0; i< n; ++i)
			//printf("%s\n", str[i]);
		}
		printf("Case #%d: %d\n", cas, res);
	//	for (int i=0; i< n; ++i)
		//	printf("%s\n", str[i]);
	}
	return 0;
}
