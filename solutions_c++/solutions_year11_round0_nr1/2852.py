#include <vector>
#include <list>

#include <deque>
#include <queue>
#include <stack>

#include <map>
#include <set>

#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> ii;
#define infinity ~(1<<31)
#define longInfinity ~((1LL)<<63)
#define eps 1e-7
#define FOR(i,n) for((i) = 0 ; (i) <int(n);++(i))
#define MP make_pair
#define PB push_back
#define sz size()
#define ln length()
#define fill(f,a) memset(f, a, sizeof(f))
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define tr(container, it) for(typeof((container).begin()) it = (container).begin(); it != (container).end(); it++)

vector<int> O;
vector<int> B;
vector<pair<bool, int> > seq;

int main() {
    int t, iterIndex, n, m, result;
    char c;
    scanf("%d", &t);
    for (iterIndex = 0; iterIndex < t; ++iterIndex) {
        //TODO takeinput
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf(" %c %d", &c, &m);
            if (c == 'O') {
                O.PB(m);
                seq.PB(MP(0, m));
            } else {
                B.PB(m);
                seq.PB(MP(1, m));
            }
        }
        result = 0;
        int aB = 1, aO = 1;
        while (!seq.empty()) {
            int diff = 0;
            if (seq[0].first) { // B
                diff = abs(seq[0].second - aB) + 1;
                assert(diff>=0);
                aB = seq[0].second;
                B.erase(B.begin());
                if (!O.empty())
                    if (O[0] < aO) {
                        aO = aO - diff <= O[0] ? O[0] : (aO - diff);
                    } else {
                        aO = aO + diff >= O[0] ? O[0] : (aO + diff);
                    }
            } else { //O
                diff = abs(seq[0].second - aO) + 1;
                assert(diff>=0);
                aO = seq[0].second;
                O.erase(O.begin());
                if (!B.empty())
                    if (B[0] < aB) {
                        aB = aB - diff <= B[0] ? B[0] : (aB - diff);
                        assert(aB>=0);
                    } else {
                        aB = aB + diff >= B[0] ? B[0] : (aB + diff);
                        assert(aB>=0);
                    }
            }
            result += diff;
            seq.erase(seq.begin());
        }
        printf("Case #%d: %d\n", iterIndex + 1, result);
    }
    return 0;
}