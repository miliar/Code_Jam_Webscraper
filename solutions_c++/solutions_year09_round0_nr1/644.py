#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <iostream>
#include <queue>
#define FOR(i,n) for(int i = 0; i < (int) (n); i++)
using namespace std;

int l, d, n;
string dict[5005];

void parse(string s, vector<bitset<256> >& v)
{
	int i = 0, n = (int) s.length();
	while (i < n) {
		bitset<256> bs;
		if (s[i] == '(') {
			i++;
			while (s[i] != ')') {
				bs[s[i]] = true;
				i++;
			}
			i++;
		} else {
			bs[s[i]] = true;
			i++;
		}
		v.push_back(bs);
	}
}

bool match(string s, const vector<bitset<256> >& v)
{
	for (int i = 0; i < (int) s.length(); i++) {
		if (!v[i][s[i]]) return false;
	}
	return true;
}

int main(void)
{
	//freopen("a.in", "rt", stdin);
	//freopen("a.out", "wt", stdout);
	cin >> l >> d >> n;
	FOR(i, d) cin >> dict[i];
	//
	FOR(tc, n) {
		string s;
		cin >> s;
		vector<bitset<256> > v;
		parse(s, v);
		int c = 0;
		FOR(i, d) if (match(dict[i], v)) c++;
		cout << "Case #" << tc + 1 << ": " << c << endl;
	}
	//
	
	return 0;
}
