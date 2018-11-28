#include <stdio.h>
#include <string>
#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;
int k;
int p, q;
const int maxn = 11000;
bool a[maxn];
int lst[maxn];
bool was[maxn];
int perm[maxn];

int getLeft(int q)
{
	int o = 0;
	while (q > 0 && !a[q])
	{
		q--;
		o++;
	}
	return o - 1;
}

int getRight(int q)
{
	int o = 0;
	while (q <= p && !a[q])
	{
		q++;
		o++;
	}
	return o - 1;
}

int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w", stdout);
	scanf("%d", &k);
	for (int t = 1; t <= k; t++)
	{
		scanf("%d%d", &p, &q);
		memset(a, 0, sizeof(a));
		for (int i = 0; i < q; i++)
			scanf("%d", &lst[i]);
		memset(was, 0, sizeof(was));
		int out = 1000000000;
		for (int i = 0; i < q; i++)
			perm[i] = i;
		/*for (int j = 0; j < q; j++)
		{
			int rl, rr;
			int l = 2 * p;
			int mx;
			for (int i = 0; i < q; i++)
			if (!was[i])
			{
				rl = getLeft(lst[i]);
				rr = getRight(lst[i]);
				//cout << lst[i] << " " << rl << " " << rr << endl;
				if (rr > rl)
					rl = rr;
				if (rl < l)
				{
					mx = i;
					l = rl;
				}
			}
			//cout << lst[mx] << endl;
			out += getLeft(lst[mx]) + getRight(lst[mx]);
			was[mx] = true;
			a[lst[mx]] = true;
		}  */
		while (3 > 1)
		{
			memset(a, 0, sizeof(a));
			int r = 0;
			for (int i = 0; i < q; i++)
			{
				r += getRight(lst[perm[i]]);
				r += getLeft(lst[perm[i]]);
				a[lst[perm[i]]] = true;
			}
			if (out > r) out = r;
			if (!next_permutation(perm, perm + q) ) break;
		}
		printf("Case #%d: %d\n", t, out);
	}
	return 0;
}