#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <stack>
#include <set>

using namespace std;

const char * crypta = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
const char * plaina = "our language is impossible to understand";
const char * cryptb = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
const char * plainb = "there are twenty six factorial possibilities";
const char * cryptc = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char * plainc = "so it is okay if you want to just give up";

char mapping[256];

void decode(const char * crypt, const char * plain) {
	for (size_t i = 0; i < strlen(crypt); i++) mapping[crypt[i]] = plain[i];
}

int main(int argc, char * argv[])
{
	memset(mapping, ' ', 256);

	decode(crypta, plaina);
	decode(cryptb, plainb);
	decode(cryptc, plainc);

	mapping['q'] = 'z';
	mapping['z'] = 'q';

	int T;
	char s[256];

	//for (char i = 'a'; i <= 'z'; i++) if (mapping[i] == ' ') cout << "Missing " << i << '\n';

	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%[^\t\n]\n", s);
		for (size_t i = 0; i < strlen(s); i++) s[i] = mapping[s[i]];
		printf("Case #%d: %s\n", t, s);
	}

	return 0;
}

