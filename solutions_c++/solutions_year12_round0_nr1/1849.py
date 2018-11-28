#include <iostream>
#include <string>
using namespace std;

string s[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string ss[] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

char c[26];
char buf[1000];

int main() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < s[i].size(); j++) {
            if (s[i][j] != ' ')
            c[s[i][j] - 'a'] = ss[i][j];
        }
    }
    c['q' - 'a'] = 'z';
    c['z' - 'a'] = 'q';
    for (int i = 0; i < 26; i++) {
        if (c[i] == 0) cout << ((char)(i + 'a')) << endl;
    }
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        fgets(buf, sizeof(buf), stdin);
        char *ptr = buf;
        cout << "Case #" << t << ": ";
        while (*ptr && *ptr != '\n' && *ptr != '\r') {
        if (*ptr == ' ') cout << ' '; else
        cout << c[*ptr - 'a'];
            ptr++;
        }
        *ptr = 0;
        cout << ptr << endl;
    }
    return 0;
}
