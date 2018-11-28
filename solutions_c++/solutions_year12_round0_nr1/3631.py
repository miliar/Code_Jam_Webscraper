#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iterator>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define for_size(var, size) \
    for(int var = 0; var < (size); ++var)
#define for_range(var, from, to) \
    for(int var = (from); var < (to); ++var)
#define for_ranges(var, from, to, step) \
    for(int var = (from); var < (to); var += (step))
#define for_each(var, container) \
    for(typeof((container).begin()) var = (container).begin(); var != (container).end(); ++var)

using namespace std;

string sampleOutput[4] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"qz"
};

string sampleInput[4] = {
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up",
"zq"
};

map<char, char> charMapping;

string& convert(string& s) {
    for_each(it, s) {
        *it = charMapping[*it];
    }
    return s;
}
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A.out", "w", stdout);
    for_size(i, 4) {
        int n = sampleInput[i].size();
        for_size(j, n) {
            charMapping[sampleOutput[i][j]] = sampleInput[i][j];
        }
    }
    int testNum;
    string line;
    cin >> testNum;
    getline(cin, line);
    for_size(testIdx, testNum) {
        getline(cin, line);
        printf("Case #%d: %s\n", testIdx + 1, convert(line).data());
    }

    return 0;
}
