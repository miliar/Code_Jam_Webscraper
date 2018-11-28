#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int countRecycled(int num, int r)
{
	vector<int> digits;
	int tmp = num;
	while(tmp)
	{
		digits.push_back(tmp % 10);
		tmp /= 10;
	}
	reverse(digits.begin(), digits.end());
	int len = digits.size();
	set<int> found;
	for(int start = 0; start < len; start++)
	{
		int cur = digits[start], i;
		for(i = (start + 1) % len; i != start; i = (i + 1) % len)
			cur = cur * 10 + digits[i];
		if (cur > num && cur <= r)
			found.insert(cur);
	}
	return found.size();
}

int main()
{
	int t, a, b;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int cur = 1; cur <= t; cur++)
	{
		cin >> a >> b;
		int ans = 0;
		for(int n = a; n < b; n++)
			ans += countRecycled(n, b);

		printf("Case #%d: %d\n", cur, ans);
		
	}

	return 0;
}