#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define FORU(i, n) for (uint i = 0; i < (n); ++i)
#define FORR(i, n) for (int i = (n)-1; i >= 0; --i)
#define FORRU(i, n) for (uint i = (n); i-- > 0;)
#define FOREACH(it, v) for (__typeof__((v).begin()) it = (v).begin(); it != (v).end(); ++it)

char cmap[26];

void cmapadd(string a, string b) {
    FORU(i, a.size()) {
        if (a[i] != ' ') {
            cmap[a[i] - 'a'] = b[i];
        }
    }
}

char cmapget(char b) {
    return cmap[b - 'a'];
}

int main() {
    int cases;
    cin >> cases;

    string line;
    getline(cin, line);

    cmapadd("z",
            "q");
    cmapadd("y qee",
            "a zoo");
    cmapadd("ejp mysljylc kd kxveddknmc re jsicpdrysi",
            "our language is impossible to understand");
    cmapadd("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
            "there are twenty six factorial possibilities");
    cmapadd("de kr kd eoya kw aej tysr re ujdr lkgc jv",
            "so it is okay if you want to just give up");

    FOR(tcase, cases) {
        getline(cin, line);

        cout << "Case #" << tcase+1 << ": ";

        FOR(i, line.size()) {
            if (line[i] == ' ') {
                cout << ' ';
            } else {
                cout << cmapget(line[i]);
            }
        }

        cout << endl;
    }

    return 0;
}
