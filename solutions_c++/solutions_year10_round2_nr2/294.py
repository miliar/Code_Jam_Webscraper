#include <iostream>

using namespace std;

long long B, T, N, K, X[64], V[64];

int main()
{
	int kases, kase = 0;
	for (cin >> kases; kases; kases--)
	{
		cin >> N >> K >> B >> T;
		for (int i = 0; i < N; i++)
		{
			cin >> X[i];
			X[i] = B - X[i];
		}
		for (int i = 0; i < N; i++)
			cin >> V[i];

		int swaps = 0;
		for (int i = N-1; K > 0 && i >= 0; i--)
		{
			if (T * V[i] >= X[i])
				K--;
			else
				swaps += K;
		}

		cout << "Case #" << ++kase << ": ";
		if (K > 0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << swaps << endl;
	}
	return 0;
}
