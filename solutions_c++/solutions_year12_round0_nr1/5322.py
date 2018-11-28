#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
#include <functional>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

map<char, char> code, rev_code;

void solve(int ind) {
    string st;
    getline(cin, st);
    for (int i = 0; i < st.size(); ++i) {
      st[i] = code[st[i]];
    }
    //output
    cout << "Case #" << ind << ": " << st << endl;
}

int main() {
    // deduce the encoding
    string in = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string ou = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    int i,T;
    for (i = 0; i < in.size(); ++i) {
      code[in[i]] = ou[i];
    }
    code['q'] = 'z';
    code['z'] = 'q';
    cin >> T;
    string st;
    getline(cin, st);
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
