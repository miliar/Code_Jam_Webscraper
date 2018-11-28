#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	vector <int> s;
	int n;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		int k;
		string str;
		cin >> str;
		k = str.length();
		s.clear();
	//	s.resize(str.length());
		for(int j = 0; j < str.length(); j++)
			s.push_back(str[j] - '0');
		string ans;
	//	str.clear();
		if(next_permutation(s.begin(), s.end()))
			for(int j = 0; j < k; j++)
				ans.push_back(s[j] + '0');
		else
		{
			int m = 10;
			for(int j = 0; j < k; j++)
				if(s[j] != 0)
					m = min(m, s[j]);
			for(int j = 0; j < k; j++)
				if(s[j] == m)
				{
					for(int x = j + 1; x < k; x++)
						s[x - 1] = s[x];
					break;
				}
			sort(s.begin(), s.end() - 1);
			ans.push_back(m + '0');
			ans.push_back('0');
			for(int j = 0; j < k - 1; j++)
				ans += s[j] + '0';
		}
		printf("Case #%d: ", i + 1);
		cout << ans << endl;
	}
	return 0;
}