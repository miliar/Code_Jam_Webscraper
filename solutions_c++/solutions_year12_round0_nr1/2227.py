#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <iostream>
#include <map>
#include <iomanip>
#include <fstream>
#include <locale>
#include <cmath>
using namespace std;

int main() {
    ifstream cin("A-small-attempt1.in");
    ofstream cout("out.txt");
    int T = 0;
    cin >> T;
    string in = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string out = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    char next[256] = {};
    for (int i = 0; i < in.size(); i++) {
        next[in[i]] = out[i];
    }
    next['z'] = 'q';
    next['q'] = 'z';
    string s;
    getline(cin, s);
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t+1 << ": ";
        getline(cin, s);
        for (int i = 0; i < s.size(); i++) {
            s[i] = next[s[i]];
        }
        cout << s;
        cout << endl;
    }
}
