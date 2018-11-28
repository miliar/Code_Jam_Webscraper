#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

char combines[256][256];
list<char> opposes[256];

int main() {
    int nTests = 0;
    cin >> nTests;

    FOR (test, 1, nTests) {
        memset(combines, -1, sizeof(combines));
        REP (i, 256) {
            opposes[i].clear();
        }
        int nCombines = 0;
        cin >> nCombines;
        REP (i, nCombines) {
            string str;
            cin >> str;
            combines[(int)str[0]][(int)str[1]] = str[2];
            combines[(int)str[1]][(int)str[0]] = str[2];
        }
        int nOpposes = 0;
        cin >> nOpposes;
        REP (i, nOpposes) {
            string str;
            cin >> str;
            opposes[(int)str[0]].PB(str[1]);
            opposes[(int)str[1]].PB(str[0]);
        }

        int N = 0;
        string invokeElems;
        cin >> N >> invokeElems;
        vector<char> list;
        multiset<char> elemsInList;
        FOREACH (ch, invokeElems) {
            list.PB(*ch);
            elemsInList.insert(*ch);
            if (SIZE(list) >= 2) {
                char x = list[SIZE(list)-1];
                char y = list[SIZE(list)-2];
                if (combines[(int)x][(int)y] != -1) {
                    list.pop_back();
                    elemsInList.erase(elemsInList.find(x));
                    list.pop_back();
                    elemsInList.erase(elemsInList.find(y));
                    list.PB(combines[(int)x][(int)y]);
                    elemsInList.insert(combines[(int)x][(int)y]);
                } else {
                    bool clear = false;
                    FOREACH (oppose, opposes[(int)x]) {
                        if (elemsInList.find(*oppose) != elemsInList.end()) {
                            clear = true;
                            break;
                        }
                    }
                    if (clear) {
                        list.clear();
                        elemsInList.clear();
                    }
                }
            }
        }

        cout << "Case #" << test << ": ";
        cout << "[";
        FOREACH (x, list) {
            if (x != list.begin()) {
                cout << ", ";
            }
            cout << *x;
        }
        cout << "]\n";
    }

    return 0;
}
