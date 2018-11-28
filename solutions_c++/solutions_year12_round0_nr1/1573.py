#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
using namespace std;

map <char, char> dict;

const char str1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char str2[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

int main() {
    size_t len = strlen(str1);
    for (size_t i = 0; i < len; ++i)
        dict[str1[i]] = str2[i];
    dict['z'] = 'q';
    dict['q'] = 'z';

    int t;
    scanf("%d\n", &t);
    for (int tt = 1; tt <= t; ++tt) {
        string s;
        getline(cin, s);
        for (size_t i = 0; i < s.size(); ++i)
            s[i] = dict[s[i]];
        cout << "Case #" << tt << ": " << s << '\n';
    }

    return 0;
}
