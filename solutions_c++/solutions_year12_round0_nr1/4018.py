#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdio>
#include <string.h>

using namespace std;

string a[5] = { 
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"q",
	"z"
};

string b[5] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"z",
	"q"
};

int main (void)
{
	map<char, char> t;
	for (int i = 0; i < 5; ++i) {
		for (int j = 0; j < a[i].size (); ++j) {
			if (a[i][j] != ' ')
				t[a[i][j]] = b[i][j];
		}
	}

	int T, l;	
	char in[256];
	
	cin >> T;
	cin.getline (in, 256, '\n');
	for (int i = 1; i <= T; ++i) {
		cin.getline (in, 256, '\n');
		l = strlen (in);
		cout << "Case #" << i << ": ";
		for (int j = 0; j < l; ++j)
			if (in[j] == ' ')
				cout << ' ';
			else
				cout << t[in[j]];
				
		cout << endl;
	}
	
	return 0;
}