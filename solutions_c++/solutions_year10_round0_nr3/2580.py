#include <assert.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <climits>
#include <cmath>
#include <time.h>
#include <iomanip>

using namespace std;

int T, R, K, N;
int g[1005], next[1005], sum[1005];

int main() {
	int p = 0;
	unsigned long long total = 0;
	cin >> T;
	for (int caseid = 1; caseid <= T; caseid++) {
		cin >> R >> K >> N;
		for (int i = 0; i < N; i++) {
			cin >> g[i];
		}
		memset(next, 0, sizeof(next));
		memset(sum, 0, sizeof(sum));

		// compute next[] and sum[]
		for (int i = 0; i < N; i++) {
			p = i; total = 0;
			int remain = K;
			bool first = true;
			// find the next point not exceed K
			while (remain - g[p] >= 0 && (p != i || first) ){
				first = false;

				total += g[p];
				remain -= g[p];
				p++;
				p %= N;
			}
			next[i] = p;
			sum[i] = total;
		}

		// compute total
		total = 0; p = 0;
		for (int r = 1; r <= R; r++) {
			total += sum[p];
			p = next[p];
		}
		// output result
		cout << "Case #" << caseid << ": " << total << endl;
	}
}
