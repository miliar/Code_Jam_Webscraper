#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;

int n;
string s;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		string s1 = s;
		string s2 = s;
		sort(s1.begin(), s1.end());
		reverse(s1.begin(), s1.end());
		next_permutation(s.begin(), s.end());
		if (s1 == s2)
		{
			s = s1;
			s = s1 + '0';
			for (int i = 0; i < s.size(); i++)
				if (s[i] < s[0] && s[i] != '0')
					swap(s[i], s[0]);
			char c = s[0];
			reverse(s.begin(), s.end());
			s.resize(s.size()-1);
			sort(s.begin(), s.end());
			s = c + s;
		}

		cout << "Case #" << i+1 << ": " << s << endl;
	}

	return 0;
}