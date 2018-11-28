#include <functional>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i)
	{
		int P, K, L;
		cin >> P >> K >> L;

		vector<int> freqs(L);
		for (int j = 0; j < L; ++j)
			cin >> freqs[j];

		long long count = 0;
		sort(freqs.begin(), freqs.end(), greater<int>());
		for (int j = 0; j < L; ++j)
		{
			int mag = 1 + (j / K);
			count += freqs[j] * mag;
		}

		cout << "Case #" << (i + 1) << ": " << count << endl;
	}

	return 0;
}
