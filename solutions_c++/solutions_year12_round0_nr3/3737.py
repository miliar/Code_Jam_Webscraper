#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <queue>
using namespace std;
#define out(x) (cout<<#x<<": "<<x<<endl)
const int maxint=0x7FFFFFFF;
typedef long long lint;
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

set<pair<int, int> > rec;

int a, b;

int mylog(int x) {
    if(x < 10) return 1;
    return mylog(x / 10) + 1;
}

int get10(int x) {
    int ret = 1;
    while(--x) ret *= 10;
    return ret;
}

int calc(int x) {
    int ret = 0;
    for (int i=10, j=get10(mylog(x)); i<=x; i*=10, j/=10) {
        int t = x / i + (x % i) * j;
        if (t > x && t <= b) {
            pair<int, int> p = make_pair(x, t);
            if(rec.find(p) == rec.end()) {
                rec.insert(p);
                ++ ret;
            }
        }
    }
    return ret;
}

int main()
{
    int z, ans;
    scanf("%d", &z);
    for (int ca=1; ca<=z; ++ca) {
        scanf("%d%d", &a, &b);
        ans = 0;
        rec.clear();
        for (int i=a; i<b; ++i) {
            ans += calc(i);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}

