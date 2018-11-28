#include <iostream>
#include <cstdio>
using namespace std;
long long f[10000][3],a[10000],l,t,n,c,t1;

int min1(long long &a, long long b)
{
    if (a > b) a = b;
}

int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    cin>>t1;
    for (int t2 = 1; t2 <= t1; ++t2){
        cin>>l >>t >>n >>c;
        for (int i = 1; i <= n; ++i)
            if (i <= c) cin>>a[i];
                else a[i] = a[i - c];
        for (int i = 1; i <= n; ++i)
            for (int j = 0; j <= l; ++j){
                f[i][j] = f[i-1][j] + 2 * a[i];
                if (j != 0){
                    if (f[i-1][j-1] >= t)
                        min1(f[i][j], f[i-1][j-1] + a[i]);
                    else {
                        int x = t - f[i-1][j-1];
                        min1(f[i][j], f[i-1][j-1] + a[i] + x / 2);
                    }
                }
            }
        cout<<"Case #"<<t2<<": "<<f[n][l]<<endl;
    }
}
