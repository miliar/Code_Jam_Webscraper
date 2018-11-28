#include <cstdio>
#include <cstring>
using namespace std;

const int MAX_N   = 128;
const int MAX_M   = 1024;
const int MAX_LEN = 1024;

int n, m;
char A[MAX_N][MAX_LEN];
char B[MAX_M][MAX_LEN];

void input ()
{
	int i;

	scanf ("%d\n", &n);
	for (i=0; i<n; i++)
		gets (A[i]);

	scanf ("%d\n", &m);
	for (i=0; i<m; i++)
		gets (B[i]);
}

void solve ()
{
	int i, j, lo, engine, maxpos, ans;
	
	for (lo=0, ans=0; lo<m; ans++) {
		maxpos=-1;
		for (i=0; i<n; i++) { // every name
			for (j=lo; j<m; j++) // in every query
				if ( strcmp(A[i],B[j])==0 ) {
					if (j>maxpos) maxpos=j;
					break;
				}

			if (j==m) {
				maxpos=m;
				break;
			}
		}

		lo=maxpos;
	}

	if (ans-1<0) ans++;

	printf ("%d\n", ans-1);
}

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int t, i;

	scanf ("%d", &t);

  	for (i=1; i<=t; i++) {
		input ();
		printf ("Case #%d: ", i);
		solve ();
	}

	return 0;
}
