#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> amount;

string intToStr(int a)
{
	string s = "";
	while (a > 0)
	{
		s = (char)((a%10) + '0') + s;
		a /= 10;
	}
	return s;
}

int main()
{
	int t;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	string s1, s2, min;
	cin >> t;
	char first;
	for (int o = 0; o < t; o++)
	{
		amount.clear();
		cout << "Case #" << o + 1 << ": ";
		int a, b;
		cin >> a >> b;
		for (int i = a; i <= b; i++)
		{		
			s1 = intToStr(i);
			min = s1;
			for (int j = 0; j < s1.size(); j++)
			{
				first = s1[0];
				s1.erase(0,1);
				s1 += first;
				if (s1 < min)
					min = s1;
			}
			amount[min]++;
		}
		int res = 0;
		map<string, int> :: iterator it;
		for (it = amount.begin(); it != amount.end(); it++)
			if (it->second > 1)
			{
				int c = it->second;
				res += c*(c-1)/2;
			}
		cout << res << endl;
	}
	return 0;
}