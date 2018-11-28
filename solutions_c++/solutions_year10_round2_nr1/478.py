//Solution by Ali-Amir Aldan
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>

#define forn(i, n) for (int (i); (i) < (n); (i)++ )
#define betw(a, b, c) ((a) <= (c) && (b) >= (c))
#define pb push_back
#define mp make_pair
#define ss second
#define ff first

typedef long long ll;
typedef long double ld;

int	fx[] = {-1, 0, +1, 0}, fy[] = {0, +1, 0, -1},
	ex[] = {-1, -1, 0, +1, +1, +1, 0, -1}, ey[] = {0, +1, +1, +1, 0, -1, -1, -1};

using namespace std;

map <string, bool> is;
string t;
int T, case_number;
int n, m, cnt;
char s[200];

#define gout case_number++, printf("Case #%d: ",case_number), cout

void main2 ()
{
	scanf ( "%d%d", &n, &m );
	cnt = 0; is[""] = 1;
	for ( int i = 0; i < n; i++ )
	{
		scanf ( "%s", s );
		t = "";
		for ( int j = 0; j < strlen (s); j++ )
		{
			if (s[j] == '/') is[t] = 1;
			t += s[j];
		}
		is[t] = 1;
	}
	for ( int i = 0; i < m; i++ )
	{
		scanf ( "%s", s );
		t = "";
		for ( int j = 0; j < strlen (s); j++ )
		{
			if (s[j] == '/')
			{
//				cout << "asd " << t << "\n";
//				printf ( "bef %d\n", cnt );
				if (!is[t]) cnt++;
//				printf ( "aft %d\n", cnt );
				is[t] = 1;
			}
			t += s[j];
		}
//		cout << "here " << t << "\n";
//		printf ( "%d\n", cnt );
		if (!is[t]) cnt++;
		is[t] = 1;
	}
	gout << cnt << "\n";
	is.clear ();
}

int main ()
{
	freopen ( "a.in", "r", stdin );
	freopen ( "a.out", "w", stdout );

	scanf ( "%d", &T );

	for ( int i = 0; i < T; i++ )
		main2 ();

	return 0;
}
