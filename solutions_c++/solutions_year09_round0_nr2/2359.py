#include <stdio.h>

int cases, x, y, h[100][100];
char b[100][100], nl;

char jump(int y1, int x1)
{
	if (b[y1][x1]) return b[y1][x1];
	char dummy;
	int n=11111, o=11111, w=11111, s=11111, m=h[y1][x1];
	if (y1) n=h[y1-1][x1];
	if (y1<y-1) s=h[y1+1][x1];
	if (x1) w=h[y1][x1-1];
	if (x1<x-1) o=h[y1][x1+1];
	if ((n>=m) && (o>=m) && (s>=m) && (w>=m))
		dummy=nl++;
	else if ((n<=w) && (n<=o) && (n<=s))
		dummy=jump(y1-1, x1);
	else if ((w<=o) && (w<=s))
		dummy=jump(y1, x1-1);
	else if ((o<=s))
		dummy=jump(y1, x1+1);
	else
		dummy=jump(y1+1, x1);
	b[y1][x1]=dummy;
	return dummy;
}

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		scanf(" %d %d", &y, &x);
		for(int j=0; j<y; j++)
			for(int i=0; i<x; i++)
			{
				b[j][i]=0;
				scanf(" %d", &h[j][i]);
			}
		nl='a';
		printf("Case #%d:\n", cs);
		for(int j=0; j<y; j++)
		{
			for(int i=0; i<x; i++)
				printf(" %c", jump(j, i));
			printf("\n");
		}
	}
	return 0;
}
