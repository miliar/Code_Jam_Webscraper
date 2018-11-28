// author: amit
#include <cstdio>
#include <iostream>
#include <cmath>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define TR(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define REP(i, n) for(int i = 0; i<(n); i++)
#define REPSE(i, s, e) for(int i = s; i <(e); i++)
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define FILL(x, c) memset(x, c, sizeof(x))
#define ALL(x) x.begin(), x.end()
#define FIN(x, c) (x.find(c)!=x.end())
#define IN(x, c) (find(x.begin(), x.end(), c)!=x.end())

#define SORT(x) sort(x.begin(), x.end())
#define SS {int t; scanf("%d", &t), t}
//

LL a[1111111];

LL fast[1111111];
LL slow[1111111];

struct node {
    int idx;
    LL diff;
    node(LL _d, int _idx) {
        idx = _idx;
        diff = _d;
    }

    bool operator<(const node & b) const {
        return diff>b.diff;
    }
};

vector<node> v;
int main() {
    freopen("B-large.in.txt", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tcase;
    scanf("%d", &tcase);

    for(int testcase = 1; testcase <= tcase; testcase++) {
        LL n, t, l, c;
        cin>>l>>t>>n>>c;

        REP(i, c) cin>>a[i];
        v.clear();
        //printf("C's: ");
        REP(i, n) {
            a[i] = a[i%c];
            //printf("%d ", a[i]);
        }

        LL total = 0;
        REP(i, n) {
            if(total >= t) {
                fast[i] = a[i];
                slow[i] = a[i]*2;
                v.push_back(node(a[i], i));
            } else
            if((total+a[i]*2) > t) {
                fast[i] = (t-total) + a[i]-(t-total)/2;
                slow[i] = 2*a[i];
                v.push_back(node(slow[i]-fast[i], i));
            }
            else {
                fast[i] = slow[i] = a[i]*2;
                v.push_back(node(0, i));
            }
            total += a[i]*2;
        }

        sort(ALL(v));

        LL mx = v.size();
        LL sub = 0;
        int cnt = 0;
        LL ans = 0;
        REP(i, mx) {
            if(cnt<l)
             ans += fast[v[i].idx];
            else
             ans += slow[v[i].idx];
            cnt++;
        }


        printf("Case #%d: ", testcase);
        cout<<ans<<"\n";
        //////
    }
}
