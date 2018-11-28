#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main()
{
	int N;
	cin >> N;

	const long long MOD = 1000000007LL;

	for (int i = 0; i < N; ++i)
	{
		long long n, m, X, Y, Z;
		cin >> n >> m >> X >> Y >> Z;

		vector<long long> A(m);
		for (int j = 0; j < m; ++j)
			cin >> A[j];

		vector<long long> B(n);
		for (int j = 0; j < n; ++j)
		{
			B[j] = A[j % m];
			A[j % m] =  (long long)(X * A[j % m] + Y * (j + 1)) % Z;
			assert(B[j] >= 0);
		}

		vector<long long> count(n);
		for (int j = 0; j < n; ++j)
		{
			count[j] = 1;
			for (int k = j - 1; k >= 0; --k)
			{
				if (B[j] > B[k])
					count[j] += count[k];
			}
			count[j] %= MOD;
			assert(count[j] > 0);
		}

		long long sum = accumulate(count.begin(), count.end(), 0LL);

		cout << "Case #" << (i + 1) << ": " << (sum % MOD) << endl;
	}

	return 0;
}
