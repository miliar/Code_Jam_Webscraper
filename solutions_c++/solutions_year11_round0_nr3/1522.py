#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void oneCase();

int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": ";
		oneCase();
		cout << endl;
	}

	return 0;
}

void oneCase()
{
	int N;
	cin >> N;

	vector<int> candy(N);
	int total = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> candy[i];
		total ^= candy[i];
	}
	if (total != 0)
	{
		cout << "NO";
		return;
	}

	sort(candy.begin(), candy.end());
	vector<int>::iterator it;
	total = 0;
	for (it = candy.begin() + 1; it != candy.end(); it++)
	{
		total += *it;
	}

	cout << total;
}