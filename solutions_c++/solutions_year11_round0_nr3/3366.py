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
        vector<int> p(n);
        FOR(i,0,n) cin >> p[i];
        int res=-1;
        FOR(m,1,(1<<n)-1) {
            int r=0;
            int sean=0,paul=0;
            FOR(i,0,n) {
                if ((m>>i)&1) { r+=p[i]; sean^=p[i]; }
                else paul^=p[i];
            }
            if (sean==paul && r>res) res=r;
        }
        cout << "Case #" << k << ": ";
        if (res!=-1) cout << res << endl;
        else cout << "NO" << endl;
    }
    return 0;
}
