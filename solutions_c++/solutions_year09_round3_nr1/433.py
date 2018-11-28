#include<iostream>
#include<vector>
#include<map>
#include<math.h>

using namespace std;

long long conv(vector<int> v, int b)
{
	long long val = 0;
	int j = 0;
	for (int i = v.size() - 1; i >= 0; i--)
	{
		val += (long long) v[i] * pow(b, j);
		j++;
	}
	return val;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		vector<int> v;
		string s;
		cin >> s;
		map<char, int> m;
		v.push_back(1);
		m[s[0]] = 2;
		int x = 1;
		for (int j = 1; j < s.size(); j++)
		{
			if (m[s[j]]) v.push_back(m[s[j]] - 1);
			else 
			{
				m[s[j]] = x;
				v.push_back(m[s[j]] - 1);
				if (x == 1)x+=2;
				else x++;
			}
		}
		int base;
		if (x < 2) base = 2; 
		else base = x - 1;
		cout << "Case #" << i << ": " << conv(v, base) << endl;
		m.clear();
	}
	return 0;
}
