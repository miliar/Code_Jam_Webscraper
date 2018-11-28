#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;


int N;


void solve(int INDEX)
{
	int n;
	vector<int> v1, v2;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int t1;
		cin >> t1;
		v1.push_back(t1);
	}
	for (int i = 0; i < n; i++)
	{
		int t1;
		cin >> t1;
		v2.push_back(t1);
	}
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	int i = 0;
	int res = 0;
	while (i < n && v1[i] < 0 && v2[n - 1 - i] > 0)
	{
		res += v1[i] * v2[n - 1 - i];
		i++;
	}
	int j = 0;
	while (j < n && v2[j] < 0 && v1[n - 1 - j] > 0)
	{
		res += v2[j] * v1[n - 1 - j];
		j++;
	}
	for (int ii = i; ii + j < n; ii++)
	{
		res += v1[ii] * v2[n - ii - 1];
	}

	cout << "Case #" <<INDEX + 1 << ": " << res << endl;
}


int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> N;
	for (int i = 0; i < N; i++)
		solve(i);
	fclose(stdin);
	fclose(stdout);
	return 0;
}