#include <climits>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

#define foreach(iter, cont) \
	for (typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)

bool solve (int n, int k)
{
	return ((k + 1) % (1 << n)) == 0;
}

int main()
{
	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; i++) {
		int N, K;
		scanf ("%d %d", &N, &K);
		printf ("Case #%d: %s\n", i, solve (N, K) ? "ON" : "OFF");
	}
	return 0;
}
