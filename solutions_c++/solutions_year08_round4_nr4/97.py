#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++)
	{
		int k;
		string s;
		cin >> k;
		cin >> s;
		vector <int> p;
		for (int i = 0; i < k; i++) p.push_back (i);
		int be = INT_MAX;
		do
		{
			string t = s;
			for (int i = 0; i < s.size(); i += k)
				for (int j = 0; j < k; j++)
					t[i+j] = s[i+p[j]];
			int c = 1;
			for (int i = 1; i < t.size(); i++)
				if (t[i] != t[i-1]) c++;
			be = min (be, c);
		} while (next_permutation (p.begin(), p.end()));
		cout << "Case #" << cc << ": " << be << endl;
	}
	return 0;
}
