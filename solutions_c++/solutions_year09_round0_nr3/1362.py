#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d\n", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int main(void) {
    int N; SC(&N);

    const char *c = "welcome to code jam";

    FOR(_i,N) {
        string s;
        getline(cin, s);
        FOR(i,s.size())
            s[i] = tolower(s[i]);

        vector<pI> dp;
        dp.push_back(pI(-1,1));

        FOR(i,19) {
            vector<pI> dpNext;

            int idx = -1;
            while(true) {
                idx = s.find(c[i], idx+1);
                if (idx == -1) break;

                int dpIdx = 0;
                int count = 0;
                while(dpIdx < dp.size() && dp[dpIdx].first < idx) {
                    count += dp[dpIdx].second;
					++dpIdx;
                }

                dpNext.push_back(pI(idx, count % 10000));
            }

            dpNext.swap(dp);
        }

        int res = 0;
        FOR(i, dp.size())
            res += dp[i].second;

        printf("Case #%d: %04d\n", _i+1, res % 10000);
    }
    return 0;
}
