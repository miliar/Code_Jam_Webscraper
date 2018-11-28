#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cctype>
#include <map>

using namespace std;

int t, n;

char c[1000];
char chs[1000];

string s;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq";
	string s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz";
	for (int i = 0; i < s1.size(); i++)
		c[s1[i]] = s2[i];
	gets(chs);
	for (int q = 1; q <= t; q++) {
		string source, res;
		gets(chs);
		for (int i = 0; i < strlen(chs); i++) 
			if (isalpha(chs[i])) {
				res+=c[chs[i]];
			} else {
				res+=chs[i];
			}
		cout << "Case #" << q << ": " << res << endl;
	}
}