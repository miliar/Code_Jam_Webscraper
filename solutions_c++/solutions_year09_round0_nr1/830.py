#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

const int	MAXL	=	15 + 10;
const int	MAXD	=	5000 + 10;
const int	MAXN	=	500 + 10;

int			w[MAXL];
char		s[MAXD][MAXL], ch;
int			N, D, L;

void Init ()
{
	scanf ("%d%d%d\n", &L, &D, &N);
	for (int i = 0; i < D; ++i)
		scanf ("%s\n", s[i]);
}

int calc ()
{
	for (int i = 0; i < L; ++i)
	{
		w[i] = 0;

		ch = getchar ();
		if (ch != '(') w[i] = (1 << (ch - 'a')); else
		{
			ch = getchar ();
			while (ch != ')')
			{
				w[i] |= (1 << (ch - 'a'));
				ch = getchar ();
			}
		}
	}
	getchar ();

	int ret = 0;

	for (int i = 0; i < D; ++i)
	{
		int flag = 1;
		for (int j = 0; j < L; ++j)
			if ((w[j] & (1 << (s[i][j] - 'a'))) == 0)
			{
				flag = 0;
				break;
			}
		
		ret += flag;
	}

	return ret;
}

void Solve ()
{
	for (int i = 1; i <= N; ++i)
		printf ("Case #%d: %d\n", i, calc ());
}

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	Init ();
	Solve ();

	return 0;
}
