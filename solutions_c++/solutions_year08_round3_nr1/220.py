#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;

class Solution 
{
public:
	void Input()
	{
		cin >> p_;
		cin >> k_;
		cin >> l_;

		table_ = vector<vector<long long>>(k_, vector<long long>(p_, 0));
		input_.clear();
		cnt_ = 0;

		int v;
		for (int i = 0; i < l_; ++i) {
			cin >> v;
			input_.push_back(v);
		}
	}

	void Process()
	{
		sort(input_.begin(), input_.end(), greater<long long>());

		for (int j = 0; j < p_; ++j) {
			for (int i = 0; i < k_; ++i) {
				if (cnt_ >= input_.size())
					return;
				table_[i][j] = input_[cnt_++];
			}
		}
	}

	void Output()
	{
		long long result = 0;

		if (cnt_ < input_.size()) {
			cout << "Impossible";
		} else {
			for (int i = 0; i < k_; ++i) {
				for (int j = 0; j < p_; ++j) {
					result += table_[i][j] * (j + 1);
				}
			}
			cout << result;
		}
	}

private:
	int p_;
	int k_;
	int l_;
	int cnt_;
	vector< vector<long long>> table_;
	vector<int> input_;	
};

int main()
{
	Solution sol;
	int N;

	cin >> N;
	for (int i = 0; i < N; ++i) {
		sol.Input();
		sol.Process();
		cout << "Case #" << i + 1 << ": ";
		sol.Output();
		cout << endl;
	}

	return 0;
}