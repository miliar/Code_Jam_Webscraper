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

vector <char> v;
string s;
int C, D, n, col, t;
int q[2000000];
int a[256][256], b[256][256], ch[256][256];

void main2 ()
{
	scanf ("%d", &C);
	col++;

	for (int i = 0; i < C; i++)
	{
		cin >> s;
		a[s[0]][s[1]] = a[s[1]][s[0]] = col;
		ch[s[0]][s[1]] = ch[s[1]][s[0]] = s[2];
	}

	scanf ("%d", &D);

	for (int i = 0; i < D; i++)
	{
	 	cin >> s;
	 	b[s[0]][s[1]] = b[s[1]][s[0]] = col;
	}

	scanf ("%d", &n);

	cin >> s;

	t = 0;
	for (int i = 0; i < n; i++)
		q[++t] = s[n-i-1];
	v.resize (0);
	for (int last = 0, x; t;)
	{
		if (!v.size ())
			v.push_back (q[t--]);
		else
		if (a[v.back ()][q[t]] == col)
			x = ch[v.back ()][q[t]],
			q[t] = x,
			v.pop_back ();
		else
		{
			int ok = 1;
		 	for (int i = 0; i < v.size (); i++)
		 		if (b[v[i]][q[t]] == col)
		 			ok = 0;
		 	if (!ok)
		 		v.resize (0);
		 	else
		 		v.push_back (q[t]);
			t--;
		}
	}

	gout;

	printf ("[");
	for (int i = 0; i < v.size (); i++)
	{
	 	printf ("%c", v[i]);
	 	if (i+1<v.size ())
	 		printf (", ");
	}

	puts ("]");
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
