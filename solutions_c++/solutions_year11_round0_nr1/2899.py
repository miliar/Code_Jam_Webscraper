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

int main() {
    int nTests = 0;
    cin >> nTests;

    FOR (test, 1, nTests) {
        int nNeedToPress = 0;
        cin >> nNeedToPress;

        int currTime = 0;
        int bluePos = 1;
        int blueMoves = 0;
        int orangePos = 1;
        int orangeMoves = 0;
        REP (i, nNeedToPress) {
            int buttonPos = 0;
            char color = '\0';
            cin >> color >> buttonPos;
            // cout << "O: " << orangePos << ", B: " << bluePos << endl;
            // cout << currTime << endl;
            if (color == 'O') {
                if (abs(orangePos - buttonPos) <= orangeMoves) {
                    // push the button
                    currTime += 1;
                    blueMoves += 1;

                    orangePos = buttonPos;
                    orangeMoves = 0;
                } else {
                    // move to button + push button
                    int movesNeeded = abs(buttonPos - orangePos) + 1;
                    if (orangeMoves >= movesNeeded) {
                        orangeMoves -= movesNeeded;
                        movesNeeded = 0;
                    } else {
                        movesNeeded -= orangeMoves;
                        orangeMoves = 0;
                    }
                    currTime += movesNeeded;
                    blueMoves += movesNeeded;

                    orangePos = buttonPos;
                }
            } else if (color == 'B') {
                if (abs(bluePos - buttonPos) <= blueMoves) {
                    // push the button
                    currTime += 1;
                    orangeMoves += 1;

                    bluePos = buttonPos;
                    blueMoves = 0;
                } else {
                    // move to button + push button
                    int movesNeeded = abs(buttonPos - bluePos) + 1;
                    if (blueMoves >= movesNeeded) {
                        blueMoves -= movesNeeded;
                        movesNeeded = 0;
                    } else {
                        movesNeeded -= blueMoves;
                        blueMoves = 0;
                    }
                    currTime += movesNeeded;
                    orangeMoves += movesNeeded;

                    bluePos = buttonPos;
                }
            } else {
                assert(false);
            }
        }

        cout << "Case #" << test << ": " << currTime << '\n';
    }

    return 0;
}
