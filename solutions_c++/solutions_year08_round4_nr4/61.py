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
	int N;
	cin >> N;
	for (int testCase = 1; testCase <= N; ++testCase){
		int k;
		cin >> k;

		string in;
		getline(cin, in);
		getline(cin, in);

		vector<int> p;
		for (int i = 0; i < k; ++i){
			p.push_back(i);
		}

		int answer = INT_MAX;
		do {
			char after[1024];
			memset(after, 0, sizeof(after));
			for (int offset = 0; offset < in.size(); offset += k){
				for (int i = 0; i < k; ++i){
					after[offset + i] = in[offset + p[i]];
				}
			}

			char last = 0;
			int temp = 0;
			for (int i = 0; i < in.size(); ++i){
				temp += (last != after[i] ? 1 : 0);
				last = after[i];
			}

			answer = min(answer, temp);
		} while (next_permutation(p.begin(), p.end()));

		printf("Case #%d: %d\n", testCase, answer);
	}
}
