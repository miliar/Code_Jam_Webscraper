#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <stack>
#include <deque>
#include <map>
#include <numeric>
#include <iterator>
#include <cassert>
#include <cstring>

#define FOR(i,s,n) for((i)=(s);(i)<(int)(n);(i)++)
#define FORD(i,s,n) for((i)=(s);(i)>=(int)(n);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define INF (1<<29)

using namespace std;

char ascii[128];

void init() {
    string from[4] = {
        "ejp mysljylc kd kxveddknmc re jsicpdrysi",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv",
        "qz"
    };
    string to[4] = {
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up",
        "zq"
    };

    int i,j;

    FOR(i,'a', 'z'+1){
        ascii[i] = 0;
    }

    FOR(i,0,4){
        FOR(j,0,from[i].size()) {
            ascii[(int)from[i][j]] = to[i][j];
        }
    }
}

int run(int ncase){
    string str, ans;
    getline (cin,str);
    //cout << str << endl;
    foreach(str, itr) {
        ans.push_back(ascii[(int)*itr]);
    }

    cout << "Case #" << ncase << ": ";
    cout << ans << endl;
    return 0;
}

int main() {
    int i, test_set;
    init();
    cin >> test_set;
    cin.ignore();
    FOR(i, 0, test_set) run(i+1);
    return 0;
}
