#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <climits>

using namespace std;

const int MaxN = 55;
const double eps = 1e-7;

int firstPos[MaxN];
int runs, N, K, B, T;
int v[MaxN], x[MaxN];
bool toRemove[MaxN];

int main()
{
	freopen("b_large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);

	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> N >> K >> B >> T;
		for (int i = 0; i < N; ++i)
			cin >> x[i];
		for (int i = 0; i < N; ++i)
			cin >> v[i];

		int cntPay = 0;
		int totalReached = 0;
		int totalPay = 0;
		memset(toRemove, 0, sizeof toRemove);
		if (K > 0)
		while (1)
		{
			memset(firstPos, -1, sizeof firstPos);
			for (int i = 0; i < N; ++i)
			{
				if (toRemove[i]) continue;
				double min = INT_MAX;
				for (int j = i+1; j < N; ++j)
				{
					if (toRemove[j]) continue;
					if (v[i] <= v[j]) continue;
					double dis = (double)(x[j] - x[i]) / (v[i] - v[j]) + x[i];
					if (dis >= B - eps) continue;
					if (dis < min)
					{
						min = dis;
						firstPos[i] = j;
					}
				}
			}

			for (int i = 0; i < N; ++i)
				if (!toRemove[i] && firstPos[i] == -1 && (double)(B - x[i]) / v[i] <= T + eps)
				{
					toRemove[i] = true;
					totalReached++;
					totalPay += cntPay;
					if (totalReached == K) break;
				}

			//for (int i = 0; i < N; ++i)
			//	cout << toRemove[i] << " ";
			//cout << endl << totalReached << " " << totalPay << endl;

			while (totalReached < K)
			{
				bool change = false;
				for (int i = 0; i < N; ++i)
					if (!toRemove[i] && firstPos[i] != -1 && (double)(B - x[i]) / v[i] <= T + eps && toRemove[firstPos[i]])
					{
						toRemove[i] = true;
						change = true;
						totalReached++;
						totalPay += cntPay;
						if (totalReached == K) break;
					}
				if (!change) break;
			}
			if (totalReached == K) break;

		//	for (int i = 0; i < N; ++i)
		//		cout << toRemove[i] << " ";
		//	cout << endl << totalReached << " " << totalPay << endl;

			bool change = false;
			for (int i = N-1; i >= 0; --i)
				if (!toRemove[i])
				{
					toRemove[i] = true;
					cntPay++;
					change = true;
					break;
				}
			if (!change) break;
		//	for (int i = 0; i < N; ++i)
		//		cout << toRemove[i] << " ";
		//	cout << endl << totalReached << " " << totalPay << endl;
		}

//		cout << " K = " << K << " " << endl;
		cout << "Case #" << run << ": ";
		if (totalReached < K)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << totalPay << endl;
	}
}
