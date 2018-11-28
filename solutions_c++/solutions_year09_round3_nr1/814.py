#include <iostream>
#include <sstream>
#include <string>
#include <map>
using namespace std;

long long pow(int a, int b)
{
	long long r = 1;
	for (int i = 0; i < b; i++)
		r *= a;
	return r;
}

int main()
{
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; testcase++)
	{
		string s;
		cin >> s;
		map<char, int> m;
		m[s[0]] = 1;
		int i = 1, j = 2, l = s.length();
		while (i < l && s[i] == s[0]) i++;
		m[s[i++]] = 0;
		for (; i < l; i++)
			if (m.find(s[i]) == m.end())
				m[s[i]] = j++;
		
		long long n = 0;
		for (int k = 0; k < l; k++)
			n += m[s[l - k - 1]] * pow(j, k);
		cout << "Case #" << testcase << ": " << n << endl;
	}
	return 0;
}
