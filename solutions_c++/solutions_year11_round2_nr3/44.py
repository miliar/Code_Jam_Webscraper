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

int n, m, col, res;
int u[200], v[200], room[200000], cnt[200], color[200], anscol[200];

int proc (int i, int j, int mask)
{
	int ret = 0;

	for (; i != j; i = (i+1)%n)
		ret |= (1<<i)&mask;
	ret |= 1<<j;

	return ret;
}

void assignrooms (int mask)
{
//	cerr << "entered " << mask << endl;
	int div1 = 0, div2 = 0, cnt=0;

	for (int i = 0; i < m; i++)
		if ((mask>>u[i])&1)
		if ((mask>>v[i])&1)
		{
			div1 = proc (u[i], v[i], mask);
			div2 = proc (v[i], u[i], mask);

			if (div1 != mask && div2 != mask)
			{
				cnt++;
				assignrooms (div1);
				assignrooms (div2);
            }
		}

	if (!cnt)
	{
		room[col++] = mask;
	}
//	cerr << "exited\n" << endl;
}

void dfs (int u)
{
	if (u == n)
	{
		int j = n-1;
		for (; !cnt[j]; j--);
		if (res > j) return;
		for (int i = 0; i < j; i++)
			if (!cnt[i]) return;
		for (int i = 0, k, msk; i < col; i++)
		{
			msk = 0;
			for (k = 0; k < n; k++)
				if ((room[i]>>k)&1)
					msk|=1<<color[k];
			if (msk!=(1<<(j+1))-1) return;
		}
		res = j+1;
		for (int i = 0; i < n; i++)
			anscol[i] = color[i];

		return;
	}
	for (int i = 0; i < n; i++)
	{
		color[u] = i;
		cnt[i]++;

		dfs (u+1);

		cnt[i]--;
	}
}

void main2 ()
{
	scanf ("%d%d", &n, &m);

	for (int i = 0; i < m; i++)
		scanf ("%d", &u[i]),
		u[i]--;
	for (int i = 0; i < m; i++)
		scanf ("%d", &v[i]),
		v[i]--;

	col = 0; res = 0;
	assignrooms ((1<<n)-1);

//	printf ("here col = %d\n", col);
//	for (int i = 0; i < col; i++)
//		printf ("%d\n", room[i]);
//	puts ("");
	dfs (0);

	gout << res << endl;
	for (int i = 0; i < n; i++)
		printf ("%d%c", anscol[i]+1, i+1==n?'\n':' ');
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
