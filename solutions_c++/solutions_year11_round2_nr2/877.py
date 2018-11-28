using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <memory.h>
#include <iostream>
#include <algorithm>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
#define ABS(a) ((a)<0?(-(a)):(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef long long ll;

pdd nums[500];
int c, d;

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;cin>>t;
    FOR1(cno, t) {
        cin>>c>>d;
        double v=0;
        FOR(i, c) {
            cin>>nums[i].first>>nums[i].second;
            v += nums[i].second;
        }

        double low = 0;
        double high = d*v;
        while(low+1e-8 < high) {
            double mid = (low+high)/2.;
            double now = -(1ll<<60);
            //cout<<"Now "<<mid<<endl;
            bool possible = true;
            FOR(i, c) {
                FOR(j, nums[i].second) {
                    double goTo = nums[i].first-mid;
                    if(goTo < now+d) { goTo = now+d; }

                    //cout<<"Moving "<<nums[i].first<<" to "<<goTo<<endl;

                    if( ABS(goTo-nums[i].first) > mid
                        || ABS(goTo - now) < d) {
                            //cout<<"-----Not possilbe"<<endl;
                        possible = false;
                        break;
                    }
                    now = goTo;
                }
                if(!possible) break;
            }
            if(!possible) low = mid;
            else high = mid;
        }
        //cout<<"Case #"<<cno<<": "<<low<<' '<<high<<endl;
        printf("Case #%d: %.8lf\n", cno, high);
    }
    return 0;
}

