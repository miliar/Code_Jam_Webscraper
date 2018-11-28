#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int d1[] = {0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10};
int d2[] = {0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10};

void solve(int T)
{
	int N, S, P, ret = 0, cur;
	printf("Case #%d: ", T);
	scanf("%d%d%d", &N, &S, &P);
	for(int i = 1; i <= N; ++ i) {
		scanf("%d", &cur);
		if (d1[cur] >= P) ret ++;
		else if (S && d2[cur] >= P) ret ++, S --;
	}
	printf("%d\n", ret);
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T; scanf("%d", &T);
	for(int i = 1; i <= T; ++ i) solve(i);
	return 0;
}
