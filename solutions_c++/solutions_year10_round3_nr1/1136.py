#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

const char *in = "A-large.in";
const char *out = "A-large.out";

vector<int> ind, A, B;
int T, N, nrsol;

bool cmp( int i, int j)
{
	return A[i] > A[j];
}

int main(void)
{
	freopen(in, "r", stdin);
	freopen(out, "w", stdout);

	scanf ("%d", &T);
	int TT, X, Y, ii;
	size_t i, j;
	nrsol = 0;

	for (TT = 1; TT <= T; ++TT)
	{
		ind.clear();
		A.clear();
		B.clear();
		nrsol = 0;
		scanf ("%d", &N);
		for (ii = 0; ii < N; ++ii)
		{
			scanf ("%d%d", &X, &Y);
			ind.push_back(ii);
			A.push_back(X);
			B.push_back(Y);
		}
		sort( ind.begin(), ind.end(), cmp);
		for (i = 0; i < ind.size(); ++i)
		{
			for (j = i+1; j < ind.size(); ++j)
				if (B[ind[j]] > B[ind[i]]) nrsol++;
		}
		printf ("Case #%d: %d\n", TT, nrsol);
	}
	return 0;
}

