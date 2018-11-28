#include <stdio.h>
#include <iostream>
using namespace std;

#define FOR(i,n) for(i=0; i<(n); ++i)

int main()
{
	FILE *fi = fopen("a.txt", "rt");
	FILE *fo = fopen("a.out", "wt");

	int t,tt;

	int A[1000], B[1000];
	int AN[1000], BN[1000];
	int as, bs;

	fscanf(fi, "%d", &tt);
	FOR(t,tt)
	{
		as = bs = 0;
		int n,i;
		fscanf(fi, "%d", &n);
		FOR(i,n)
		{
			char c = ' ';
			int v;
			while (c != 'O' && c != 'B')
			{
				fscanf(fi, "%c", &c);
			}
			fscanf(fi, "%d", &v);
			
			if (c=='O')
			{
				AN[as] = i;
				A[as++] = v;
			}
			else
			{
				BN[bs] = i;
				B[bs++] = v;
			}
		}

		int ret = 0; 
		int ap = 0, bp = 0;
		int av = 1, bv = 1;
		int cb = 0;
		while (ap < as || bp < bs)
		{
			bool pushed = false;
			if (ap < as)
			{
				if (av < A[ap]) ++av;
				else if (av > A[ap]) --av;
				else if (cb == AN[ap]) {++ap; ++cb; pushed=true;}
			}
			if (bp < bs)
			{
				if (bv < B[bp]) ++bv;
				else if (bv > B[bp]) --bv;
				else if (cb == BN[bp] && !pushed) {++bp; ++cb;}
			}
			++ret;
		}
		fprintf(fo, "Case #%d: %d\n", t+1, ret);
	}

	fclose(fo);
	fclose(fi);
	return 0;
}