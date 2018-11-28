#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

char temp[100], line[10000];
int l[100], r[100];
double p[100];
char feature[100][30];
char list[100][30];
int stack[100];

int main() {
	int caseSize;
	scanf("%d", &caseSize);
	for (int T = 1; T <= caseSize; T++) {
		int L;
		scanf("%d\n", &L);
		int length = 0;
		char ch;
		while (L-- > 0) {
			gets(temp);
			int len = strlen(temp);
			line[length++] = ' ';
			for (int i = 0; i < len; i++) line[length++] = temp[i];
		}
		line[length] = 0;
		int top = 0;
		int size = 0;
		int link = 0;
		do {
			if (top > 0 && r[stack[top - 1]] != -1) {
				while (line[link] == ' ') link++;
				link++;
				top--;
				continue;
			}
			l[size] = -1; r[size] = -1;
			while (line[link] == ' ') link++;
			link++;
			while (line[link] == ' ') link++;
			sscanf(line + link, "%lf", &p[size]);
			while (line[link] <= '9' && line[link] >= '0' || line[link] == '.') link++;
			while (line[link] == ' ') link++;
			ch = line[link++];
			if (ch == ')') {
				if (top > 0 && l[stack[top - 1]] == -1) l[stack[top - 1]] = size;
				else if (top > 0 && r[stack[top - 1]] == -1) r[stack[top - 1]] = size;
				size++;
			} else {
				feature[size][0] = ch;
				if (line[link] == ' ') feature[size][1] = 0;
				else {
					sscanf(line + link, "%s", feature[size] + 1);
					while (isalpha(line[link])) link++;
				}
				if (top > 0 && l[stack[top - 1]] == -1) l[stack[top - 1]] = size;
				else if (top > 0 && r[stack[top - 1]] == -1) r[stack[top - 1]] = size;
				stack[top++] = size++;
			}
		} while (top > 0);
		printf("Case #%d:\n", T);
		int A, n;
		scanf("%d", &A);
		for (int k = 0; k < A; k++) {
			scanf("%s%d", line, &n);
			for (int i = 0; i < n; i++)
				scanf("%s", list[i]);
			int pos = 0;
			double result = p[0];
			while (l[pos] != -1) {
				bool found = false;
				for (int i = 0; i < n; i++) if (strcmp(list[i], feature[pos]) == 0)
					found = true;
				if (found) pos = l[pos];
				else pos = r[pos];
				result *= p[pos];
			}
			printf("%.7lf\n", result);
		}
	}
	return 0;
}
