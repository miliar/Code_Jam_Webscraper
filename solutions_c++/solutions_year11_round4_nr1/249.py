#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;

const double eps = 1e-9;
const int maxn = 1000010;

int cas, X, S, R, N;
int v[maxn], p[maxn];
double ans, t;

bool cmp(int a, int b )
{
    return v[a]<v[b];
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        cin>>X>>S>>R>>t>>N;
        for (int i = 0; i<X; i++ )
            v[i] = S;
        int a, b, c;
        for (int i = 0; i<N; i++ )
        {
            scanf("%d%d%d",&a,&b,&c);
            for (int j = a; j<b; j++ )
                v[j] += c;
        }
        ans = 0;
        for (int i = 0; i<X; i++ )
            ans += 1.0/(double)v[i];
        for (int i = 0; i<X; i++ ) p[i] = i;
        //cout<<"yes0"<<endl;
        sort(p, p+X, cmp);
        //cout<<"yes0.5"<<endl;
        for (int j = 0; j<X && t>eps; j++ )
        {
            //cout<<j<<' '<<p[j]<<endl;
            int i = p[j];
            int v2 = v[i]+R-S;
            //cout<<"yes1"<<endl;
            double t2 = 1.0/(double)v2;
            //cout<<i<<' '<<v2<<' '<<t2<<endl;
            if (t2 <= t)
            {
            //cout<<"yes2"<<endl;
                ans = ans - 1.0/(double)v[i] + 1.0/(double)v2;
                t -= t2;
            }
            else
            {
            //cout<<"yes3"<<endl;
                ans = ans - 1.0/(double)v[i];
                ans = ans + t;
                double x = 1 - t*v2;
                ans = ans + x/(double)v[i];
                t = 0;
            }
        }
        //cout<<"yes"<<endl;
        printf("Case #%d: %.8lf\n", run,ans);
    }
    //system("pause");
    return 0;
}
