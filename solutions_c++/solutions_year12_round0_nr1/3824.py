#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<char, char> mapping;
    const string olds = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv qeyz\n";
    const string news = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up zoaq\n";

    for (int i = 0; i < olds.length(); ++i) mapping[olds[i]]=news[i];

    int n;
    string str;
    cin >> n;
    getline(cin, str);
    for (int i = 0; i < n; ++i) {
        getline(cin, str);
        cout << "Case #" << i+1 << ": ";
        for (int j = 0; j < str.length(); ++j) cout << mapping[str[j]];
        cout << endl;
    }

    return 0;
}

