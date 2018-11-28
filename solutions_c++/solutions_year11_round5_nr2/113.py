#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

// Dire Straight

int main()
{
	int cases;
	cin >> cases;

	for (int caseno = 1; caseno <= cases; caseno++) {
		int N;
		cin >> N;
		vector <int> card(10000, 0);
		for (int i = 0; i < N; i++) {
			int c;
			cin >> c;
			card[c - 1]++;
		}
		int ret = 1 << 30;
		for (int i = 0; i < 10000; i++) {
			while (card[i] >= 1) {
				int n = 0;
				int f = card[i];
				for (int j = i; j < 10000; j++) {
					if (card[j] < f) {
						break;
					}
					f = card[j];
					card[j]--;
					n++;
				}
				ret = min(ret, n);
			}
		}
		if (N == 0) {
			ret = 0;
		}
		cout << "Case #" << caseno << ": " << ret << endl;
	}

	return 0;
}
