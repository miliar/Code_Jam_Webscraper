#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
int inline ABS(int a){ return a>0?a:-a; }
typedef pair<int,int> pi;
typedef unsigned long long ULL;
typedef long long LL;

/* Main code starts from here */

char mp[26];

void decode() {
	memset(mp, -1, sizeof mp);
	string inp = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string out = "our language is impossible to understand";
	for (int i = 0; i < inp.size(); i++) {
		if (inp[i] == ' ') continue;
		mp[inp[i]-'a'] = out[i]-'a';
	}
	inp = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	out = "there are twenty six factorial possibilities";
	for (int i = 0; i < inp.size(); i++) {
		if (inp[i] == ' ') continue;
		mp[inp[i]-'a'] = out[i]-'a';
	}
	inp = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	out = "so it is okay if you want to just give up";
	for (int i = 0; i < inp.size(); i++) {
		if (inp[i] == ' ') continue;
		mp[inp[i]-'a'] = out[i]-'a';
	}
	// q and z left unmapped
	mp['z'-'a'] = 'q' - 'a';
	mp['q'-'a'] = 'z' - 'a';
}

int main() {
	decode();
	int t = 1,T;
	for (scanf("%d", &T), getchar(); t <= T; t++) {
		string inp;
		getline(cin, inp);
		printf("Case #%d: ", t);
		for (int i = 0; i < inp.size(); i++)
			if (inp[i] == ' ')
				putchar(' ');
			else
				putchar (mp[inp[i]-'a'] + 'a');
		puts("");
	}
	return 0;
}
