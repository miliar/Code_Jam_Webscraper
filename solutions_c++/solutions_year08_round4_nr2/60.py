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

int main() {
	int C;
	cin >> C;

	for (int testCase = 1; testCase <= C; ++testCase){
		int N, M, A;
		cin >> N >> M >> A;

		vector<int> answer;
		for (int x2 = 0; x2 <= N && answer.empty(); ++x2){
			for (int y2 = 0; y2 <= M && answer.empty(); ++y2){
				for (int x3 = 0; x3 <= N && answer.empty(); ++x3){
					for (int y3 = 0; y3 <= M && answer.empty(); ++y3){
						if (abs(x2 * y3 - y2 * x3) == A){
							answer.push_back(x2);
							answer.push_back(y2);
							answer.push_back(x3);
							answer.push_back(y3);
						}
					}
				}
			}
		}

		if (answer.empty()){
			printf("Case #%d: IMPOSSIBLE\n", testCase);
		} else {
			printf("Case #%d: 0 0 %d %d %d %d\n", testCase, answer[0], answer[1], answer[2], answer[3]);
		}
	}
}
