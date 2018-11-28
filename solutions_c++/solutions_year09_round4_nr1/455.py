#include <iostream>
#include <vector>
#include <string.h>
#include <queue>
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


int n;
char mp[100][100];
map < vector<int>, int> ok, seen, d;


int main() {
    int kases = GI;
    FOR(kase,1,kases+1) {
        printf("Case #%d: ", kase);
        ok.clear();
        seen.clear();        
        n = GI;
        REP(i,n) scanf("%s", mp[i]);
        int val[n];
        memset(val,0,sizeof(val));
        REP(i,n) {
            for(int j = n-1; j >= 0; j--) {
                if(mp[i][j] == '1') {
                    val[i] = j;
                    break;   
                }
            }            
        }
        VI v;
        REP(i,n) v.pb(i);
        int ans = 0;
        bool changed = true;
        while(changed) {
            changed=false;
//            REP(i,v.sz) cout << v[i] <<" "; cout << endl;
            REP(i,v.sz) if(i < val[v[i]]){
                FOR(j,i+1,v.sz) if(val[v[j]] <= i) {
                    // bubble up
                    for(int k = j-1; k >= i; k--) {
                        swap(v[k], v[k+1]);
                    }
                    changed = true;
                    ans +=  j-i;
                    goto next;               
                }
                next:;
            }
            
        }
        cout << ans << endl;

   }







}
