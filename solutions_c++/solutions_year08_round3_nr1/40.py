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

int main() {
	int N;
	cin >> N;
	for (int testCase = 1; testCase <= N; ++testCase){
		int P, K, L;
		cin >> P >> K >> L;

		vector<int> ls;
		for (int i = 0; i < L; ++i){
			int in;
			cin >> in;
			ls.push_back(in);
		}

		sort(ls.begin(), ls.end(), greater<int>());

		ll answer = 0;
		for (int i = 0; i < L; ++i){
			answer += ls[i] * (i / K + 1);
		}

		cout << "Case #" << testCase << ": " << answer << endl;
	}

}
