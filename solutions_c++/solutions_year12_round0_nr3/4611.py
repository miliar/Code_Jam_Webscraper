#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<vector>
#include<algorithm>
using namespace std;

bool check(int a, int b)
{
	ostringstream oss1, oss2;
	oss1 << a;
	oss2 << b;
	string s1 = oss1.str();
	string s2 = oss2.str();
	if(s1 == s2)
		return true;
	for(int i = 0; i < s1.size() && s1.size() > 1; ++i)
	{
		//cout << s1 << ' ' << s2 << endl;
		rotate(s1.begin(), s1.begin() + 1, s1.end());  
		if(s1 == s2)
			return true;
	}
	return false;
}

int solve(int a, int b)
{
	int ans = 0;
	for(int i = a; i <= b; ++i)
		for(int j = i + 1; j <= b; ++j)
			if(check(i, j)) ans++;
	return ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	cin >> n;
	int a, b;
	for(int i = 0; i < n; ++i)
	{
		cin >> a >> b;
		cout << "Case #" << i + 1 << ": " << solve(a, b) << endl;
	}
	return 0;
}