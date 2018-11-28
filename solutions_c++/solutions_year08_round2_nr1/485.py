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
    int N;
    cin>>N;
    f(tests, 1, N+1) {
        ll n,a,b,c,d,x,y,m;
        ll ans = 0;
        ll arr[3][3] = {0};
        vector< pair<ll, ll> > points;
        cin>>n>>a>>b>>c>>d>>x>>y>>m;
        f(i,0,n) {
            pb(points, make_pair(x,y));
            x = (x*a+b)%m;
            y = (y*c+d)%m;
        }
        sort(range(points));
        vector< pair<ll, ll> >::iterator newEnd = unique(range(points));
        points.erase(newEnd, points.end() );
        f(i,0,points.sz) {
            x = points[i].first;
            y = points[i].second;
            ans += arr[(3-(points[i].first%3))%3][(3-(points[i].second%3))%3];
            f(j,0,i) {
                ll x1 = points[j].first;
                ll y1 = points[j].second;
                arr[(x+x1)%3][(y+y1)%3]++;
            }
        }
        cout<<"Case #"<<tests<<": "<<ans<<endl;
    }
    return 0;
}
