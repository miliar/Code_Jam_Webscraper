#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;
map<char, char> dict;

void doDict(string in, string out) {
	for (int i = 0, n = in.length() ; i < n ; i++) {
		dict[in[i]] = out[i];
	}
}

string translate(string lang) {
	for (int i = 0, n = lang.length(); i < n; i++) {
		lang[i] = dict[lang[i]];
	}
	return lang;
}

int main() {
    int n;
    string lang;
    doDict("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    doDict("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    doDict("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    doDict("zq", "qz");
    cin >> n;
    getline(cin, lang);
    for (int i = 1 ; i < n+1 ; i++) {
        getline(cin, lang);
        cout << "Case #" << i << ": " << translate(lang) << endl;
    }
    return 0;
}