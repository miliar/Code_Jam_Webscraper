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

struct plant {
    double x,y,r;
};
double dist(plant p1, plant p2) {
    double x = p1.x - p2.x;
    double y = p1.y - p2.y;
    return sqrt(x*x + y*y);
}
int main() {
    int n;
    cin>>n;
    f(test,1,n+1) {
        double ans = 0;
        int plants;
        cin>>plants;
        vector<plant> ps(plants);
        f(i,0,plants) {
            plant &p = ps[i];
            cin>>p.x>>p.y>>p.r;
        }
        if (plants == 1) {
            ans = ps[0].r;
        } else if (plants == 2) {
            ans = max(ps[0].r, ps[1].r);
        } else if (plants == 3) {
            double d01 = (dist(ps[0], ps[1]) + ps[0].r + ps[1].r)/2;
            double d02 = (dist(ps[0], ps[2]) + ps[0].r + ps[2].r)/2;
            double d12 = (dist(ps[1], ps[2]) + ps[1].r + ps[2].r)/2;
            ans = max(d01, ps[2].r);
            double ans1 = max(d02, ps[1].r);
            ans = min(ans, ans1);
            ans1 = max(d12, ps[0].r);
            ans = min(ans, ans1);
        }
        cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
