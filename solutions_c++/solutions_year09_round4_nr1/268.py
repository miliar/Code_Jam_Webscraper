#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef long long ll;
typedef pair<ll, int> P;

ll mat[50];
int used[50];
int pos[50];

int main() {
	int N;
	cin >> N;
	for(int t = 0; t < N; ++t) {
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) {
			char k;
			mat[i] = 0;
			used[i] = 0;
			for(int j = 0; j < n; ++j) {
				cin >> k;
				mat[i] |= (ll)(k - '0') << j;
			}
			pos[i] = i;
		}
		int res = 0;
		for(int i = 0; i < n; ++i) {
			ll sup = (1LL << (i + 1)) - 1;
			int u = 0;
			for(int j = 0; j < n; ++j) if(mat[j] <= sup && !used[j]) {
				res += abs(pos[j] - i);
				u = j;
				used[j] = true;
				break;
			}
			for(int j = 0; j < u; ++j) ++pos[j];
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}
