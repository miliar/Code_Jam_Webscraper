#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

using namespace std;

#define TRACE(x) 
#define DEBUG(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f;


int main() {
	int N;
	scanf(" %d", &N);
	for (int _42=1; _42 <= N; _42++) {
		int k;
		char S[50010];
		MSET(S, 0);
		scanf(" %d %s", &k, S);

		vector<int> P;
		for (int i=0; i < k; i++) P.push_back(i);
		int Y = INF;
		char R[50010];
		MSET(R, 0);
		do {
			for (int b=0; b < (int)strlen(S)/k; b++) {
				for (int i=0; i < (int)P.size(); i++) {
					R[b*k+i] = S[b*k+P[i]];
				}
			}
			DEBUG("R = %s\n", R);

			int blocks = 1;
			for (int i=1; i < (int)strlen(R); i++) {
				if (R[i] != R[i-1]) blocks++;
			}
			Y = min(Y, blocks);
		} while (next_permutation(P.begin(), P.end()));

		printf("Case #%d: %d\n", _42, Y);
	}

	return 0;
}

