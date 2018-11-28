#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <climits>

#include <cstdlib>
#include <algorithm>
#include <cmath>

#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <ctime>

using namespace std;

typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

#define FOR(i,n1,n2) for(int i=n1;i<n2;i++)
#define FORD(i,n1,n2) for(int i=n1;i>=n2;i--)
#define FORE(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define PB push_back
#define MP make_pair
#define SZ(i) i.size()
#define FIR first
#define SEC second

int main() {
    int t;
    cin >> t;
    FOR(k,1,t+1) {
        int c;
        cin >> c;
        vector<string> ce(c);
        FOR(i,0,c) cin >> ce[i];
        int d;
        cin >> d;
        vector<string> de(d);
        FOR(i,0,d) cin >> de[i];

        int n;
        cin >> n;
        string s;
        cin >> s;

        string res="";

        FOR(i,0,n) {
            if (SZ(res)==0) res+=s[i];
            else {
                bool ok=false;
                FOR(w,0,c) {
                    if ((s[i]==ce[w][1] && res[SZ(res)-1]==ce[w][0]) ||
                        (s[i]==ce[w][0] && res[SZ(res)-1]==ce[w][1])) {
                        res.resize(SZ(res)-1);
                        res+=ce[w][2];
                        ok=true;
                        break;
                    }
                }
                if (!ok) {
                    FOR(w,0,d) {
                        if (s[i]==de[w][0]) {
                            FOR(j,0,SZ(res)) if (res[j]==de[w][1]) {
                                res="";
                                ok=true;
                                break;
                            }
                        }
                        if (!ok && s[i]==de[w][1]) {
                            FOR(j,0,SZ(res)) if (res[j]==de[w][0]) {
                                res="";
                                ok=true;
                                break;
                            }
                        }
                    }

                }
                if (!ok) res+=s[i];
            }
        }

        cout << "Case #" << k << ": ";
        cout << "[";
        if (SZ(res)) {
            FOR(i,0,SZ(res)-1) cout << res[i] << ", ";
            cout << res[SZ(res)-1];
        }
        cout << "]" << endl;
    }
    return 0;
}
