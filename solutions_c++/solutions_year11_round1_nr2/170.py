#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <sstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define TWO(x) (1<<(x))
#define CONTAIN(S,x) (S & TWO(x))
using namespace std;

const double PI = acos(-1.0);

string a[10111], b[111], cur;
bool can[10111];
int Left, now, n, m, mask[10111];

bool match(int i) {
    REP(x,a[i].length())
        if (cur[x] != '_') {
            if (a[i][x] != cur[x]) return false;
        }
    return true;
}

bool check(char c) {
    FOR(i,1,n) if (can[i] && CONTAIN(mask[i], c-'a')) return true;
    return false;
}

void update(char c, int word) {
    if (!check(c)) return ;
    if (Left == 1) return ;
    
//    cout << "Guess: " << c << endl;
    
    REP(x,cur.length())
        if (a[word][x] == c) cur[x] = c;
    
    bool contains = CONTAIN(mask[word], c-'a');
    if (!contains) now++;
        
    FOR(i,1,n)
    if (can[i])
        if (contains && !CONTAIN(mask[i], c-'a')) { can[i] = false; Left--; }
        else if (!contains && CONTAIN(mask[i],c-'a')) { can[i] = false; Left--; }
        else if (contains && !match(i)) { can[i] = false; Left--; }
        else {
            REP(x,cur.length())
                if (a[i][x] == c && cur[x] != c) {
                    can[i] = false;
                    Left--;
                    break;
                }
        }
        
//    FOR(i,1,n) if (can[i]) cout << a[i] << ' '; cout << endl;
}

int main() {
    freopen("B-small.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; cin >> test;
    FOR(t,1,test) {
        cout << "Case #" << t << ":";
        cin >> n >> m;
        FOR(i,1,n) cin >> a[i];
        FOR(i,1,m) cin >> b[i];
        
        FOR(i,1,n) {
            mask[i] = 0;
            REP(x,a[i].length()) {
                mask[i] = mask[i] | TWO(a[i][x]-'a');
            }
        }
        
        FOR(turn,1,m) {
            int best = -1, save = -1;
            
            FOR(i,1,n) {
//                cout << "Try word " << i << ' ' << a[i] << endl;
                cur = a[i]; now = 0;
                Left = n;
                memset(can, true, sizeof can);
                FOR(j,1,n) if (a[j].length() != cur.length()) { can[j] = false; Left--; }
                
//                FOR(j,1,n) cout << can[j] << ' '; cout << endl;
                
                REP(x,cur.length()) cur[x] = '_';
                
                REP(pos,26) update(b[turn][pos], i);
                
//                cout << "Need : " << now << endl;
                    
                if (now > best) {
                    best = now;
                    save = i;
                }
            }
            
            cout << ' ' << a[save];
        }
        puts("");
    }
    return 0;
}
