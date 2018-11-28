#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
#include <set>
#include <stack>
#include <map>
#include <queue>
using namespace std;

string fileName = "B-large";
int main()
{
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);

	int test;
	cin >> test;
	for (int cas = 1; cas <= test; ++cas)
	{
		printf("Case #%d: ", cas);
		string s;
		cin >> s;
		string cs = s;
		if (next_permutation(s.begin(), s.end()))
			cout << s << endl;
		else
		{
			int index = -1;
			for (int i = 0; i < s.length(); ++i)
				if (s[i] > '0' && (index == -1 || s[index] > s[i]))
					index = i;
			char c = s[index];
			s.erase(s.begin() + index);
			sort(s.begin(), s.end());
			cout << c << "0" << s << endl;
		}
	}
	return 0;
}