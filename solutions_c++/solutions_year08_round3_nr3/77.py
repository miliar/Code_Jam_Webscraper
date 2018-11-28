#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
using namespace std;

class ProblemC
{
	static const int MOD = 1000000007;
	long long n, m, X, Y, Z;
	vector<long long> A, speed;
public:
	void ReadData()
	{
		cin >> n >> m >> X >> Y >> Z;
		A.resize(m);  for (int i=0; i<m; ++i)  cin >> A[i];
		speed.resize(n);
		for (int i=0; i<n; ++i)
		{
			speed[i] = A[i%m];
			A[i%m] = (X*A[i%m] + Y*(i+1)) % Z;
		}
	}
	void Solve(int nCase)
	{
		ReadData();

		vector<long long> count(n, 1);
		for (int i=1; i<n; ++i)
			for (int j=0; j<i; ++j)
				if (speed[j]<speed[i])  count[i] = (count[i]+count[j]) % MOD;

		cout << "Case #" << nCase << ": " << accumulate(count.begin(), count.end(), 0LL) % MOD << endl;
	}
};

int main()
{
	int N;  string s;  getline(cin, s);  istringstream(s) >> N;
	ProblemC sol;	for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}