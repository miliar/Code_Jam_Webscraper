#include <cstdio>
using namespace std;
#define LMAX 32
#define DMAX 8192
#define NMAX 512

int D, L, N, s, p;
char alpha[DMAX][LMAX];
int index[DMAX], auxi[DMAX];
int start[LMAX], end[LMAX];
char strg[NMAX];

int minim(int l, int r)
{
	return l < r? l: r;
}

int maxim(int l, int r)
{
	return l > r? l: r;
}

int compare(int i, int j)
{
	for (int k = 0; k < L; ++k)
	{
		if (alpha[i][k] < alpha[j][k])
			return -1;
		if (alpha[i][k] > alpha[j][k])
			return 1;
	}

	return 0;
}

int findsmallest(int i, char c, int l, int r)
{
	if (l > r) return D+1;
	
	int m = (l+r) >> 1;

	if (alpha[index[m]][i] < c)
		return findsmallest(i, c, m+1, r);
	if (alpha[index[m]][i] > c)
		return findsmallest(i, c, l, m-1);
	if (alpha[index[m]][i] == c)
		return minim(m, findsmallest(i, c, l, m-1));
}

int findlargest(int i, char c, int l, int r)
{
	if (l > r) return 0;

	int m = (l+r) >> 1;

	if (alpha[index[m]][i] > c)
		return findlargest(i, c, l, m-1);
	if (alpha[index[m]][i] < c)
		return findlargest(i, c, m+1, r);
	if (alpha[index[m]][i] == c)
		return maxim(m, findlargest(i, c, m+1, r));
}

void msort(int l, int r)
{
	if (l >= r) return;
	int m = (l+r) >> 1, i, j, k;
	msort(l, m);
	msort(m+1, r);
	for (i = k = l, j = m+1; i <= m && j <= r;)
		if (compare(index[i], index[j]) <= 0)
			auxi[k++] = index[i++];
		else
			auxi[k++] = index[j++];

	for (; i <= m;)
		auxi[k++] = index[i++];

	for (; j <= r;)
		auxi[k++] = index[j++];

	for (k = l; k <= r; ++k)
		index[k] = auxi[k];
}

void rec(int pos, int l, int r)
{
	for (int i = start[pos]; i <= end[pos]; ++i)
	{
		char c = strg[i];

		int newl = findsmallest(pos, c, l, r);
		int newr = findlargest(pos, c, l, r);

		if (newr-newl+1 >= 0)
			if (pos >= L-1)
				s += newr-newl+1;
			else
				rec(pos+1, newl, newr);
	}
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	scanf("%d%d%d", &L, &D, &N);
	for (int i = 1; i <= D; ++i)
	{
		index[i] = i;
		scanf("\n%s", &alpha[i]);
	}

	msort(1, D);

	for (int i = 1; i <= N; ++i)
	{
		scanf("\n%s", &strg);
		p = 0;
		for (int j = 0; j < L; ++j)
			if ('a' <= strg[p] && strg[p] <= 'z')
			{
				start[j] = end[j] = p;
				p++;
			}
			else
			{
				p++;
				start[j] = p;
				while ('a' <= strg[p] && strg[p] <= 'z')
					p++;
				end[j] = p-1;
				p++;
			}

		s = 0;
		rec(0, 1, D);

		printf("Case #%d: %d", i, s);
		if (i < N)
			printf("\n");
	}

	return 0;
}