#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <queue>

using namespace std;

const char *in = "C-small-attempt0.in";
const char *out = "C-small.out";

int T, N;
long int R, K;
long int nrsol, val;

int main (void)
{
	freopen (in, "r", stdin);
	freopen (out, "w", stdout);

	scanf ("%d", &T);

	int i, j;
	long int tmp;
	vector<long int>::iterator it;
	for (j = 1; j <= T; ++j)
	{
		queue<long int> g;
		vector <long int> aux;
		nrsol = 0;

		scanf ( "%ld%ld%d", &R, &K, &N);
		for (i = 1; i <= N; ++i)
		{
			scanf ( "%ld", &tmp );
			g.push(tmp);
		}
		while (R)
		{
			val = 0;
			aux.clear();
			while (!g.empty())
			{
				if (g.front() + val > K) break;
				val += g.front();
				aux.push_back ( g.front() );
				g.pop();
			}
			nrsol += val;
			R--;
			for (it = aux.begin(); it != aux.end(); ++it)
				g.push (*it);
		}
		printf ("Case #%d: %ld\n", j, nrsol);
	}
	return 0;
}
