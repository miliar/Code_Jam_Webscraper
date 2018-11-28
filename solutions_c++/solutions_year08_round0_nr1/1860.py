#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int MaxS = 105;
const int MaxQ = 1005;

class Solution
{
public:
	void Input()
	{
		string input;

		searchEngine_.clear();
		query_.clear();

		cin >> s_;
		for (int i = 0; i < s_; ++i) {			
			getline(cin, input);
			if (input == "")
				getline(cin, input);
			searchEngine_.push_back(input);
		}

		cin >> q_; 
		for (int i = 0; i < q_; ++i) {			
			getline(cin, input);
			if (input == "")
				getline(cin, input);
			query_.push_back(input);
		}

		for (int i = 0; i <= MaxS; ++i) { 
			for (int j = 0; j <= MaxQ; ++j) {
				table_[i][j] = 0;
			}
		}
	}

	void Process()
	{
		int i, j, min = INT_MAX;

		for (j = 1; j <= q_; ++j) {
			for (i = 1; i <= s_; ++i) {			
				if (searchEngine_[i - 1] == query_[j - 1]) {
					table_[i][j] = 10000;
				} else {
					min = INT_MAX;

					for (int k = 1; k <= s_; k++) {
						if (i == k && min > table_[i][j - 1])
							min = table_[i][j - 1];
						else if (min > table_[k][j - 1] + 1)
							min = table_[k][j - 1] + 1;
					}

					table_[i][j] = min;
				}
			}
		}
	}

	void Output()
	{
		int min = INT_MAX;

		for (int i = 1; i <= s_; ++i) {
			if (min > table_[i][query_.size()])
				min = table_[i][query_.size()];
		}

		cout << min << endl;
	}

private:
	int s_, q_;
	vector<string> searchEngine_;
	vector<string> query_;
	int table_[MaxS + 1][MaxQ + 1];
};


int main()
{
	int testCase;
	Solution sol;

	cin >> testCase;

	for (int i = 0; i < testCase; ++i) {
		sol.Input();
		sol.Process();

		cout << "Case #" << i + 1 << ": ";
		sol.Output();
	}

	return 0;
}