#include <iostream>
#include <vector>
#include <string>

#define M 1000000000

using namespace std;

int a[1005][105][105];
vector<string> S, Q;
int s, q;

int get(int qq, int kk, int ll) {
	if (a[qq][kk][ll] != -1)
		return a[qq][kk][ll];
	if (qq < 0)
		return a[qq][kk][ll] = 0;
	if (Q[qq] == S[kk])
		return a[qq][kk][ll] = M;
	if (qq == 0)
		return a[qq][kk][ll] = 0;
	int res = M;
	for (int i = 0; i < s; ++i) {
		if (kk != ll)
			res = min(res, get(qq - 1, ll, i) + 1);
		else
			res = min(res, get(qq - 1, ll, i));
	}
	return a[qq][kk][ll] = res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		memset(a, 0xff, sizeof(a));
		S.clear();
		Q.clear();
		scanf("%d", &s);
		char str[200];
		gets(str);
		for (int j = 0; j < s; ++j)
		{
			gets(str);
			S.push_back(str);
		}
		scanf("%d", &q);
		gets(str);
		for (int j = 0; j < q; ++j)
		{
			gets(str);
			Q.push_back(str);
		}
		int ans = M;
		if (q == 0)
			ans = 0;
		else {
			for (int j = 0; j < s; ++j)
				for (int k = 0; k < s; ++k)
					ans = min(ans, get(q - 1, k, j));
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}

	return 0;
}
