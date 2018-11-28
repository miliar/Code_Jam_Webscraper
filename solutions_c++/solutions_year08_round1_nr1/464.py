#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; casenum++)
	{
		int n;
		cin >> n;
		vector<int> v1;
		vector<int> v2;
		for (int i = 0; i < n; i++)
		{
			int temp;
			cin >> temp;
			v1.push_back(temp);
		}
		for (int i = 0; i < n; i++)
		{
			int temp;
			cin >> temp;
			v2.push_back(temp);
		}
		sort(v1.begin(), v1.end(), less_equal<int>());
		sort(v2.begin(), v2.end(), greater_equal<int>());
		long res = 0;
		for (int i = 0; i < n; i++)
		{
			res += v1[i] * v2[i];
		}
		cout << "Case #" << casenum << ": " << res << endl;
	}
	return 0;
}