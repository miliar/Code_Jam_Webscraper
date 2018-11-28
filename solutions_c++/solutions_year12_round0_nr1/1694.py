#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>

using namespace std;

char* enc[3] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char* de[3] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};

char ms[256];

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < 3; ++i) {
		for(int j = 0; enc[i][j]; ++j) {
			ms[enc[i][j]] = de[i][j];
		}
	}
	ms['z'] = 'q';
	ms['q'] = 'z';
	string input;
	getline(cin, input);
	for(int c = 1; c <= T; ++c) {
		getline(cin, input);
		printf("Case #%d: ", c);
		for(int i = 0; i < input.size(); ++i) if('a' <= input[i] && input[i] <= 'z' || input[i] == ' ') {
			if(ms[input[i]]) putchar(ms[input[i]]);
			else printf("(%c)", input[i]);
		}
		puts("");
	}
	return 0;
}
