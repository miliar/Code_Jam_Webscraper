#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution 
{
public:
	int InnerProduct(vector<int> v, vector<int> w)
	{
		int result = 0;

		for (int i = 0; i < v.size(); ++i)
			result += v[i] * w[i];

		return result;
	}

	void Input()
	{
		int value;

		cin >> n_;

		v_.clear();
		w_.clear();

		for (int i = 0; i < n_; ++i) {
			cin >> value;
			v_.push_back(value);
		}

		for (int i = 0; i < n_; ++i) {
			cin >> value;
			w_.push_back(value);
		}
	}

	void Process()
	{
		sort(v_.begin(), v_.end(), greater<int>());
		sort(w_.begin(), w_.end(), less<int>());
	}

	void Output()
	{
		cout << InnerProduct(v_, w_);
	}

private:
	int n_;
	vector<int> v_;
	vector<int> w_;	
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