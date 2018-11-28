/**
   File: main.cpp

   (c) Copyright Albert Graells Rovira

   $Id$
*/

#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi>  vvi;

long long best(int state, int match, int missed, vi& input, map<pair<int, pii>, int>& memo) {
    if (state == 0) {
        if (missed > input[match]) return -1;
        else                       return 0;
    }
    else {
        std::pair<int, pii> actual = make_pair(state, pii(match, missed));

        if (memo.find(actual) != memo.end()) {
            return memo[actual];
        }

        // buy match
        long long iVal1 = best(state - 1, match * 2, missed, input, memo);
        long long iVal2 = best(state - 1, match * 2 + 1, missed, input, memo);

        long long iOut1 = -1;

        if (iVal1 != -1 && iVal2 != -1) {
            iOut1 = input[match] + iVal1 + iVal2;
        }

        // don't buy
        long long iVal3 = best(state - 1, match * 2, missed + 1, input, memo);
        long long iVal4 = best(state - 1, match * 2 + 1, missed + 1, input, memo);

        long long iOut2 = -1;

        if (iVal3 != -1 && iVal4 != -1) {
            iOut2 = iVal3 + iVal4;
        }

        if (iOut1 == -1) return memo[actual] = iOut2;
        if (iOut2 == -1) return memo[actual] = iOut1;

        return memo[actual] = min(iOut1, iOut2);
    }
}

long long calcResult() {
    int P;
    cin >> P;
    vi input(1 << (P + 1));

    for (int i = (1 << (P + 1)) - 1; i > 0 ; i--) cin >> input[i];
    map<std::pair<int, pii>, int> memo;
    return best(P, 1, 0, input, memo);
}


int main()
{
    int N;
    cin >> N;
    for (int k = 1; k <= N; k++) {
        cout << "Case #" << k << ": ";
        long long iResult = calcResult();
        cout << iResult << endl;
    }
    return 0;
}
