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

long long solve (int r, int k, int n)
{
	int group[n];
	for (int i = 0; i < n; i++)
		scanf ("%d", &group[i]);

	long long sum = 0;
	for (int i = 0; i < n; i++)
		sum += group[i];
	if (sum <= k)
		return ((long long) sum) * r;

	long long	res = 0;
	long long	before[n];
	int			round[n];
	for (int i = 0; i < n; i++)
		before[i] = -1;

	int head = 0;
	int rnd = 0;
	while (rnd < r) {
		if (before[head] != -1 && (r - rnd) >= (rnd - round[head])) {
			long long w = res - before[head];
			int l = rnd - round[head];
			int c = (r - rnd) / l;
			assert (l > 0);
			assert (c > 0);
			rnd += c * l;
			res += c * w;
		} else {
			before[head] = res;
			round[head] = rnd;

			long long step = 0;
			int next = head;
			while (step + group[next] <= k) {
				step += group[next];
				next = (next + 1) % n;
			}

			res += step;
			head = next;
			rnd++;
		}
	}

	return res;
}

int main ()
{
	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; i++) {
		int R, k, N;
		scanf ("%d %d %d", &R, &k, &N);
		printf ("Case #%d: %Ld\n", i, solve (R, k, N));
	}
	return 0;
}
