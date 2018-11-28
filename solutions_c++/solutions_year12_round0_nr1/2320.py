#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <map>
#include <string>

using namespace std;

const int N = 100 + 10;

char decode[256];
string s[N], t[N];

void analyze (const string &s, const string &t) {
	assert(s.size() == t.size());
	int n = s.size();
	for (int i = 0; i < n; ++i) {
		decode[s[i]] = t[i];
	}
}

int main () {
	freopen("sample.in", "r", stdin);
	freopen("decode.out", "w", stdout);
	
	memset(decode, -1, sizeof(decode));
	char buf[1000];
	int n, i;
	cin >> n;
	gets(buf);
	for (int i = 0; i < n; ++i) {
		gets(buf);
		s[i] = buf;
	}
	for (int i = 0; i < n; ++i) {
		gets(buf);
		t[i] = buf;
	}
	for (int i = 0; i < n; ++i) {
		analyze(s[i], t[i]);
	}
	
	cout << "{";
	for (char c = 'a'; c <= 'z'; ++c) {
		if (c != 'a') {
			cout << ", ";
		}
		cout << "'" << decode[c] << "'";
	}
	cout << "}";
	return 0;
}
