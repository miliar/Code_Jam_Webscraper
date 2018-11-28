#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> X, Y;

long long solve()
{
	vector<int> pX, nX, pY, nY;

	for (int i = 0; i < N; i++)
		if (X[i] > 0)
			pX.push_back(X[i]);
		else
			nX.push_back(X[i]);

	for (int i = 0; i < N; i++)
		if (Y[i] > 0)
			pY.push_back(Y[i]);
		else
			nY.push_back(Y[i]);

	sort(pX.begin(), pX.end());
	sort(nX.begin(), nX.end());
	sort(pY.begin(), pY.end());
	sort(nY.begin(), nY.end());

	long long res = 0;
	while (pX.size() > 0 && nY.size() > 0)
	{
		res += (long long) pX[pX.size() - 1] * nY[0];
		pX.erase(pX.begin() + pX.size() - 1);
		nY.erase(nY.begin());
	}

	while (pY.size() > 0 && nX.size() > 0)
	{
		res += (long long) pY[pY.size() - 1] * nX[0];
		pY.erase(pY.begin() + pY.size() - 1);
		nX.erase(nX.begin());
	}

	vector<int> A, B;

	A = pX;
	for (int i = 0; i < nX.size(); i++)
		A.push_back(nX[i]);

	B = pY;
	for (int i = 0; i < nY.size(); i++)
		B.push_back(nY[i]);

	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	
	if (!A.size())
		return res;

	for (int i = 0; i < A.size(); i++)
		res += (long long) A[i] * B[B.size() - i - 1];

	return res;
}	


void readAndSolve()
{
	int T;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &N);
		X.clear(), Y.clear();
		int nr;
		for (int j = 0; j < N; j++)
		{
			scanf("%d", &nr);
			X.push_back(nr);
		}

		for (int j = 0; j < N; j++)
		{
			scanf("%d", &nr);
			Y.push_back(nr);
		}

		printf("Case #%d: %d\n", i + 1, solve());
	}
}

int main()
{
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small-attempt3.out", "w", stdout);

	readAndSolve();

	return 0;
}