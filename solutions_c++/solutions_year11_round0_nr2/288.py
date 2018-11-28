#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int comb[26][26];
bool oppo[26][26];

int list[103];
int n;

bool findOppo(int x)
{
	for (int i = 0; i != n; i++)
		if (oppo[list[i]][x])
			return true;
	return false;
}

int main()
{
	int testCount, cCount, dCount, nCount;
	char x, y, z;

	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &testCount);
	for (int ct = 1; ct <= testCount; ct++) {
		memset(comb, -1, sizeof(comb));
		memset(oppo, false, sizeof(oppo));	
		scanf("%d ", &cCount);
		while (cCount--) {
			scanf("%c%c%c ", &x, &y, &z);			
			x -= 'A';
			y -= 'A';
			z -= 'A';
			comb[x][y] = comb[y][x] = z;
		}
		scanf("%d ", &dCount);
		while (dCount--) {
			scanf("%c%c ", &x, &y);
			x -= 'A';
			y -= 'A';
			oppo[x][y] = oppo[y][x] = true;			
		}
		scanf("%d ", &nCount);
		n = 0;
		while (nCount--) {
			scanf("%c", &x);
			x -= 'A';
			if (n == 0)
				list[n++] = x;
			else if (comb[x][list[n - 1]] != -1) {
				list[n - 1] = comb[x][list[n - 1]];
			}
			else if (findOppo(x)) {
				n = 0;
			}
			else
				list[n++] = x;
		}
		printf("Case #%d: [", ct);
		for (int i = 0; i != n; i++) {
			printf("%c%s", list[i] + 'A', i < n - 1 ? ", " : "");
		}
		printf("]\n");
	}
	return 0;
}
