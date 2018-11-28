#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
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
using namespace std;
static const double EPS = 1e-8;
typedef long long ll;

int memo[128][128];

int main() {
	//ifstream cin("d.in.txt");

	int N;
	cin >> N;

	for (int testCase = 1; testCase <= N; ++testCase){
		memset(memo, 0, sizeof(memo));

		int H, W, R;
		cin >> H >> W >> R;

		set<pair<int, int> > rocks;
		for (int i = 0; i < R; ++i){
			int x, y;
			cin >> y >> x;
			rocks.insert(make_pair(x, y));
		}

		memo[1][1] = 1;
		for (int x = 2; x <= W; ++x){
			for (int y = 2; y <= H; ++y){
				if (rocks.count(make_pair(x, y))){
					continue;
				}

				memo[x][y] = (memo[x - 2][y - 1] + memo[x - 1][y - 2]) % 10007;
			}
		}

		printf("Case #%d: %d\n", testCase, memo[W][H]);
	}
}
