#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 1024;

int p, k, n;
int A[MAX_N];
int ans;

void input ()
{
	int i;

	cin >> p >> k >> n;

	for (i=0; i<n; i++)
		cin >> A[i];

	sort (A,A+n);
	reverse (A,A+n);
}

void solve ()
{
	int i, j, t;

	ans=0;

	for (i=1, t=0; t<n; i++, t+=k)
		for (j=0; j<k && t+j<n; j++)
			ans += i*A[t+j];
}

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int i, t;
	cin >> t;

	for (i=1; i<=t; i++) {
		input ();
		solve ();

		printf ("Case #%d: %d\n", i, ans);
	}
	
	return 0;
}
