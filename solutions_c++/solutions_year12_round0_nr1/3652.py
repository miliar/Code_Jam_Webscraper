#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <cmath>
#include <fstream>
#include <queue>
#include <list>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fill(x, y) memset(x, y, sizeof(x))
#define deb(x) cerr << #x << " = " << (x) << "; "
#define debln(x) cerr << #x << " = " << (x) << endl
#define EPS 1e-30

typedef pair<int, int> ii;
typedef pair<int, ii> iii;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	const char *map_str = "ay bh ce ds eo fc gv hx id ju ki lg ml nb ok pr qz rt sn tw uj vp wf xm ya zq ";
	char mapX[26];
	int i = 0;
	while (map_str[i] != 0) {
		mapX[map_str[i] - 'a'] = map_str[i + 1];
		i += 3;
	}

	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; i++) {
		char line[257];
		gets(line);
		int j = 0;
		printf("Case #%d: ", i);
		while (line[j] > 0) {
			if (line[j] == ' ') putchar(' ');
			else putchar(mapX[line[j] - 'a']);
			j++;
		}
		puts("");
	}

	return 0;
}
