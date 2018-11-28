#include <memory.h>
#include <stdio.h>
#include <assert.h>

#include <string>
#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<ll> vll;

#define all(x) (x).begin(), (x).end()
#define clear(x) (x).clear()
#define clearm(x) memset((x), 0, sizeof(x))

#define FOR(i, b, e) for (int i = (b); i < (e); ++i)
#define RE(i, n) FOR(i, 0, (n))

const int maxn = 2e5 + 5;

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char dic[26] = {
	'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r',
'z',	
't', 'n', 'w', 'j', 'p', 'f', 'm', 'a',
'q'
};

int main() {
#ifndef ONLINE_JUDGE
    //freopen("in.txt", "r", stdin);
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    // freopen("out.txt", "w", stdout);
#endif
	/*
	for (int i = 'a'; i <= 'z'; ++i) {
		char c = -1;
		for (int j = 0; j < a.size(); ++j) {
			if (a[j] == i) {
				c = b[j];
				break;
			}
		}
		if (c != -1) {
			cout << "'" << c << "'," << endl;
		} else {
			cout << "wrong" << endl;
		}
	}
	return 0;
	*/
	int ncase;
	string line;
	cin >> ncase;
	getline(cin, line);
	RE(i, ncase) {	
		cout << "Case #" << i + 1 << ": ";
		getline(cin, line);
		RE(j, line.size()) {
			if ('a' <= line[j] && line[j] <= 'z') {
				cout << dic[line[j] - 'a'];
			} else {
				cout << line[j];
			}
		}
		cout << endl;
	}
    return 0;
}