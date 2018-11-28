#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <set>
using namespace std;

int main() {
    string a[3] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    };
    string b[3] = {
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up",
    };
    map<char, char> mapping;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < (int)a[i].size(); ++j) {
            if (isalpha(a[i][j])) {
                mapping.insert(make_pair(a[i][j], b[i][j]));
            }
        }
    }
    mapping.insert(make_pair('q', 'z'));
    mapping.insert(make_pair('z', 'q'));
    /*
    set<char> s;
    for (map<char,char>::iterator it=mapping.begin(); it!=mapping.end(); ++it) {
        cout << it->first << endl;
        s.insert(it->second);
    }
    for (char i = 'a'; i <= 'z'; ++i) {
        if (!s.count(i)) {
            cout << "MISSING " << i << endl;
        }
    }
    cout << mapping.size() << endl;
    */
    int t;
    cin >> t;
    while (cin.get() != '\n');
    for (int tt = 0; tt < t; ++tt) {
        string buf;
        getline(cin, buf);
        for (int i = 0; i < (int)buf.size(); ++i) {
            if (isalpha(buf[i])) {
                buf[i] = mapping[buf[i]];
            }
        }
        cout << "Case #" << tt + 1<< ": " << buf << endl;
    }
}
