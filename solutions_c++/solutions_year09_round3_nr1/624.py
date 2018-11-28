#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	FILE *fp;
	fp = fopen("output.txt", "w");
	int T, i, j;
	char str[70];
	int num[70];
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++) {
		scanf("%s", str);
		int len = strlen(str);
		num[0] = 1;
		int limit = 0;
		for(i = 1; i < len; i++) {
			for(j = 0; j < i; j++) {
				if(str[i] == str[j]) {
					num[i] = num[j];
					break;
				}
			}
			if(j == i) {
				num[i] = limit;
				limit++;
				if(limit == 1) limit++;
			}
		}
		int base;
		if(limit == 0) base = 2;
		else base = limit;
		__int64 ans = 0;
		for(i = 0; i < len; i++) {
			ans = ans*base + num[i];
		}
		fprintf(fp, "Case #%d: %I64d\n", cases, ans);
	}
	fclose(fp);
	return 0;
}