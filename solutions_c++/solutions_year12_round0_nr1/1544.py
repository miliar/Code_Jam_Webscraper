#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

string s[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

string t[] = {"our language is impossible to understand", 
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

map<char, char> trans;
int ts, ca;
string str;

int main() {
    freopen("gcj_A.out", "w", stdout);
    trans['z'] = 'q';
    trans['q'] = 'z';
    trans[' '] = ' ';
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < (int)s[i].length(); j++) {
            if(!isalpha(s[i][j])) continue;
            trans[s[i][j]] = t[i][j];
        }
    }
    cin >> ts;
    getline(cin, str);
    while(ts--) {
        cout << "Case #" << ++ca << ": ";
        getline(cin, str);
        for(int i = 0; i < (int)str.length(); i++) {
            cout << trans[str[i]];
        }
        cout << endl;
    }
    return 0;
}

