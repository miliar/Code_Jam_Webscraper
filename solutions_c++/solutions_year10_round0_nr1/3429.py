#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

const char *in = "A-large.in";
const char *out = "A-large.out";

long int N, K;
int T, TT;

int main (void)
{
	freopen (in, "r", stdin );
	freopen (out, "w", stdout );

	scanf ("%d", &T);
	TT = T;
	for (; T; --T)
	{
		scanf ("%ld%ld", &N, &K);
		printf ("Case #%d: %s\n", TT-T+1, (K % (1L<<N) == (1L<<N)-1) ? "ON" : "OFF" );
	}

	return 0;
}
