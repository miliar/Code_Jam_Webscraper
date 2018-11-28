#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <cstring>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <cassert>
#include <queue>
#include <iterator>

typedef long long LL;
typedef long double LD;

using namespace std;

const string TRANSLATED = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
                          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
                          "de kr kd eoya kw aej tysr re ujdr lkgc jv"
                          "yeqz";

const string ORIGINAL =   "our language is impossible to understand"
                          "there are twenty six factorial possibilities"
                          "so it is okay if you want to just give up"
                          "aozq";

map<char, char> mapping;

int main() {
#ifndef LOCAL
//  freopen(".in", "r", stdin);
//  freopen(".out", "w", stdout);
#endif

    assert(ORIGINAL.size() == TRANSLATED.size());
    for (int i = 0; i < ORIGINAL.size(); i++) {
        char c = TRANSLATED[i];
        char w = ORIGINAL[i];
        if (mapping.count(c) && mapping[c] != w) {
            cerr << "Error at position " << i << '\n'
                 << "wants to map " << c << " to " << w << '\n'
                 << "but " << c << " is already mapped to " << mapping[c] << '\n';
            assert(0);
        }
            
        mapping[c] = w;
    }
    assert(mapping.size() == 27);

    int nTests;
    cin >> nTests;

    string tmp;
    getline(cin, tmp);

    for (int test = 1; test <= nTests; test++) {
        string text;
        getline(cin, text);

        for (int i = 0; i < text.size(); i++) {
            if (!mapping.count(text[i])) {
                cerr << "Error: no mapping for " << text[i] << '\n';
                assert(0);
            }
            text[i] = mapping[text[i]];
        }

        cout << "Case #" << test << ": " << text << '\n';
    }

    return 0;
}


