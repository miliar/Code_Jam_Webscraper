
#include <map>
#include <cstdio>
#include <iostream>
#include <cassert>
#include <set>
using namespace std;

int main() {
	string line;
	getline(cin, line);
	int testsCount;
	sscanf(line.c_str(), "%d", &testsCount);
	string inputs[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	string outputs[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
	map<char, char> onto;
	onto['y'] = 'a';
	onto['e'] = 'o';
	onto['q'] = 'z';
	for (int i = 0; i < 3; ++i) {
		assert(inputs[i].size() == outputs[i].size());
		for (int j = 0; j < (int)inputs[i].size(); ++j) {
			if (onto.count(inputs[i][j])) {
				assert(onto[inputs[i][j]] == outputs[i][j]);
			}
			onto[inputs[i][j]] = outputs[i][j];
		}
	}
	set<char> allRight;
	for (char ch = 'a'; ch <= 'z'; ++ch) allRight.insert(ch);
	for (__typeof(onto.begin()) it = onto.begin(); it != onto.end(); ++it)
		if (allRight.count(it->second)) {
			allRight.erase(it->second);
		}
	for (char ch = 'a'; ch <= 'z'; ++ch) if (!onto.count(ch)) {
		onto[ch] = *allRight.begin();
		break;
	}

	for (int test = 0; test < testsCount; ++test) {
		printf("Case #%d: ", test + 1);
		getline(cin, line);
		for (int i = 0; i < (int)line.size(); ++i) {
			if (!onto.count(line[i])) {
				putchar('?');
			} else
				putchar(onto[line[i]]);
		}
		puts("");
	}
	return 0;
}
