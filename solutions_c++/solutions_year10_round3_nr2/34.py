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
	int t;
	int i, j, k;
	int n;
	int l, p, c;
	int ta;
	double dl, dp;
	freopen("in","r",stdin);freopen("out","w",stdout);

	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d %d %d", &l, &p, &c);
		ans = 0;
		dl = l;
		dp = p;
		while(dl < dp) {
			dl *= c;
			ans++;
		}
		ta = 0;
		ans--;
		j = 1;
		while(j <= ans) {
			ta ++;
			j <<= 1;
		}
		printf("Case #%d: %d\n", i, ta);
	}
	return 0;
}