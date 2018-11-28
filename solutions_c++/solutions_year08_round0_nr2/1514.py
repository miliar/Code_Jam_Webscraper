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

int getTime() {
    int hr, min;
    char c;
    cin>>hr>>c>>min;
    return hr*60+min;
}
int main() {
    int n;
    cin>>n;
    f(testCase,0,n) {
        int ansA = 0, ansB = 0;
        int t;
        cin>>t;
        int na, nb;
        cin>>na>>nb;
        vector<pair<int, int> > ea, eb;
        int ta = 0, tb = 0;
        char c;
        f(i,0,na) {
            pb(ea, make_pair(getTime(), 1) );
            pb(eb, make_pair(getTime() + t, 0) );
        }
        f(i,0,nb) {
            pb(eb, make_pair(getTime(), 1) );
            pb(ea, make_pair(getTime() + t, 0) );
        }
        
        sort(range(ea));
        sort(range(eb));
        int i=0,j=0;
        while (i<ea.sz && j<eb.sz) {
            if (ea[i].first < eb[j].first) {
                if (ea[i].second == 0) ta++;// can start again from here. 
                else {
                    if (ta > 0) ta--;
                    else ansA++;
                }
                i++;
            } else {
                if (eb[j].second == 0) tb++;
                else {
                    if (tb > 0) tb--;
                    else ansB++;
                }
                j++;
            }
        }
        cout<<"Case #"<<testCase+1<<": "<<ansA<<" "<<ansB<<endl;
    }
    return 0;
}
