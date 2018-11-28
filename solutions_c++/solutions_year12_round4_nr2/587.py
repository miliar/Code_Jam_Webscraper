#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

bool Comp(const int *x, const int *y)
{
	return *x < *y;
}

bool iComp(const int *x, const int *y)
{
	return *x > *y;
}

int n;
int w, l;
int rev;
int r[1024];
int *pr[1024];
int x[1024], y[1024];

FILE *fin, *fout;

int printxy(int i)
{
	int j;
	for ( j = 0; j < n; ++j )
		if ( pr[j] == r + i )
			break;
	if ( !rev )
		fprintf(fout, " %d.0 %d.0", x[j], y[j]);
	else
		fprintf(fout, " %d.0 %d.0", y[j], x[j]);
	return 0;
}

int main()
{
	fin = fopen("B-large.in", "r");
	fout = fopen("B-large.out", "w");
	int itest, ntest;
	fscanf(fin, "%d", &ntest);
	for ( itest = 0; ++itest <= ntest; )
	{
		int i;
		fscanf(fin, "%d%d%d", &n, &w, &l);
		for ( i = 0; i < n; ++i )
			fscanf(fin, "%d", r+i);
		for ( i = 0; i < n; ++i )
			pr[i] = r + i;
		for ( rev = 0; rev < 2; ++rev )
		{
			int dor;
			if ( rev )
			{
				int t = w;
				w = l;
				l = t;
			}
			for ( dor = 0; dor < 1000; ++dor )
			{
				int l2 = 0, w2 = 0;
				int nl = 0;
				if ( dor == 0 )
					sort(pr, pr+n, Comp);
				else if ( dor == 1 )
					sort(pr, pr+n, iComp);
				else
					random_shuffle(pr, pr+n);
				for ( i = 0; i < n; ++i )
				{
					int ix = w2, iy = l2;
					if ( ix )
						ix += *pr[i];
					if ( iy )
						iy += *pr[i];
					if ( ix > w )
					{
						l2 = nl;
						iy = nl + *pr[i];
						ix = w2 = 0;
					}
					if ( iy > l )
						break;
					if ( iy + *pr[i] > nl )
						nl = iy + *pr[i];
					w2 = ix + *pr[i];
					x[i] = ix;
					y[i] = iy;
				}
				if ( i >= n )
					break;
			}
			if ( dor < 1000 )
				break;
		}
		fprintf(fout, "Case #%d:", itest);
		for ( i = 0; i < n; ++i )
			printxy(i);
		fprintf(fout, "\n");
	}
	return 0;
}
