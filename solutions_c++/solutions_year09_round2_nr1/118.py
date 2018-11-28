#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

const int	MAXL	=	100 + 10;
const int	MAXN	=	100 + 10;
const int	MAXLEN	=	10 + 10;

char	f[MAXL][MAXLEN], cur[MAXN][MAXLEN];
double	p[MAXL];
int		T, L, A, n, tot, root, Lc[MAXL], Rc[MAXL];
char	ch;

int getTree ()
{
	int ret = ++tot;
	scanf ("%lf", &p[ret]);
	ch = getchar ();
	while (ch != ')' && (ch < 'a' || ch > 'z')) ch = getchar ();

	if (ch == ')')
	{
		Lc[ret] = Rc[ret] = 0;
		return ret;
	}

	f[ret][0] = ch;
	gets (f[ret] + 1);

	ch = getchar ();
	while (ch != '(' && ch != ')') ch = getchar ();
	Lc[ret] = getTree ();
	ch = getchar ();
	while (ch != '(' && ch != ')') ch = getchar ();
	Rc[ret] = getTree ();
	ch = getchar ();
	while (ch != '(' && ch != ')') ch = getchar ();

	return ret;
}

void printTree (int r)
{
	if (r == 0) return;
	printf ("%.2lf %s\n", p[r], f[r]);
	printTree (Lc[r]);
	printTree (Rc[r]);
}

void Init ()
{
	ch = getchar ();
	while (ch != '(') ch = getchar ();
	tot = 0;
	root = getTree ();

	//printTree (root);
}

double calc (int r, double now)
{
	if (Lc[r] == 0) return now * p[r];

	int flag = 0;
	for (int i = 0; i < n; ++i)
		if (strcmp (cur[i], f[r]) == 0)
		{
			flag = 1;
			break;
		}
	
	if (flag)
		return calc (Lc[r], now * p[r]);
	else
		return calc (Rc[r], now * p[r]);
}

void Solve ()
{
	scanf ("%d", &A);
	while (A--)
	{
		scanf ("%s", cur[0]);
		scanf ("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf ("%s", cur[i]);

		printf ("%.7lf\n", calc (root, 1));
	}
}

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d:\n", i);
		Init ();
		Solve ();
	}

	return 0;
}
