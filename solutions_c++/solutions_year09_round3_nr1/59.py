#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

map <char, int> biect;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		biect.clear();
		string s;
		cin >> s;
		int n = s.length();
		biect[s[0]] = 1;
		int now = 0;
		for(int j = 1; j < n; j++)
		{
			if(biect.find(s[j]) == biect.end())
				biect[s[j]] = now++;
			if(now == 1)
				now++;
		}
		now = max(now, 2);
		long long ans = 0;
		for(int j = 0; j < n; j++)
		{
			ans *= now;
			ans += biect[s[j]];
		}
		printf("Case #%d: ", i + 1);
		cout << ans << endl;
	}
	return 0;
}