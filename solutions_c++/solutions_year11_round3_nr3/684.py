#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int maxn = 11000;
const long long oo = 1000000000000000000;

long long l,h,g,a[maxn],gc[maxn],lc[maxn];

long long min1(long long &a, long long b)
{
    if (a > b) a = b;
}

long long get(long long x, long long y, long long l, long long r)
{
    long long z = y / x, ans1 = oo;
    for (long long i = 1; i <= floor(sqrt(z)); ++i)
    if (z % i ==0){
        if ((l <= i * x) && (i * x <= r)){
            min1(ans1, i * x);
        }
        if ((l <= z / i * x) && (z / i * x <= r)){
            min1(ans1, z / i * x);
        }
    }
    return ans1;
}

long long gcd(long long x, long long y)
{
    if (y == 0) return x;
    return gcd(y, x % y);
}

int sort(int l, int r)
{
    int i = l, j = r, x = a[(l + r) / 2];
    while (i <= j){
        while (a[i] < x) ++i;
        while (a[j] > x) --j;
        if (i <= j){
            int t = a[i];
            a[i] = a[j];
            a[j] = t;
            ++i;--j;
        }
    }
    if (l < j) sort(l, j);
    if (i < r) sort(i, r);
}

int main()
{
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    int t1;
    cin>>t1;
    for (int t2 = 1; t2 <= t1; ++t2){
        int n;
        cin>>n >>l >>h;
        for (int i = 1; i <= n; ++i)
            cin>>a[i];
        /*
        bool find = false;
        for (int i = l; i <= h; ++i){
            bool flag = true;
            for (int j = 1; j <= n; ++j)
                if ((i % a[j] != 0) && (a[j] % i != 0))
                    flag = false;
            if (flag) {find = true; cout<<i <<endl;break;}
        }
        if (!find) cout <<"no" <<endl;

        if (t2 == 12)
        n = n;
        */
        sort(1, n);
        a[n+1] = 0;lc[0] = 1;gc[n+1] = 0;
        long long ans = oo;
        for (int i = n; i >= 1; --i)
            gc[i] = gcd(a[i], gc[i+1]);
        if ((gc[1] % lc[0] == 0) && (l <= gc[1]))
            min1(ans,get(lc[0], gc[1], l, h));
        for (int i = 1; i <= n; ++i){
            g = gcd(lc[i-1], a[i]);
            if ((i == 1) || (log(lc[i-1]) + log(a[i]) - log(g) <= log(oo))){
                lc[i] = lc[i-1] / g * a[i];
            } else lc[i] = oo;
            if ((gc[i+1] % lc[i] == 0) && (l <= gc[i+1]))
                min1(ans,get(lc[i], gc[i+1], l, h));
            if ((l <= lc[i]) && (h >= lc[i]) && (gc[i+1] % lc[i] == 0)){
                min1(ans, lc[i]);
                break;
            }
        }
        if ((ans == oo) && (lc[n] <= h) && (lc[n] >= l)) min1(ans, lc[n]);
        if ((ans == oo) && (lc[n] < l)){
            long long ans1 = floor(l / lc[n]) * lc[n];
            if (l % lc[n] != 0) ans1 += lc[n];
            if (ans1 <= h) min1(ans, ans1);
        }
        cout<<"Case #" <<t2 <<": ";
        if (ans == oo) cout<<"NO"<<endl;
            else cout<<ans<<endl;
    }
}
