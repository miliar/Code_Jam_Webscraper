// Test.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>

using namespace std;

long long calc (const vector<int>& a, int N, long long t, int L1, int L2)
{
	long long B1 = t, B2 = t;
	long long time = 0;
	for (int i = 0; i < N; i++)
	{
		int d = a[i % a.size()];
		long long tm = d << 1;
		if (i == L1) {
			if (B1 > 0) {
				if (tm > B1)
					tm = B1 + (d - (B1 >> 1));
			}
			else
				tm = d;
		}
		else if (i == L2) {
			if (B2 > 0) {
				if (tm > B2)
					tm = B2 + (d - (B2 >> 1));
			}
			else
				tm = d;
		}
		B1 -= tm; B2 -= tm;
		time += tm;
	}

	return time;
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for (int i = 0; i < numCases; ++i) 
	{
		int L, N, C;
		long long t;
		cin >> L >> t >> N >> C;

		vector<int> a;
		a.resize(C);
		for (int j = 0; j < C; ++j)
			cin >> a[j];

		long long time = -1;
		if (L == 0)
			time = calc(a, N, t, -1, -1);
		else if (L == 1) {
			for (int j = 0; j < N; j++) {
				long long tm = calc(a, N, t, j, -1);
				if (time < 0 || tm < time)
					time = tm;
			}
		}
		else if (L == 2) {
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < N; k++) {
					if (j != k) {
						long long tm = calc(a, N, t, j, k);
						if (time < 0 || tm < time)
							time = tm;
					}
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " << time << endl;
	}
		
	return 0;
}

