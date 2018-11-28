#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution
{
public:
	void Input()
	{
		int i, x, y;
		cin >> n_ >> m_;

		customer_.clear();
		success_ = false;

		for (i = 0; i < m_; ++i) {
			int T;
			vector<pair<int, int>> customer;

			customer.clear();
			cin >> T;

			for (int j = 0; j < T; ++j) {
				pair<int, int> p;
				cin >> x >> y;

				p.first = x;
				p.second = y;
				
				customer.push_back(p);
			}

			customer_.push_back(customer);
		}
	}

	static bool less(vector<pair<int, int>> a, vector<pair<int, int>> b)
	{
		if (a.size() < b.size())
			return true;

		return false;
	}

	static bool less2(pair<int, int> p1, pair<int, int> p2)
	{
		if (p1.second == 0 && p2.second == 0) {
			if (p1.first < p2.first)
				return true;
			else 
				return false;
		} else {
			if (p1.second == 0)
				return true;
			else
				return false;
		}

		return false;
	}

	void Backtracking(int m)
	{
		int i;

		if (m >= m_) {
			success_ = true;
			return;
		}

		for (i = 0; i < customer_[m].size(); ++i) {
			int index, value;
			index = customer_[m][i].first - 1;
			value = customer_[m][i].second;

			if (milkshake_[index] == -1) {
				milkshake_[index] = value;
				Backtracking(m + 1);
				if (success_ == true) return;
				milkshake_[index] = -1;
			} else if (milkshake_[index] == value) {
				Backtracking(m + 1);
				if (success_ == true) return;
			}
		}
	}

	void Process()
	{
		sort(customer_.begin(), customer_.end(), less);

		for (int i = 0; i < customer_.size(); ++i)
			sort(customer_[i].begin(), customer_[i].end(), less2);

		milkshake_ = vector<int>(n_, -1);

		Backtracking(0);
	}

	void Output()
	{
		int i;

		if (!success_) {
			cout << "IMPOSSIBLE";
		} else {
			for (i = 0; i < n_; ++i) {
				if (milkshake_[i] == -1)
					cout << "0 ";
				else 
					cout << milkshake_[i] << " ";
			}		
		}
	}

private:
	vector<vector<pair<int, int>>> customer_;
	vector<int> milkshake_;
	int n_, m_;
	bool success_;
};

int main()
{
	int T;
	Solution sol;

	cin >> T;

	for (int i = 0; i < T; ++i) {
		sol.Input();
		sol.Process();
		cout << "Case #" << i + 1 << ": ";
		sol.Output();
		cout << endl;
	}

	return 0;
}