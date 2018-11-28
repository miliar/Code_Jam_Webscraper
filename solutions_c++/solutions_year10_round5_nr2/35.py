#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

int main(void) {
	int testNum;
	cin >> testNum;
	for (int testNo = 1; testNo <= testNum; testNo++) {
		long long L;
		int N;
		cin >> L >> N;
		vector<int> b(N);
		for (int i = 0; i < N; i++) {
			cin >> b[i];
		}
		int maxEl = *max_element(b.begin(), b.end());
		vector<int> bestSol(maxEl, -1);
		bestSol[0] = 0;
		for (int i = 0; i < N; i++) {
			bool addedNew = true;
			while (addedNew) {
				addedNew = false;
				for (int j = 0; j < maxEl; j++) {
					if (bestSol[j] == -1)
						continue;
					int u = j + b[i];
					int d = 0;
					if (u >= maxEl) {
						u -= maxEl;
						d = 1;
					}
					if (bestSol[u] == -1 || bestSol[u] > bestSol[j] + 1 - d) {
						bestSol[u] = bestSol[j] + 1 - d;
						addedNew = true;
					}
				}
			}
		}

		cout << "Case #" << testNo << ": ";
		if (bestSol[L % maxEl] == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << bestSol[L % maxEl] + L / maxEl << endl;
	}
	return 0;
}
