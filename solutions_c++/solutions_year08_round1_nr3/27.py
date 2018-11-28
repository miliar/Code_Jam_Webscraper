#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int const maxN = 30;
typedef struct mType {
	int v[maxN][maxN];
	int* operator [] (int t) {
		return v[t];
	}
};
int totCases, n;
mType a;
mType base;
void Mult(mType &a, mType &b, int n, int m, int l);
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d: ", cases + 1);
		scanf("%d", &n);
		--n;
		a[0][0] = 2;
		a[0][1] = 6;
		base[0][0] = 0;
		base[0][1] = -4;
		base[1][0] = 1;
		base[1][1] = 6;

		while (n) {
			if (n & 1) Mult(a, base, 1, 2, 2);
			Mult(base, base, 2, 2, 2);
			n >>= 1;
		}
		int ans = a[0][1] - 1;
		while (ans < 0) ans += 1000;
		while (ans >= 1000) ans -= 1000;
		printf("%03d\n", ans);
	}
}
void Mult(mType &a, mType &b, int n, int m, int l)
{
	mType tem;
	memset(&tem, 0, sizeof(tem));
	for (int i(0); i < n; ++i)
	    for (int j(0); j < l; ++j) {
	        for (int k(0); k < m; ++k)
	            (tem[i][j] += a[i][k] * b[k][j]);
			tem[i][j] %= 1000;
		}
	a = tem;
}

/*   2 6 0 -4
       1 6
*/
