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

#define MMM 1001
bool comp[MMM];
bool seen[MMM];
int main() {
    int c;
    vector<ll> primes;
    f(i,2,MMM) {
        if (!comp[i]) {
            pb(primes, i);
            for (int j=i+i;j<MMM;j+=i) {
                comp[j] = true;
            }
        }
    }
    cin>>c;
    f(tests,1,c+1) {
        ll a,b,p;
        cin>>a>>b>>p;
        init(seen, false);
        int ans = 0;
        f(i,0,primes.sz) {
            if (primes[i] < p) continue;
            vi candidates;
            f(j,a,b+1) {
                if (!(j%primes[i])) {
                    pb(candidates, j);
                }
            }
            bool alreadySeen = false;
            f(j,0,candidates.sz) {
                if (seen[candidates[j]]) {
                    alreadySeen = true;
                }
                seen[candidates[j]] = true;
            }
            if (!alreadySeen && candidates.sz > 0) ans++;
        }
        f(i,a,b+1) if (!seen[i]) ans++;
        cout<<"Case #"<<tests<<": "<<ans<<endl;
    } 
    return 0;
}
