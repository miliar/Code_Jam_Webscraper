#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct T
{
	int left;
	int right;
}T;

#define N 1001

T t[N];
int ans;

int cmp(const void *aa, const void *bb)
{
	T *a = (T*)aa;
	T *b = (T*)bb;
	if(a->left > b->left) return 1;
	return -1;
}

int main()
{
	int c;
	int i, j, k;
	int n;
	freopen("in","r",stdin);freopen("out","w",stdout);

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		scanf("%d", &n);
		ans = 0;
		for(j = 0; j < n; j++) {
			scanf("%d %d", &t[j].left, &t[j].right);
		}
		qsort(&t, n, sizeof(T), cmp);
//		for(j = 0; j < n; j++)printf("%d %d\n", t[j].left, t[j].right);
		for(j = 0; j <n; j++) {
			for(k = j + 1; k < n; k++) {
				if(t[k].right < t[j].right) ans++;
			}
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}