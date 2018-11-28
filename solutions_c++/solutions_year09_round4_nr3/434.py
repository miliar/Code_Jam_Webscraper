#include <iostream>
#include <vector>
#include <string.h>
#include <queue>
#include <cmath>
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
#define MAX 27
typedef vector<int> VI;
typedef double D;


int mp[100][100], n, k, mem[(1<<16) + 10], ok[1<<16 + 10];

int go(int mask) {
    if(mem[mask] != -1) return mem[mask];    
    if(mask == 0) return 0;
    
    int &res = mem[mask] = INF;
    for(int sub = mask; sub > 0; sub = (sub-1)&mask) {        
        if(ok[sub] && mask != sub) {
//    REP(i,n) if(mask&(1<<i)) cout << 1; else cout << 0; cout <<" to ";
//    REP(i,n) if(sub&(1<<i)) cout << 1; else cout << 0; cout << endl;

            REP(i,n) if(sub&(1<<i)) mask ^= 1<<i;
            res = min(res, 1+go(mask));
            REP(i,n) if(sub&(1<<i)) mask ^= 1<<i;
        }
    }
 //   REP(i,n) if(mask&(1<<i)) cout << 1; else cout << 0; cout <<" -> "<<res << endl;
    return res;

}
int main() {
    int kases = GI;
    FOR(kase,1,kases+1) {
        n = GI, k = GI;
        REP(i,n) REP(j,k) mp[i][j] = GI;
        memset(mem,-1,sizeof(mem));
        int N = 1<<n;
        REP(i,N) {
            ok[i] = 1;
            REP(j,n) if(i&(1<<j)) REP(q,n) if(q != j && i&(1<<q)) {
                REP(p,k-1) {
                    if(mp[j][p] < mp[q][p] && mp[j][p+1] < mp[q][p+1] || mp[j][p] > mp[q][p] && mp[j][p+1] > mp[q][p+1]) continue;
                    ok[i] = 0;
                    goto next;
                }
            }
            mem[i] = 1;
            next:;
            
        }
        int ans = 0;
        REP(i,n) ans |= 1<<i;
        ans = go(ans);
        
        printf("Case #%d: %d\n", kase, ans);
//        return 1;
    }


}
