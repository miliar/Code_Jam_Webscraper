#include <stdio.h>
#include <string.h>

char str[256];
char combine_table[256][256];
bool opposed_table[256][256];
char ans[256];
int top;
int n;

int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		int num_combine;
		memset(combine_table, 0, sizeof(combine_table));
		scanf("%d", &num_combine);
		for (int i = 0; i < num_combine; ++i) {
			scanf("%s", str);
			combine_table[str[0]][str[1]] = str[2];
			combine_table[str[1]][str[0]] = str[2];
		}

		int num_opposed;
		memset(opposed_table, false, sizeof(opposed_table));
		scanf("%d", &num_opposed);
		for (int i = 0; i < num_opposed; ++i) {
			scanf("%s", str);
			opposed_table[str[0]][str[1]] = true;
			opposed_table[str[1]][str[0]] = true;

		}
		scanf("%d", &n);
		scanf("%s", str);

		top = 0;
		for (int i = 0; i < n; ++i) {
			ans[top++] = str[i];
			if (top < 2) continue;
			if (combine_table[ans[top - 1]][ans[top - 2]] != 0) {
				char temp = combine_table[ans[top - 1]][ans[top - 2]]; 
				top -= 2;
				ans[top++] = temp;
			}
			for (int j = 0; j < top - 1; ++j)
				if (opposed_table[ans[top - 1]][ans[j]]) {
					top = 0;
				}
		}



		printf("Case #%d: ", k + 1);
		printf("[");
		for (int i = 0; i < top - 1; ++i)
			printf("%c, ", ans[i]);
		if (top > 0)
			printf("%c", ans[top - 1]);
		printf("]\n");
	}
	return 0;
}
