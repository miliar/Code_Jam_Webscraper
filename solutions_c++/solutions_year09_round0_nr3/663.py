#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <algorithm>
using namespace std;
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int _; scanf("%d", &_); _;})
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF 1e8
#define MAX 104
typedef vector<int> VI;

#define MOD 10000
string wel = "welcome to code jam";
int main() {
    int testcases = GI;
    cin.ignore();
    string line;
    FOR(kase,1,testcases+1) {
        getline(cin,line);
        int cnt = 0, dp[line.sz][wel.sz];
        memset(dp,0,sizeof(dp));
        REP(i,line.sz) if(line[i] == wel[0]) dp[i][0] = 1;
        
        FOR(k,1,wel.sz) {
            REP(i,line.sz) if(line[i] == wel[k]) {
                REP(j,i) if(line[j] == wel[k-1]) {
                    dp[i][k] += dp[j][k-1];
                    dp[i][k] %= MOD;
                }
            }
        }
        int ans = 0;
        REP(i,line.sz) ans += dp[i][wel.sz-1], ans %= MOD;
        printf("Case #%d: %04d\n", kase, ans);
    }
 
}





			
