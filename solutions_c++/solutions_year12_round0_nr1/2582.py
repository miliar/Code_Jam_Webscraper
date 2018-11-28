// includes {{{
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
// }}}
// defines {{{
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define all(c) (c).begin(),(c).end()
#define foreach(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
// }}}


int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    //find mapping with examples
    string ex_from = (string)"ejp mysljylc kd kxveddknmc re jsicpdrysi " +
                     (string)"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd " +
                     (string)"de kr kd eoya kw aej tysr re ujdr lkgc jv " +
                     (string)"y qee";
    string ex_to = (string)"our language is impossible to understand " +
                   (string)"there are twenty six factorial possibilities " +
                   (string)"so it is okay if you want to just give up " +
                   (string)"a zoo";

    char dict[256];
    for (int i = 0; i < sz(ex_from); ++i)
        dict[int(ex_from[i])] = ex_to[i];

    //for (int i=0; i<26; ++i)
        //cout << char(i+'a') << ' ' << dict[int(i+'a')] << endl;
    dict[int('z')] = 'q';

    int cases;
    cin >> cases;
    cin.ignore();

    for (int i = 1; i <= cases; ++i) {
        string s;
        getline(cin, s);

        cout << "Case #" << i << ": ";
        for (int j = 0; j < sz(s); ++j)
            cout << dict[int(s[j])];
        cout << endl;
    }

    return 0;
}
