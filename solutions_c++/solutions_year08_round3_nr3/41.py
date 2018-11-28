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
static const double EPS = 1e-5;
typedef long long ll;

ll memo[500010];
ll values[500010];

int main() {
	int N;
	cin >> N;

	for (int testCase = 1; testCase <= N; ++testCase){
		ll n, m, X, Y, Z, A[128];
		cin >> n >> m >> X >> Y >> Z;

		for (int i = 0; i < m; ++i){
			cin >> A[i];
		}

		memset(memo, 0, sizeof(memo));

		for (int i = 0; i < n; ++i){
			values[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
		}

		for (int i = 0; i < n; ++i){
			for (int from = 0; from < i; ++from){
				if (values[i] > values[from]){
					memo[i] += memo[from];
				}
			}

			++memo[i];
			memo[i] %= 1000000007;
		}

		ll answer = 0;
		for (int i = 0; i < n; ++i){
			answer += memo[i];
			answer %= 1000000007;
		}

		printf("Case #%d: %d\n", testCase, (int)answer);
	}
}
