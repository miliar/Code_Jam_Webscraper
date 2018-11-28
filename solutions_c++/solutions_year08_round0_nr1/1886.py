#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;

typedef long long ll;
typedef unsigned int uint;

#define FOR(I,A,B) for(uint I=(A);I<=(B);I++)
#define REP(I,N) for(uint I=0;I<(N);I++)
#define VAR(V,I) typeof(I) V=(I)
#define FOREACH(I,C) for(VAR(I,(C).begin());I != (C).end(); I++)

#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

#define INTPINF  2147483647
#define INTNINF  2147483648
#define UINTINF  4294967295U
#define LLPINF   9223372036854775807LL
#define LLNINF   9223372036854775808LL
#define ULLINF   18446744073709551615ULL
#define INF      6666

int main() {
    uint ts;
    char str[101];
    uint dp[100][1000];
    uint qs[1000];
    map<string,uint > engines;
    uint switches;
    
    scanf("%d", &ts);
    REP(t, ts) {
        uint s;
        uint q;
        
        engines.clear();
        scanf("%d", &s);
        REP (i, s) {
            str[0] = 0;
            while (str[0] == 0) {
                gets(str);
            }
            engines.insert(MP(string(str), i));
        }
        scanf("%d", &q);
        REP (i, q) {
            str[0] = 0;
            while (str[0] == 0) {
                gets(str);
            }
            qs[i] = engines.at(string(str));
        }
        
        REP(j, q) {
            uint minchanged = INF;
            REP(i, s) {
                dp[i][j] = INF;
                if (j == 0) {
                    if (qs[j] != i) dp[i][j] = 0;
                } else if (qs[j] != i) {
                    if (i > 0 && dp[i-1][j-1] != INF) 
                        dp[i][j] = dp[i-1][j-1] + 1;
                    if (i < s-1 && dp[i+1][j-1] != INF) {
                        dp[i][j] = min(dp[i][j], dp[i+1][j-1] + 1);
                    }
                    minchanged = min(minchanged, dp[i][j]);
                }
            }
            REP(i, s) {
                if (j > 0 && qs[j] != i) {
                    dp[i][j] = min(minchanged, dp[i][j-1]);
                }
            }
        }
        
        switches = INF;
        if (q == 0) switches = 0;
        else {
            REP(i, s) {
                switches = min(switches, dp[i][q-1]);
            }
        }
        
        printf("Case #%d: %d\n", t+1, switches);
    }

	return 0;
}
