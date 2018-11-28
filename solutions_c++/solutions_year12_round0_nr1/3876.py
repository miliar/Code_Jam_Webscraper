#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <cassert>
#include <cctype>

using namespace std;

const char* sample_in[] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

const char* sample_out[] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

char mapping[26];

int main(int ac, char** av)
{
    for (int i=0;i<26;++i) mapping[i] = -1;
    mapping['y'-'a'] = 0;
    mapping['y'-'a'] = 0;
    mapping['e'-'a'] = 'o' - 'a';
    mapping['q'-'a'] = 'z' - 'a';
    mapping['z'-'a'] = 'q' - 'a';
    int cnt=3;
    char a, b;
    for (int i=0; i<3; ++i) {
        for (int j=0; sample_in[i][j]; ++j) {
            a = sample_in[i][j];
            b = sample_out[i][j];
            if (isspace(a)) continue;
            // cerr << a << " -> " << b << endl;
            a -= 'a';
            b -= 'a';
            if (mapping[a]!=-1) {
                // if (mapping[a] != b) {
                //     cerr << "line " << (i+1) << " char " << j << ": ";
                //     cerr << char('a' + a) << " -> " << char('a' + mapping[a])  << " <> " << char('a' + b) << endl;
                // }
                assert(mapping[a]==b);
            } else {
                mapping[a] = b;
                ++cnt;
            }
        }
    }

    string line;
    int T;
    cin >> T;
    getline(cin, line);
    for (int i=1 ;i<=T; ++i) {
        getline(cin, line);
        cout << "Case #" << i << ": ";
        for (int j=0; j<line.size(); ++j) {
            if (isspace(line[j])) {
                cout << line[j];
                continue;
            }
            cout << char('a' + mapping[line[j]-'a']);
        }
        cout << "\n";
    }
}
