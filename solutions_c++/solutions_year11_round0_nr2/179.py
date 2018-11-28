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
using namespace std;

const double PI = acos(-1.0);

char com[300][300], opp[300][300];
int top;
char st[300];

int main() {
    freopen("B1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        memset(com, 0, sizeof com);
        memset(opp, 0, sizeof opp);
        top = 0;
        
        cout << "Case #" << test << ": ";
        int c, d, n;
        cin >> c;
        string s;
        while (c--) {
            cin >> s;
            com[s[0]][s[1]] = s[2];
            com[s[1]][s[0]] = s[2];
        }
        
        cin >> d;
        while (d--) {
            cin >> s;
            opp[s[0]][s[1]] = 1;
            opp[s[1]][s[0]] = 1;
        }
        
        cin >> n;
        cin >> s;
        REP(i,n) {
            char c = s[i];
            st[++top] = c;
            while (top > 1 && com[st[top-1]][st[top]]) {
                st[top-1] = com[st[top-1]][st[top]];
                top--;
            }
            
            FOR(x,1,top)
                if (opp[st[x]][st[top]]) {
                    top = 0;
                    break;
                }
        }
        cout << "[";
        if (top) {
            FOR(i,1,top-1) cout << st[i] << ", ";
            cout << st[top];
        }
        cout << "]\n";
    }
    return 0;
}
