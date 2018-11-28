// acm.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	
	for (int test = 1; test <= t; ++test) {
		int c, d, n;
		cin >> c;
		string s;
		char a[26][26];
		memset(a, 0, sizeof(a));
		for (int i = 0; i < c; ++i) {
			cin >> s;
			a[s[0] - 'A'][s[1] - 'A'] = a[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		cin >> d;
		bool r[26][26];
		memset(r, 0, sizeof(r));
		for (int i = 0; i < d; ++i) {
			cin >> s;
			r[s[0] - 'A'][s[1] - 'A'] = r[s[1] - 'A'][s[0] - 'A'] = true;
		}
		cin >> d >> s;
		char st[100000];
		int stl = 0;
		for (int i = 0; i < s.length(); ++i) {
			st[stl++] = s[i];
			if (stl > 1) {
				char c1 = st[stl - 1];
				char c2 = st[stl - 2];
				char c3 = a[c1 - 'A'][c2 - 'A'];
				if (c3) {
					stl -= 2;
					st[stl++] = c3;
				} else
					for (int j = 0; j < stl; ++j)
						for (int k = j + 1; k < stl; ++k)
							if (r[st[j] - 'A'][st[k] - 'A'])
								stl = 0;
			}
		}
		cout << "Case #" << test << ": [";
		for (int i = 0; i < stl - 1; ++i)
			cout << st[i] << ", ";
		if (stl > 0)
			cout << st[stl - 1];
		cout << "]\n";
	}

	return 0;
}

