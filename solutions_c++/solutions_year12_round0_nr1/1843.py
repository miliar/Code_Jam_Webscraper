#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

string ax = "our language is impossible to understand";
string bx = "there are twenty six factorial possibilities";
string cx = "so it is okay if you want to just give up";

char dic[256];
char dicx[256];

void main() {
	int i, j;
	memset(dic, 0x00, sizeof(dic));
	memset(dicx, 0x00, sizeof(dicx));

	dic['q'] = 'z';
	dicx['z'] = 'q';

	REP(i,a.length()) {
		if (a[i] != ' ') {
			dic[a[i]] = ax[i];
			dicx[ax[i]] = a[i];
		}
	}

	REP(i,b.length()) {
		if (b[i] != ' ') {
			dic[b[i]] = bx[i];
			dicx[bx[i]] = b[i];
		}
	}

	REP(i,c.length()) {
		if (c[i] != ' ') {
			dic[c[i]] = cx[i];
			dicx[cx[i]] = c[i];
		}
	}

	for (i = 'a'; i <= 'z'; ++i) {
		if (!dic[i])
			break;
	}

	for (j = 'a'; j <= 'z'; ++j) {
		if (!dicx[j])
			break;
	}

	if (i <= 'z' && j <= 'z') {
		dic[i] = j;
		dicx[j] = i;
	}

	int G;
	char buf[200];

	gets(buf);
	sscanf(buf, "%d", &G);

	REP(i, G) {
		gets(buf);
		if (buf[0] == '\n' || buf[0] == 0x00)
			break;

		string res = "";

		for (j = 0; buf[j] != 0x00 && buf[j] != '\n'; ++j) {
			if (buf[j] == ' ')
				res += ' ';
			else
				res += dic[buf[j]];
		}

		cout << "Case #" << (i+1) << ": " << res << endl;
	}
}