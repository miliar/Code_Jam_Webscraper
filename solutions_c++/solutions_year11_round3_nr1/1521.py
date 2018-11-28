#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int n, r, c;
char m[100][100];

int main()
{
	int i, j, k, tag;

	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d %d", &r, &c);
		for (j = 0; j < r; j++)
			scanf("%s", m[j]);
		for (j = 0; j < r - 1; j++)
			for (k = 0; k < c - 1; k++)
				if (m[j][k] == '#' &&
					m[j + 1][k] == '#' &&
					m[j][k + 1] == '#' &&
					m[j + 1][k + 1] == '#') {
					m[j][k] = m[j + 1][k + 1] = '/';
					m[j + 1][k] = m[j][k + 1] = '\\';
				}
		tag = 1;
		for (j = 0; j < r; j++)
			for (k = 0; k < c; k++)
				if (m[j][k] == '#')
					tag = 0;
		printf("Case #%d:\n", i + 1);
		if (tag) {
			for (j = 0; j < r; j++)
				printf("%s\n", m[j]);
		} else {
			printf("Impossible\n");
		}
	}

	return (0);
}


