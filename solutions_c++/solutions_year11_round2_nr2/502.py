#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int t;
int c, d, n;
vector<int> a;

bool check(double ans) {
    double left = -1e100;
    for (int i = 0; i < n; ++i) {
        if (left + d <= a[i] - ans) {
            left = a[i] - ans;
        } else if (left + d <= a[i] + ans) {
            left = left + d;
        } else {
            return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    for (int v = 1; v <= t; ++v) {
        scanf("%d%d", &c, &d);
        a.clear();
        n = 0;
        for(int i = 0;i < c; ++i){
            int x,y;
            scanf("%d%d",&x,&y);
            n += y;
            while(y--) a.push_back(x);
        }
        sort(a.begin(),a.end());
        if(check(0)) {printf("Case #%d: %.4f\n",v,0.0);continue;}
        double l = 0,r = 1,mid;
        while(!check(r)) r += r;
        while(r - l >= 1e-4){
            mid = (l+r)/2.0;
            if(check(mid)) r = mid;
            else l = mid;
        }
        printf("Case #%d: %.4f\n",v,(l+r)/2.0);
    }
    return 0;
}

