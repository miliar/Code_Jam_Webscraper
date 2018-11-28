#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

const int MaxN = 1005;

int x[MaxN], y[MaxN];
int N;
int runs;

int main()
{
	freopen("a_large.in", "r", stdin);
	freopen("a_large.out", "w", stdout);
	
	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> x[i] >> y[i];

		int sum = 0;
		for (int i = 0; i < N; ++i)
			for (int j = i+1; j < N; ++j)
				if (x[i] > x[j] && y[i] < y[j] || x[j] > x[i] && y[j] < y[i])
					sum++;
		cout << "Case #" << run << ": " << sum << endl;
	}
}
