#include	<cstdio>
#include	<algorithm>
using namespace std;
int t, n, m, a;
bool found;
int main ()
{
	freopen ("B-small-attempt1.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
	scanf ("%d", &t);
	for (int l = 1; l <= t; ++ l)
	{
		scanf ("%d %d %d", &n, &m , &a);
		found = false;
		printf ("Case #%d: ", l);
		for (int i = 0; i <= n; ++ i)
			for (int j = 0; j <= m; ++ j)
				for (int ii = 0; ii <= n; ++ ii)
					for (int jj = 0; jj <= m; ++ jj)
						if (abs (i*jj - ii*j) == a)
						{
							printf ("0 0 %d %d %d %d\n", i, j, ii, jj);
							found = true;
							goto out;
						}
		out:
		if (!found)
			puts ("IMPOSSIBLE");
	}
	//system ("pause");
}
