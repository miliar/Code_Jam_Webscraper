#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char mark[262144];
int nn;
int num[10485760];

int main()
{
	int ntest, itest;
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &ntest);
	for ( itest = 0; ++itest <= ntest; )
	{
		int a, b, i, res = 0;
		fscanf(fin, "%d%d", &a, &b);
		for ( i = a; i <= b; ++i )
		{
			int te = 1, de, min;
			while ( te < i )
				te *= 10;
			min = te / 10;
			//memset(mark, 0, sizeof(mark));
			nn = 0;
			for ( de = 10; de < te; de *= 10 )
			{
				int j = i * (__int64) (te + 1) / de % te;
				if ( i < j && j >= min && j >= a && j <= b )//&& !(mark[j>>3]&1<<(j&7)) )
				{
					num[nn++] = j;
					//mark[j>>3] |= 1 << (j&7);
					//printf("(%d, %d)\n", i, j);
				}
			}
			sort(num, num+nn);
			for ( int j = 0; j < nn; ++j )
				if ( j == 0 || num[j] != num[j-1] )
					++res;
		}
		fprintf(fout, "Case #%d: %d\n", itest, res);
	}
	return 0;
}
