#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
#include <cstring>

using namespace std;
static const double EPS = 1e-8;
typedef long long ll;

static const int MAX = INT_MAX / 3;

int main() {
	int N;
	cin >> N;
	for (int testCase = 1; testCase <= N; ++testCase){
		int M, V;
		cin >> M >> V;

		int memo[16384][2];
		fill_n((int*)memo, 16384 * 2, MAX);

		int gs[16384];
		int changeable[16384];
		for (int i = 1; i <= (M - 1) / 2; ++i){
			cin >> gs[i] >> changeable[i];
		}
		for (int i = (M - 1) / 2 + 1; i <= M; ++i){
			int I;
			cin >> I;
			memo[i][I] = 0;
		}

		for (int i = (M - 1) / 2 ; i > 0; --i){
			for (int left = 0; left < 2; ++left){
				for (int right = 0; right < 2; ++right){
					if (memo[i * 2][left] == MAX || memo[i * 2 + 1][right] == MAX){
						continue;
					}

					if (gs[i] == 0){
						//ORƒQ[ƒg
						memo[i][left | right] = min(memo[i][left | right], memo[i * 2][left] + memo[i * 2 + 1][right]);

						if (changeable[i]){
							//AND
							memo[i][left & right] = min(memo[i][left & right], memo[i * 2][left] + memo[i * 2 + 1][right] + 1);
						}
					} else {
						//AND
						memo[i][left & right] = min(memo[i][left & right], memo[i * 2][left] + memo[i * 2 + 1][right]);

						if (changeable[i]){
							//ORƒQ[ƒg
							memo[i][left | right] = min(memo[i][left | right], memo[i * 2][left] + memo[i * 2 + 1][right] + 1);
						}
					}
				}
			}
		}

		int answer = memo[1][V];

		if (answer == MAX){
			printf("Case #%d: IMPOSSIBLE\n", testCase);
		} else {
			printf("Case #%d: %d\n", testCase, answer);
		}
	}
}
