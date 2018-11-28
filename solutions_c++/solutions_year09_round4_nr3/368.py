#include <algorithm>
#include <iterator>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;

typedef vector<int> vi;
typedef vector<string> vs;

#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fd(i,a,b) for(int i=(a);i>=(b);--i)
#define pb(_v,_a) (_v).push_back(_a)
#define sz size()
#define range(_a) (_a).begin(),(_a).end()
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define init(m,v) memset((m), (v), sizeof((m)))
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

bool arr[16][16];
int answer[1<<20];
int cptbl[1<<20];
int stks;
bool compatible(int t) {
    int &retval = cptbl[t];
    if (retval != -1) return retval == 1;
    f(i,0,stks) {
        if (t & (1<<i) ) {
            f(j,i+1,stks) {
                if ((t & (1<<j)) && !arr[i][j]) { retval = 0;return false;}
            }
        }
    }
    retval = 1;
    return true;
}
int doOp(int val) {
    if (val == 0) return 0;
    int &retval = answer[val];
    if (retval != -1) return retval;
    int t = val;
    retval = 0;
    while (t) { // maximum value retval can get
        retval ++;
        t = t & (t-1);
    }
    t = val;
    do {
        if (compatible(t)) {
            retval = min(retval, 1+doOp(val ^ t));
        }
        t = (t-1) & val;
    } while (t);
    return retval;
}
int main() {
    int n;
    cin>>n;
    f(test,1,n+1) {
        ll ans = 0;
        int k;
        cin>>stks>>k;
        vector<vector<int> > stocks(stks);
        f(i,0,stks) {
            vi &stock = stocks[i];
            f(j,0,k) {
                int t;
                cin>>t;
                pb(stock, t);
            }
        }
        init(arr, false);
        init(answer, -1);
        init(cptbl, -1);
        f(i,0,stks) f(j,0,stks) {
            bool compatible = true;
            bool direction = (stocks[i][0] > stocks[j][0]);
            f(l,0,k) if (stocks[i][l] == stocks[j][l] || (direction != (stocks[i][l] > stocks[j][l])) ) { compatible = false; break; }
            arr[i][j] = compatible;
        }
        ans = doOp((1<<stks) - 1);
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
