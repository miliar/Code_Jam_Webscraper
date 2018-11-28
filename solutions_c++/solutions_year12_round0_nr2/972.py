#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

int score[105];

int main()
{
	freopen("Binput.txt", "r", stdin);
	freopen("Boutput.txt", "w", stdout);
	int i, x, y;
	int n, s, p;
	int tc, nc;
	int res;
	scanf("%d", &tc);
	for (nc = 1; nc <= tc; nc++) {
		res = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (i = 0; i < n; i++)
			scanf("%d", &score[i]);
		sort(score, score+n, greater<int>());
		for (i = 0; i < n; i++) {
			x = (score[i]+2)/3;
			y = (score[i]%3 == 1 ? 0 : 1);
			if (x >= p) {
				res++;
			}
			else if (s > 0 && score[i] >= 2 && score[i] <= 28 && x+y >= p) {
				res++;
				s--;
			}
		}
		printf("Case #%d: %d\n", nc, res);
	}
}
