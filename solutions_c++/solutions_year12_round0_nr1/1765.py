#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

string FROM[3] = { "ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
string TO[3] =   { "our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up" };

int main()
{
    map<char, char> mp;
    for (int i = 0; i < 3; ++i)
        for (size_t j = 0; j < FROM[i].size(); ++j)
            mp[FROM[i][j]] = TO[i][j];
    mp['z'] = 'q';
    mp['q'] = 'z';

    int tests;
    cin >> tests;
    cin.ignore();
    for (int test = 0; test < tests; ++test)
    {
        string s;
        getline(cin, s);
        for (size_t i = 0; i < s.size(); ++i) s[i] = mp[s[i]];
        cout << "Case #" << test + 1 << ": " << s << '\n';
    }
    return 0;
}
