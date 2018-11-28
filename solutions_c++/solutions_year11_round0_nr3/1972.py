#include <iostream>

#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		cout << "Case #" << caseNum << ": ";

		int N, xorAcc = 0, total = 0, smallest = 2000000;
		vector<int> candy;
		cin >> N;
		for (int j = 0; j < N; ++j)
		{
			int c;
			cin >> c;
			candy.push_back(c);

			xorAcc ^= c;
			total += c;
			smallest = min(smallest, c);
		}

		if (xorAcc)
			cout << "NO";
		else
			cout << total - smallest;

		cout << endl;
	}
	return 0;
}
