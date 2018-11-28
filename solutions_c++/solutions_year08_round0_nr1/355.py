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

int MEMO[128][1024];

int main() {
	//ifstream cin("a.in.txt");

	int N;
	cin >> N;
	for (int testCase = 1; testCase <= N; ++testCase){
		vector<int> conflicts;

		int S;
		cin >> S;
		map<string, int> queries;

		string dummy;
		getline(cin, dummy);

		for (int i = 0; i < S; ++i){
			string s;
			getline(cin, s);
			queries.insert(make_pair(s, i));
		}

		int Q;
		cin >> Q;
		getline(cin, dummy);
		for (int i = 0; i < Q; ++i){
			string q;
			getline(cin, q);

			if (queries.count(q)){
				conflicts.push_back(queries[q]);
			}
		}

		conflicts.erase(unique(conflicts.begin(), conflicts.end()), conflicts.end());

		if (conflicts.size() <= 1){
			printf("Case #%d: %d\n", testCase, 0);
			continue;
		}

		//DP
		fill_n((int*)MEMO, 128 * 1024, INT_MAX / 2);
		for (int i = 0; i < S; ++i){
			if (conflicts[0] != i){
				MEMO[i][0] = 0;
			}
		}

		for (int queryIndex = 1; queryIndex < conflicts.size(); ++queryIndex){
			for (int searchIndex = 0; searchIndex < S; ++searchIndex){
				if (conflicts[queryIndex] == searchIndex){
					continue;
				}

				for (int prevSearchIndex = 0; prevSearchIndex < S; ++prevSearchIndex){
					int& memo = MEMO[searchIndex][queryIndex];
					memo = min(memo, MEMO[prevSearchIndex][queryIndex - 1] + ((searchIndex == prevSearchIndex) ? 0 : 1));
				}
			}

			//for (int i = 0; i < S; ++i){
			//	for (int q = 0; q <= queryIndex; ++q){
			//		if (MEMO[i][q] == INT_MAX / 2){
			//			cout << "- ";
			//			continue;
			//		}
			//		cout << MEMO[i][q] << " ";
			//	}
			//	cout << endl;
			//}
			//cout << endl;
		}

		int answer = INT_MAX;
		for (int i = 0; i < S; ++i){
			answer = min(answer, MEMO[i][conflicts.size() - 1]);
		}

		printf("Case #%d: %d\n", testCase, answer);
	}
}
