#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string apply(string &s, vector<int> &a)
{
	string t = s;
	int k = a.size();
	for(int i = 0; i < s.length(); i+=k)
	{
		for(int j = 0; j < k; ++j)
			t[i+j] = s[i+a[j]];
	}
	return t;
}

int rle(string &s)
{
	int cnt = 1;
	char last = s[0];
	for(int i = 1; i < s.length(); ++i)
		if(last != s[i])
			cnt++,
			last = s[i];
	return cnt;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt; cin >> tt;
	for(int z = 1; z <= tt; ++z)
	{
		int k;
		string s, t;
		cin >> k >> s;
		vector<int> a(k, 0);
		for(int i = 0; i < k; ++i)
			a[i] = i;
		int best = rle(s);
		do
		{
			t = apply(s, a);
			best = min(best, rle(t));
		}while(next_permutation(a.begin(), a.end()));
		printf("Case #%d: %d\n", z, best);
	}
	return 0;
}