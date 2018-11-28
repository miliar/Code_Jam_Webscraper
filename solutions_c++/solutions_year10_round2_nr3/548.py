#include <cstdio>
#include <cstring>
#define mod 100003
int n;
int x[32];


int sol ;
void afis ()
{
	int a[32];
	int nr = 0;
	int i, j;

	for (i = 1; i <= n; ++i)
		if (x[i])
			a[++nr] = i;

	for (i = nr; i != 1; )
	{

		
		for (j = i - 1; j >= 1; --j)
			if (a[j] == i)
				break;

		if (a[j] != i) return;

		i = j;



	}
	
	++sol;
	sol %= mod;
	//printf ("hey\n");
}

void back (int k)
{
	if (k == n + 1) afis ();
	else
	{
		if (k != n)
		{
			x[k] = 0;
			back (k + 1);
		}
		x[k] = 1;
		back (k + 1);
	}
}

void solve (int caz)
{

	fprintf (stderr, "%d\n", caz);
	sol = 0;
	back (1);	

	printf ("Case #%d: %d\n", caz, sol);

}



int main ()
{
	freopen ("c.in", "r", stdin);
	freopen ("c.out", "w", stdout);
	int T, caz;

	scanf ("%d\n", &T);

	for (caz = 1; caz <= T; ++caz)
	{
		scanf ("%d\n", &n);
		solve (caz);

		//printf ("\n");


	}


	return 0;
}

