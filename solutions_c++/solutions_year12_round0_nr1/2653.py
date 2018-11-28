#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;
string Encrypt[3] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string plain[3] = {
	"our language is impossible to understand", 
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};
int perm[26];
string Decrypt(string s) {
	string res = "";
	for (int i = 0; i < s.size(); ++ i) {
		if (s[i] != ' ')
			res += perm[s[i] - 'a'] + 'a';
		else res += ' ';
	}
	return res;
}
int dictn = 3;

int main() {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);
	memset(perm, -1, sizeof(perm));
	perm['y'-'a'] = 'a' - 'a';
	perm['e' - 'a'] = 'o' - 'a';
	perm['q' - 'a'] = 'z' - 'a';
	perm['z' - 'a'] = 'q' - 'a';
	for (int i = 0; i < dictn; ++ i) {
		for (int j = 0; j < Encrypt[i].size(); ++ j) if (Encrypt[i][j] != ' ') {
			if (perm[Encrypt[i][j] - 'a'] != -1 && (plain[i][j] - 'a') != perm[Encrypt[i][j] - 'a']) {
				cout << "wrong" << endl;
				return -1;
			}
			perm[Encrypt[i][j] - 'a'] = (plain[i][j] - 'a');
		}
	}
	int n;
	char line[1024];
	scanf ("%d", &n);
	getchar();
	for (int i = 0; i < n; ++ i) {
		cin.getline(line, 1024);
		cout << "Case #" << i + 1 << ": " << Decrypt(line) << endl;
	}
	return 0;
}
