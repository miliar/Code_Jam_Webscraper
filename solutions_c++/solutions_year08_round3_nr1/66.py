#include <algorithm>
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

int main() {
    int n;
    cin>>n;
    f(test,1,n+1) {
        ll ans = 0;
        int p,k,l;
        cin>>p>>k>>l;
        vector<ll> freq;
        f(i,0,l) {
            int t;
            cin>>t;
            pb(freq, t);
        }
        sort(range(freq));
        reverse(range(freq));
        int ind = 0;
        f(i,1,p+1) {
            if (ind == freq.sz) break;
            f(j,0,k) {
                if (ind < freq.sz) {
                    ans += i * freq[ind];
                    ind++;
                } else break;
            }
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
