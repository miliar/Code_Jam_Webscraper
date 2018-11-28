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
#define MAX 27
typedef vector<int> VI;

int len, words, pats, yes[16][28], ok[5005], kase = 1;
string s;
const char OPEN = '(', CLOSE = ')';

int main() {
    len = GI, words = GI, pats = GI;
    vector <string> w;
    REP(i,words) {
        cin >> s;
        w.pb(s);
    }
    REP(i,pats) {
        cin >> s;
        memset(yes,0,sizeof(yes));
        int cur = -1, in = 0;
        string p = "";
        REP(j,s.sz) {
            if(s[j] == OPEN) in++, p += s[j];
            else if(s[j] == CLOSE) in--, p += s[j];
            else if(in == 0) p += OPEN, p += s[j], p += CLOSE;
            else p += s[j];
        }
        s = p;
        REP(j,s.sz) {            
            if(s[j] == OPEN) cur++;
            else if(s[j] != CLOSE) {
                yes[cur][s[j]-'a'] = 1;
            }
        }
        memset(ok,60,sizeof(ok));
        int ans = words;
        REP(j,len) {
            REP(k,words) if(ok[k]) {
                if(!yes[j][w[k][j]-'a']) {
                    ok[k] = 0, ans--;
                }
            }
        }
        printf("Case #%d: %d\n", kase++, ans);
    }






}





			
