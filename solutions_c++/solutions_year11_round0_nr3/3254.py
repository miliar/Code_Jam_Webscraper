#include <cstdio>
#include <bitset>
#include <cstring>
#include <string>
#include <algorithm>
#define MAXN 1010

using namespace std;

int N, i, C[MAXN], T;
int main ()
{


	freopen ("candy.in", "r", stdin);
	freopen ("candy.out", "w", stdout);

	int i;
	scanf ("%d\n", &T);
	
	for (int t = 1; t <= T; t++) {
		scanf ("%d", &N);
		int S = 0;
		for (i = 0; i < N; i++) {
			scanf ("%d", &C[i]);
			S ^= C[i];
		}
		if (S != 0) {
			printf ("Case #%d: NO\n", t);
			continue;
		}
		long long res = 0;

		sort (C, C + N);
		for (i = 1; i < N; i++)
			res += C[i];
		printf ("Case #%d: %lld\n", t, res);
		
	}
	return 0;
}
