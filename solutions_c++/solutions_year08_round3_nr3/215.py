#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
	void MakeSequence()
	{
		unsigned long long i;

		for (i = 0; i < n_; ++i) {
			seq_[i + 1] = A_[i % m_];
			A_[i % m_] = (X_ * A_[i % m_] + Y_ * (i + 1)) % Z_;
		}
	}

	void Input()
	{
		cin >> n_;
		cin >> m_;
		cin >> X_;
		cin >> Y_;
		cin >> Z_;
	
		A_ = vector<unsigned long long>(m_, 0);
		seq_ = vector<unsigned long long>(n_ + 1, 0);

		unsigned long long v;
		for(unsigned long long i = 0; i < m_; ++i) {
			cin >> v;
			A_[i] = v;
		}

		MakeSequence();
	}

	void Process()
	{
		unsigned long long i, j, k;
		unsigned long long count = 0;
		bool cond;
		table_ = vector<vector<unsigned long long>>(n_ + 1, vector<unsigned long long>(n_ + 1, 0));

		for (i = 1; i <= n_; ++i)
			table_[1][i] = 1;

		RowBound_ = n_;

		for (i = 2; i <= n_; ++i) {
			cond = false;
			for (j = i; j <= n_; ++j) {
				count = 0;
				for (k = 1; k < j; ++k) {
					if (seq_[j] > seq_[k]) {
	count = (count + table_[i - 1][k] ) % 1000000007ULL;
					}
				}

				table_[i][j] = count;
				if (count != 0) cond = true;
			}

			if (cond == false) {
				RowBound_ = i;
				break;
			}
		}		
	}

	void Output()
	{
		unsigned long long i, j;
		unsigned long long total = 0;

		for (i = 1; i <= RowBound_; ++ i) {
			for (j = 1; j <= n_; ++j) {
				if (table_[i][j] != 0) {
					total = ( total + table_[i][j] ) % 1000000007ULL;
				}				
			}
		}

		cout << (total % 1000000007ULL);
	}

private:
	unsigned long long n_;
	unsigned long long m_;
	unsigned long long X_;
	unsigned long long Y_;
	unsigned long long Z_;
	unsigned long long RowBound_;	
	vector<unsigned long long> A_;
	vector<unsigned long long> seq_;
	vector<vector<unsigned long long>> table_;
};

int main()
{
	unsigned long long T;
	Solution sol;

	cin >> T;

	for (unsigned long long i = 0; i < T; ++i) {
		sol.Input();
		sol.Process();
		cout << "Case #" << i + 1 << ": ";
		sol.Output();
		cout << endl;
	}

	return 0;
}