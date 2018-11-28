#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;

int nn,n,m;
string a[2000],b[2000];
int aa[2000][2000];

int A(int i, int j)
{
	if (j>m)
		return 0;
	if (aa[i][j]==-1)
	{
		if (a[i] != b[j])
			aa[i][j] = A(i, j+1);
		else
		{
			int res=1000000;
			for (int k=1; k<=n; ++k)
				if (k!=i)
					res = min(res, A(k, j+1));
			aa[i][j] = res+1;
		}
	}
	return aa[i][j];
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d\n",&nn);
	for (int ii=1; ii<=nn; ++ii)
	{
		scanf("%d\n",&n);
		for (int i=1; i<=n; ++i)
		{
			char cc[2000];
			gets(cc);
			a[i]=cc;
		}
		scanf("%d\n",&m);
		for (int i=1; i<=m; ++i)
		{
			char cc[2000];
			gets(cc);
			b[i]=cc;
		}
		memset(aa, -1, sizeof aa);
		int res=1000000;
		for (int i=1; i<=n; ++i)
			res = min(res, A(i, 1));
		printf("Case #%d: %d\n", ii, res);
	}
	return 0;
}
