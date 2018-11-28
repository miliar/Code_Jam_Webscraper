#include<iostream>
#include<map>
#include<math.h>

using namespace std;

long long convert(int v[], int b, int n)
{
	long long val = 0;
	int j = 0;
	for (int i = n - 1; i >= 0; i--)
	{
		val += (long long) v[i] * pow(b, j);
		j++;
	}
	return val;
}

int main()
{
	int a;
	int b;

	// cout << "Anik";

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		string s;
		cin >> s;
		map<char, int> m;
		int v[s.size()];
		
		v[0]=1;

		int jj = 1;
		m[s[0]] = 2;
		int x = 1;
		for (int j = 1; j < s.size(); j++)
		{
			if (m[s[j]]) v[jj++] = (m[s[j]] - 1);
			else 
			{
				m[s[j]] = x;
				v[jj++] = (m[s[j]] - 1);
				if (x == 1)x+=2;
				else x++;
			}
		}
		int base;
		if (x < 2) {
			base = 2; 
		} else{
		       	base = x - 1;
		}

		cout << "Case #" << i << ": " << convert(v, base, jj) << endl;
		m.clear();
	}
	return 0;
}
