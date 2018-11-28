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

string s;
int t;
int a[2000], b[2000];

void main2 ()
{
	cin >> s;

	long long L = 1LL<<((s.size()-1)>>1), V = L*L;
	t = 0;
	for (int i = 0; i < s.size (); i++)
		if (s[i] != '?')
			a[t] = s.size ()-i-1,
			b[t++] = s[i]-'0';
	for (; V < (1LL<<((s.size()-1))); L++)
		V += L+L+1;

//	for (int i = 0; i < t; i++)
//		printf ("%d %d\n", a[i], b[i]);

	for (int i, fnd;; L++)
	{
		fnd = 1;
		for (i = 0; i < t&&fnd; i++)
			if (((V>>a[i])&1)!=b[i])
				fnd=0;

		if (fnd) break;

//		printf ("here L=%I64d, V = %I64d\n", L, V);

		V += L+L+1;
	}

	string res = "";
	for (int i = 0; i < s.size (); i++)
		res += (V&1)+'0',
		V >>= 1;
	reverse (res.begin (), res.end ());
	gout << res << endl;
}

int main ()
{
	scanf ( "%d", &test_num );

	for ( int i = 0; i < test_num; i++ )
		main2 ();

	return 0;
}
