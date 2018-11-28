#include <string>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

char input[128];
string inp[7] = {"a", "o", "z", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv", "q"};
string out[7] = {"y", "e", "q", "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up", "z"};
map<char, char> m;

int main() {
    int i, j, t, T;

    m.clear();
    for (i=0; i<7; i++) {
        for (j=0; j<(int)inp[i].size(); j++) {
            m[inp[i][j]] = out[i][j];
        }
    }

    cin.getline(input, 128); sscanf(input, "%d", &T);
    for (t=1; t<=T; t++) {
        cout << "Case #" << t << ": ";
        cin.getline(input, 128);
        for (i=0; input[i]!='\0'; i++) cout << m[input[i]];
        cout << endl;
    }

    return 0;
}
