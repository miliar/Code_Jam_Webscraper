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

int T, N, K;
bool snapper[35];
bool recpow[35];

int main() {
	cin >> T;
	for (int caseid = 1; caseid <= T; caseid++) {
		memset(snapper, 0, sizeof(snapper));
		snapper[0] = true;
		cin >> N >> K;
		bool light;

		// k round toggle
		for (int cnt = 1; cnt <= K; cnt++) {
			// do toggle
			light = true;
			for (int i = 1; i <= N; i++) {
				if (light) {
					light = snapper[i];
					snapper[i] = (snapper[i]?false:true);
				} else {
					light = false;
					break;
				}
			}
		}
		// judge
		light = true;
		for (int i = 1; i <= N; i++) {
			if (snapper[i] == false) {
				light = false;
				break;
			}
		}

		cout << "Case #"<< caseid << (light?": ON":": OFF") << endl;
	}
}
