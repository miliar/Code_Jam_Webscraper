#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <bitset>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;

vector <long long> arr;
vector <bool> pr;

void Solve()
{
	long long n;
	cin >> n;
	if(n == 1)
	{
		cout << 0 << endl;
		return;
	}
	long long ans = 0;
	for(int i = 0; i < arr.size() && arr[i] * arr[i] <= n; i++)
	{
		long long x = arr[i] * arr[i];
		while(x <= n)
		{
			ans++;
			x *= arr[i];
		}
	}
	cout << ans + 1 << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	pr.assign(1000002, true);
	for(long long i = 2; i <= 1000000; i++)
		if(pr[i])
			for(long long j = i * i; j <= 1000000; j += i)
				pr[j] = false;
	for(int i = 2; i < 1000002; i++)
		if(pr[i])
			arr.push_back(i);
	for(int tc = 0; tc < t; tc++)
	{
		printf("Case #%d: ", tc + 1);
		Solve();
	}
	return 0;
}