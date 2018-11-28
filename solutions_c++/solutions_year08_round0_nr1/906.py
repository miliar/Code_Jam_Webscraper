#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int dp[100];

int solve(int s, const vector<int>& queries)
{
	int q = queries.size();
	int result = 0;

	vector<int> was(s, 0);
	int rem = s;

	for (int i = 0; i < q; ++i) {
		if (was[queries[i]] == 0) {
			was[queries[i]] = 1;
			--rem;
			if (rem == 0) {
				++result;
				was.assign(s, 0); was[queries[i]] = 1; rem = s - 1;
			}
		}
	}

	return result;
}

int main()
{
	int tests, s, q;
	map<string, int> engines;
	//vector<string> engine_names;
	string engine, tmp;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		vector<int> queries;
		
		cin >> s;
		getline(cin, tmp);
		
		for (int i = 0; i < s; ++i) {
			getline(cin, engine);
			engines[engine] = i;
			//engine_names.push_back(engine);
		}
		//getline(cin, tmp);
		
		cin >> q;
		getline(cin, tmp);

		for (int i = 0; i < q; ++i) {
			getline(cin, engine);
			queries.push_back(engines.find(engine)->second);
		}
		//getline(cin, tmp);

		cout << "Case #" << (test + 1) << ": " << solve(s, queries) << endl;
	}
	return 0;
}
