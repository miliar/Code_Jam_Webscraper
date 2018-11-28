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

#define MAX_SCORE 10
#define MAX_TOTAL_SCORE 30
#define MAX_SURPRISED 100
#define MAX_GOOGLERS 100

int n, max_surprising, p;
int scores[MAX_GOOGLERS + 1];

//surp[i][j] = 1 if total score i with best score j is not surprising
int surp[MAX_TOTAL_SCORE + 1][MAX_SCORE + 1];

//-2 = not calculated, -1 not possible
int dp[MAX_SURPRISED + 1][MAX_GOOGLERS + 1];

int solve(int num_surprised, int curr_googler)
{
    if (num_surprised > max_surprising)
        return -10;

    if (curr_googler == n) {
        if (num_surprised != max_surprising)
            return -10;
        else
            return 0;
    }

    if (dp[num_surprised][curr_googler] != -2)
        return dp[num_surprised][curr_googler];

    int best = -1;

    //try >= p
    int exists = 0;
    int non_exists = 0;
    for (int i = p; i <= MAX_SCORE; ++i) {
        if (surp[scores[curr_googler]][i] == 1)
            exists = 1;
        else if (surp[scores[curr_googler]][i] == 2)
            non_exists = 1;
    }
    if (exists)
        best = max(best, solve(num_surprised, curr_googler + 1) + 1);
    if (non_exists)
        best = max(best, solve(num_surprised + 1, curr_googler + 1) + 1);

    //try < p
    exists = 0;
    non_exists = 0;
    for (int i = 0; i < p; ++i) {
        if (surp[scores[curr_googler]][i] == 1)
            exists = 1;
        else if (surp[scores[curr_googler]][i] == 2)
            non_exists = 1;
    }
    if (exists)
        best = max(best, solve(num_surprised, curr_googler + 1));
    if (non_exists)
        best = max(best, solve(num_surprised + 1, curr_googler + 1));

    return dp[num_surprised][curr_googler] = best;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("B-small-attempt4.in", "r", stdin);
    freopen("B-small-attempt4.out", "w", stdout);

    for (int i = 0; i <= MAX_SCORE; ++i)
    for (int j = 0; j <= MAX_SCORE; ++j)
    for (int k = 0; k <= MAX_SCORE; ++k) {
        int maxdiff = max(abs(j - i), max(abs(k - j), abs(k - i)));
        if (surp[i + j + k][max(k, max(i, j))] != 1) {
            if (maxdiff < 2)
                surp[i + j + k][max(k, max(i, j))] = 1;
            else if (maxdiff == 2)
                surp[i + j + k][max(k, max(i, j))] = 2;
        }
        if (surp[i+j+k][min(k, min(i,j))] != 1) {
            if (maxdiff==2)
                surp[i+j+k][min(k, min(i,j))] = 2;
        }
    }
//
//    for (int i = 0; i <= 30; ++i) {
//        cout << i << ' ';
//        for (int j = 0; j <= 10; ++j)
//            cout << surp[i][j] << ' ';
//        cout << endl;
//    }

    int cases;
    cin >> cases;

    for (int i = 1; i <= cases; ++i) {
        cin >> n >> max_surprising >> p;
        for (int j = 0; j < n; ++j)
            cin >> scores[j];

        for (int k = 0; k <= MAX_SURPRISED; ++k)
            for (int j = 0; j <= MAX_GOOGLERS; ++j)
                dp[k][j] = -2;

        int ans = max(0, solve(0, 0));

        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
