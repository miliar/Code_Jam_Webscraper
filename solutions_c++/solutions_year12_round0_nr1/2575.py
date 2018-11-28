#include <cstdio>
#include <map>
#include <vector>
#include <iostream>
#include <string>
#include <set>

using namespace std;

map<char, char> dic;

void init() {
	vector<char> used1(26, false);
	vector<char> used2(26, false);
	string s1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqee";
	string s2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazoo";
	for (int i = 0; i < s1.size(); ++i) {
		char c1 = s1[i];
		char c2 = s2[i];
		used1[c1 - 'a'] = true;
		used2[c2 - 'a'] = true;
		dic[c1] = c2;
	}
	for (int i = 0; i < 26; ++i) {
		for (int j = 0; j < 26; ++j) {
			if (!used1[i] && !used2[j]) {
				used1[i] = used2[j] = true;
				dic['a' + i] = 'a' + j;
			}
		}
	}
}


string solve(string str) {
	for (int i = 0; i < str.size(); ++i) {
		char& c = str[i];
		if ('a' <= c && c <= 'z') {
			c = dic[c];
		}
	}
	return str;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	init();
	int T;
	cin >> T;
	string str;
	getline(cin, str);
	for (int t = 1; t <= T; ++t) {
		getline(cin, str);
		cout << "Case #" << t << ": " << solve(str) << endl;
	}
	return 0;
} 