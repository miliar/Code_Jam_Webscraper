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
        int n;
        cin >> n;
        queue<int> O,B;
        queue<pair<string, int> > Q;
        FOR(i,0,n) {
            string s;
            cin >> s;
            int x;
            cin >> x;
            if (s=="O") O.push(x);
            else B.push(x);
            Q.push(MP(s,x));
        }

        int res=0;
        int pozo=1,pozb=1;
        while(!Q.empty()) {
            int o,b;
            if (O.empty()) o=9999999999;
            else o=O.front();
            if (B.empty()) b=9999999999;
            else b=B.front();

            string who=Q.front().first;
            Q.pop();
            if (who=="O") {
                O.pop();
                while(pozo!=o) {
                    if (pozo<o) pozo++; else pozo--;
                    if (pozb<b) pozb++;
                    else if (pozb>b) pozb--;
                    res++;
                }
                res++;
                if (pozb<b) pozb++;
                else if (pozb>b) pozb--;
            }
            else {
                B.pop();
                while(pozb!=b) {
                    if (pozb<b) pozb++; else pozb--;
                    if (pozo<o) pozo++;
                    else if (pozo>o) pozo--;
                    res++;
                }
                res++;
                if (pozo<o) pozo++;
                else if (pozo>o) pozo--;
            }
        }
        cout << "Case #" << k << ": " << res << endl;
    }
    return 0;
}
