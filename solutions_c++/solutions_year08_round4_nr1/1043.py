#include <cstdio>
#include <cstring>
#include <algorithm>
#define MIN(a, b) ((a)<(b)?(a):(b))
int list[10000][2];
int tree[10000], changable[5004];
int m, in;
const int inf = 0x3fffffff;
void init()
{
	memset(list, -1, sizeof(list));
}
int count(int index, int need);
int calc(int index, int need)
{
	int left, right;
	int op  = tree[index];
	if(list[index][op]>=0)
		return list[index][op];

	left = count(index<<1, need);
	right = count((index<<1)+1, need);
	if(need == op)
		list[index][op] = left + right;
	else
		list[index][op] = MIN(left, right);
	return list[index][op];
}
int count(int index, int need)
{
	int res, resc = inf;
	if(index > in)
	{
		if(need == tree[index])
			return 0;
		else
			return inf;
	}
	res = calc(index, need);
	if(changable[index])
	{
		tree[index] = !tree[index];
		resc = calc(index, need)+1;
		tree[index] = !tree[index];
	}
	return MIN(res, resc);
}
void solve() {
	int i, j;
	int need;
	init();
	scanf("%d%d", &m, &need);
	in = (m-1)>>1;
	for(i = 1;i <= in;i++)
		scanf("%d%d", &tree[i], &changable[i]);
	for(;i <= m;i++)
		scanf("%d", &tree[i]);
	j = count(1, need);
	if(j < inf)
		printf("%d\n", j);
	else
		printf("IMPOSSIBLE\n");
	return;
}
int main() {
	int casei, casen;
	freopen("E:\\A-small-attempt0.in", "r+", stdin);
	freopen("E:\\test.out", "w+", stdout);
	scanf("%d", &casen);
	for (casei = 1; casei <= casen; casei++) {
		printf("Case #%d: ", casei);
		solve();
	}
	return 0;
}
