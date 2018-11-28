//Solution by Ali-Amir Aldan
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
#include <set>

#define forn(i, n) for (int (i); (i) < (n); (i)++ )
#define betw(a, b, c) ((a) <= (c) && (b) >= (c))
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define pint pair <int, int> 

typedef long long ll;
typedef double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

int test_num, case_number;

#define gout case_number++, printf("Case #%d: ",case_number), cout

int gox[256], goy[256];
int n, m, col, res, fnd, sx, sy;
char s[200][200];
int w[200][200], coef[200][200];

/*void ddfs (int x, int y)
{
	printf ("here at %d %d with col = %d s[x][y]=%c gox=%d goy=%d\n", x, y, col, s[x][y], gox[s[x][y]], goy[s[x][y]]);
	w[x][y] = col;

	int xx = (x+gox[s[x][y]]*coef[x][y]+n)%n, yy = (y+goy[s[x][y]]*coef[x][y]+m)%m;
	printf ("next = %d %d\n", xx, yy);

	if (w[xx][yy])
	{
		if (w[xx][yy] != col) fnd = 0;
		if (xx!=sx || yy != sy) fnd=0, printf ("here\n");
	}
	else
		ddfs (xx, yy);
}
*/
void dfs (int x, int y)
{
	w[x][y] = col;
//	cerr << "here x = " << x << " y = " << y << endl;

	int xx = (x+gox[s[x][y]]*coef[x][y]+n)%n, yy = (y+goy[s[x][y]]*coef[x][y]+m)%m;

	if (w[xx][yy])
	{
		if (w[xx][yy] != col) fnd = 0;
		if (xx!=sx || yy != sy) fnd=0;
	}
	else
		dfs (xx, yy);
}

void main2 ()
{
	scanf ("%d %d\n", &n, &m);

	for (int i = 0; i < n; i++)
		scanf ("%s", s[i]);

	gox['-'] = 0; goy['-'] = 1;
	gox['|'] = 1; goy['|'] = 0;
	gox['/'] = 1; goy['/'] = -1;
	gox['\\'] = 1; goy['\\'] = 1;

	res = 0;
	for (int mask = 0, i, j; mask < (1<<(n*m)); mask++)
	{
		for (i = 0; i < n; i++) for (j = 0; j < m; j++)
		{
			w[i][j] = 0;
			if ((mask>>(i*m+j))&1)
				coef[i][j] = 1;
			else
				coef[i][j] = -1;
		}

		fnd = 1;
		for (i = 0; i < n && fnd; i++)
			for (j = 0; j < m && fnd; j++)
				if (!w[i][j])
				{
				 	col++;
				 	sx = i; sy = j;
				 	dfs (i, j);
				}
/*		if (fnd)
		{

		for (i = 0; i < n; i++) for (j = 0; j < m; j++)
		{
			w[i][j] = 0;
			if ((mask>>(i*m+j))&1)
				coef[i][j] = 1;
			else
				coef[i][j] = -1;
		}
		fnd = 1;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
				if (!w[i][j])
				{
				 	col++;
				 	sx = i; sy = j;
				 	ddfs (i, j);
				}
		 	for (int i = 0; i < n; i++)
		 	{
		 	 	for (int j = 0; j < m; j++)
		 	 		printf ("%d ", coef[i][j]);
		 	 	puts ("");
		 	}
		 	 	puts ("");
			break;
			exit (0);
		}*/
/*		 	for (int i = 0; i < n; i++)
		 	{
		 	 	for (int j = 0; j < m; j++)
		 	 		printf ("%d ", coef[i][j]);
		 	 	puts ("");
		 	}
		 	 	puts ("");*/
		res += fnd;
//		res++;
	}

	gout << res << endl;
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
