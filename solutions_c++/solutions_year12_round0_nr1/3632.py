#include <algorithm>
#include <cassert>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

const string decoded="a zooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
const string encoded="y qeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";

int main() {
	map<char, char> translation;
	for (int i=0; i<encoded.size(); i++) {
		if (translation.find(encoded[i]) != translation.end())
			assert(translation[encoded[i]] == decoded[i]);
		else
			translation[encoded[i]] = decoded[i];
	}

	translation['z'] = 'q';

	int T;
	scanf("%d\n", &T);
	char buf[1000];
	for (int t=1; t<=T; t++) {
		gets(buf);
		printf("Case #%d: ", t);
		for (int i=0; buf[i]; i++) {
			assert(translation.find(buf[i]) != translation.end());
			buf[i] = translation[buf[i]];
		}
		puts(buf);
	}
	return 0;
}