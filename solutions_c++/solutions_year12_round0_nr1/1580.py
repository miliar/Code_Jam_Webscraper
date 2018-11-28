#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
using namespace std;
char a[5000];
void calc(string s1, string s2) {
    for (int j = 0; j < s2.size(); j++) {
        a[s1[j]] = s2[j];
       // cout << int(s1[j]) << endl;
    }
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.txt", "w", stdout);
    calc("z","q");
    calc("q", "z");
    calc("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand");
    calc("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    calc("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    //for (int i = 97; i < 97 + 26; i++) cout << a[i] << endl;
    int n;
    cin >> n;
    string t;
    getline(cin,t);
    for (int i = 0; i < n; i++) {
        getline(cin,t);
        cout << "Case #" << i + 1<< ": ";
        for (int j = 0; j < t.size(); j++) {
            cout << a[t[j]];
        }
        cout << endl;
    }
    return 0;
}
