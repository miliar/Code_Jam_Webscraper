#include <cstdio>
#include <algorithm>
using namespace std;

int n, na, nb, t;

struct node
{
	int t, lv;
	node (int tt = 0, int lvv = 0) : t(tt), lv(lvv) {}
	bool operator<(const node &tt) const
	{
		if (t == tt.t)
			return lv < tt.lv;
		return t < tt.t;
	}
} a[500], b[500];
int inda, indb;

void input(node x[], node y[], int &indx, int &indy)
{
	int h, m;
	int t0, t1;
	scanf("%d:%d", &h, &m);
	t0 = h * 60 + m;
	scanf("%d:%d", &h, &m);
	t1 = h * 60 + m;
	x[indx++] = node(t0, 1);
	y[indy++] = node(t1 + t, 0);
}

int go(node x[], int &ind)
{
	int num = 0;
	int res = 0;

	for (int j = 0; j < ind; ++j) {
		if (x[j].lv) {
			if (num)
				--num;
			else
				++res;
		}
		else
			++num;
	}
	return res;
}
int main()
{
	//freopen("B-large.in", "r",stdin);
	//freopen("B-large.out", "w", stdout);

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &t);
		scanf("%d%d", &na, &nb);
		inda = indb = 0;
		for (int j = 0; j < na; ++j)
			input(a, b, inda, indb);
		for (int j = 0; j < nb; ++j)
			input(b, a, indb, inda);
		sort(a, a + inda);
		sort(b, b + indb);
		printf("Case #%d: %d %d\n", i + 1, go(a, inda), go(b, indb));
	}
	return 0;
}