#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <cstring>
#include <iostream>
#include <cassert>
#include <cctype>

using namespace std;

char line[1024];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	gets(line);
	int T = atoi(line);

	for (int test=0; test<T; ++test) {
		gets(line);
		string a(line);
		string b = a;
		string c = "";

		next_permutation(b.begin(), b.end());
		//cout << a << " " << b << endl;

		if (a<b) {
			c = b;
		} else if (a==b) {
			c = b;
			c.insert(1, "0");
		} else {
			c = b;
			for (int i=0; i<c.length(); ++i) {
				if (c[i]!='0') {
					char app[2] = {c[i], '\0'};
					c[i] = '0';
					c.insert(0, app);
					break;
				}
			}
			assert(a.length()==c.length()-1);
		}

		printf("Case #%d: %s\n", test+1, c.c_str());
	}


	return 0;
}