#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

char a[550][550];
int aib[550][550];


int n, m;

inline void update (int x, int y)
{
	for (int i = x+1; i <= n+1; i += i & -i)
		for (int j = y+1; j <= m+1; j += j & -j)
			++aib[i][j];
		
}

inline int quer (int x, int y)
{
	int s = 0;
	for (int i = x+1; i ; i -= i & -i)
		for (int j = y+1; j ; j -= j & -j)
			s += aib[i][j];
	return s;
}

inline int query (int x1, int y1, int x2, int y2)
{
	int s = quer (x2, y2) + quer (x1 -1, y1 - 1) - quer (x2, y1-1) - quer (x1 - 1, y2);
	return s;	
}

inline int verif (int x1, int y1, int x2, int y2)
{
	int i, j;
	
	for (i = x1; i <= x2; ++i)
	{
		for (j = y1 + 1; j <= y2; ++j)
			if (a[i][j] != 1 - a[i][j - 1]) return 0;
	}
	
	for (i = y1; i <= y2; ++i)
	{
		for (j = x1 + 1; j <= x2; ++j)
			if (a[j][i] != 1 - a[j-1][i]) return 0;
		
	}
	
	return 1;
	
	
}
void solve (int caz)
{
	int N = min (n, m);
	int i, j, k, t;
	
	memset (aib, 0, sizeof (aib));

	vector <pair <int, int> > sol;
	
	for (; N >= 1; --N)
	{
		int nr = 0;
		
		for (i = 1; i <= n - N + 1; ++i)
			for (j = 1; j <= m - N + 1; ++j)
			{
				if (query (i, j, i + N - 1, j + N - 1)) continue;
				
				if (verif (i, j, i + N - 1, j + N - 1))
				{
					for (k = i ; k < i + N; ++k)
						for (t = j; t < j + N; ++t)
							update (k, t);
					
					++nr;
				}
				
			}
			
			if (nr)
				sol.push_back (make_pair (N, nr));
			//	printf ("%d %d\n", N, nr);
	}

	fprintf (stderr, "Case %d\n", caz);
	printf ("Case #%d: %d\n", caz, sol.size ());
	for (i = 0; i < sol.size (); ++i)
		printf ("%d %d\n", sol[i].first, sol[i].second);
//	printf( "\n");
}


int main ()
{
	freopen ("c.in", "r", stdin);
	freopen ("c.out", "w", stdout);
	int T, i,k,  j, nr;
	char ax[512];
	scanf ("%d\n", &T);
	
	for (int caz = 1; caz <= T; ++caz)
	{
		scanf ("%d %d\n", &n, &m);
		
		for (i = 1; i <= n; ++i)
		{

			memset (ax, 0, sizeof (ax));
			scanf ("%s\n", &ax);
			
			nr = m / 4;
			k = 0;
			
			for (j = 0; j < nr;++j)
			{
				int v = 0;
				
				if (ax[j] >= '0' && ax[j] <= '9')
					v = ax[j] - '0';
				else
					v = 10 + ax[j] - 'A';
				
					for (int t = 4; t >= 1; --t)
						if (v & ( 1 << (t - 1)))
							a[i][++k] = 1;
						else
							a[i][++k] = 0;
				
			}
		
		}
/*
		for (i = 1 ; i <= n; ++i)
		{
			for (j = 1; j <= m; ++j)
				printf ("%d ", a[i][j]);
			printf ("\n");
		}
		
		printf ("\n");
	*/
	
	solve (caz);
	}
	
	return 0;
}