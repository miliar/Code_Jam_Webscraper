
/*ID: jbsu321
PROG: test
LANG: C++
*/

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>

#define ms(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define pi (2*acos(0))
#define oo 1<<29
#define dd double
#define ll long long
#define ff float
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100
#define SZ(a) (int)a.size()
#define all(a) a.begin(),a.end()
#define intlim 2147483648
#define rtintlim 46340
#define llim 9223372036854775808
#define rtllim 3037000499
#define ull unsigned long long

using namespace std;

vector<ll>V[10000];

void kapjap()
{
    for(int i=12; i<=1000;i++)
    {
        if(i>99)
        {
            ll x = 100 * (i%10) + (i/10);
            if((ll)(log10(x))==((ll)(log10(i))))
            {
                if(x<i) V[x].pb(i);
                else if(x>i) V[i].pb(x);
            }
            x = 10 * (i%100) + (i/100);

            if((ll)log10(x)==(ll)(log10(i)))
            {
                if(x<i) V[x].pb(i);
                else if(x>i) V[i].pb(x);
            }
        }
        else if(i>9)
        {
            ll x = 10 * (i%10) + (i/10);
            if((ll)(log10(x))==(ll)(log10(i)))
            {
                if(x<i) V[x].pb(i);
                else if(x>i) V[i].pb(x);
            }
        }
    }
//    cout<<"asd"<<endl;
    return;
}

void process()
{
    ll a, b, c, high, low, t, cas=1;
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin>>t;
    kapjap();
//    cout<<V[12][0]<<endl;


    while(t--)
    {
        cin>>low>>high;
        cout<<"Case #"<<cas++<<": ";

        ll cnt=0;
        for(int i=low;i<=high;i++)
        {
            for(int j=0;j<SZ(V[i]);j++)
            {
                if(V[i][j]<=high) cnt++;
            }
        }
        cout<<(cnt/2)<<endl;
    }
}

int main()
{
    process();
    return 0;
}
