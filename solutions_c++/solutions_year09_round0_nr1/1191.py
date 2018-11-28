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

vs strs;
bool notAvailable[5000];
bool avail[26];
int main() {
    int n, l, d;
    cin>>l>>d>>n;
    f(i,0,d) {
        string s;
        cin>>s;
        pb(strs, s);
    }
    f(test,1,n+1) {
        ll ans = 0;
        string pat;
        cin>>pat;
        init(avail,false);
        init(notAvailable, false);
        int currentPatternIdx = 0;
        f(i,0,l) {
            f(j,0,26) avail[j] = false;
            if (pat[currentPatternIdx] != '(') {
                avail[pat[currentPatternIdx]-'a'] = true;
            } else {
                currentPatternIdx++;
                while (pat[currentPatternIdx] != ')') {
                    avail[pat[currentPatternIdx]-'a'] = true;
                    currentPatternIdx++;
                }
            }
            currentPatternIdx++;
            f(j,0,d) {
                if (!notAvailable[j]) {
                    if (!avail[strs[j][i]-'a']) {
                        notAvailable[j] = true;
                    }
                }
            }
        }
        f(i,0,d) if (!notAvailable[i]) ans++;
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
