#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string>

#define FORr(i,A,B)	for (int i=(A); i<(B); ++i)
#define FOR(i, N)	FORr(i,0,N)

using namespace std;

int 	get_int()		{int a; 	scanf("%d", &a); 	return a;}
double	get_double()	{double a;	scanf("%lf", &a);	return a;}
char	get_char()		{char c; 	scanf("%c", &c); 	return c;}

char str_buf[100000];
string	get_str()		{scanf("%s", str_buf); return str_buf;}

void solve()
{
	int Height = get_int();
	int Width = get_int();

	int pic[50][50];

	FOR(y, Height)
	{
		string str = get_str();
		FOR(x, Width)
		{
			switch (str.at(x))
			{
			case '.': pic[y][x] = 0; break;
			case '#': pic[y][x] = 1; break;
			}
		}
	}

	FOR (y, Height)
	{
		FOR (x, Width)
		{
			if (pic[y][x] == 1)
			{
				// replace red
				if (x == Width - 1) goto Impossible;
				if (y == Height - 1) goto Impossible;
				if (pic[y][x+1] != 1) goto Impossible;
				if (pic[y+1][x] != 1) goto Impossible;
				if (pic[y+1][x+1] != 1) goto Impossible;

				pic[y][x] = 2;
				pic[y][x+1] = 3;
				pic[y+1][x] = 4;
				pic[y+1][x+1] = 5;
			}
		}
	}

	// succeeded

	FOR (y, Height)
	{
		FOR (x, Width)
		{
			char tile = '.';
			switch (pic[y][x])
			{
			case 0: tile = '.'; break;
			case 1: tile = '#'; break;
			case 2: tile = '/'; break;
			case 3: tile = '\\'; break;
			case 4: tile = '\\'; break;
			case 5: tile = '/'; break;
			}
			printf("%c", tile);
		}
		printf("\n");
	}

	return;

Impossible:
	printf("Impossible\n");
	return;
}

int main()
{
	int T = get_int();
	FOR (t, T)
	{
		printf("Case #%d:\n", t + 1);
		solve();
//		printf("\n");
	}
}
