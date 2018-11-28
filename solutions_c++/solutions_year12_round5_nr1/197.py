#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int maxn = 1000 + 10;
struct node
{
	int id, x;
} a[maxn];
int n, p[maxn], L[maxn];

bool cmp(node a, node b)
{
	return (a.x>b.x || (a.x==b.x && a.id<b.id));
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int TextN, TT = 0;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d", &n);
		for (int i = 0; i != n; i++) scanf("%d", &L[i]);
		for (int i = 0; i != n; i++) scanf("%d", &p[i]);
		for (int i = 0; i != n; i++) {
			a[i].id = i;
			a[i].x = L[i] * p[i];
		}
		sort(a, a + n, cmp);
		printf("Case #%d:", ++TT);
		for (int i = 0; i != n; i++) printf(" %d", a[i].id);
		printf("\n");
	}
	return 0;
}