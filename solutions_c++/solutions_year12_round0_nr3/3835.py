#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <memory.h>
#include <stack>
#include <queue>
#include <deque>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <time.h>
#include <iomanip>

#define pi 3.1415926535897932
#define abs(x) ((x)>0?(x):-(x))
#define sqr(x) ((x)*(x))
#define fill(m,v) memset(m,v,sizeof(m))
#define sci(x) scanf("%d",&x)
#define scd(x) scanf("%lf",&x)
#define pri(x) printf("%d",x)
#define prd(x) printf("%lf",x)
#define oo 2000000000
#define fi first
#define se second
#define tr(container, iterator) for(typeof(container.begin()) iterator=container.begin(); it != container.end(); it++)
#define all(x) x.begin(), x.end()
#define y0 stupid_cmath
#define y1 very_stupid_cmath
#define ll long long
#define pb push_back
#define mp make_pair

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;

template <class T>
istream & operator>> (istream & in, vector <T> & v)
{
    for(size_t i_=0;i_<v.size();++i_)
        in>>v[i_];
    return in;
}

template <class T>
ostream & operator<< (ostream & out, vector <T> & v)
{
    for(size_t i_=0;i_<v.size();++i_)
        out<<v[i_]<<' ';
    out<<endl;
    return out;
}


int j,k,m,i,n;
int main()
{
    ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>n;
    ll a,b,x,h=0;
    ll res=0;
    string s;
    while (n--)
    {
        cin>>a>>b;
        s="";
        res=0;
        vi c(2000000,0);
        for(i=a;i<=b;++i)
        {
            x=j =i;
            if (c[j]==0)
            {
                m=0;
                while (j)
                {
                    j/=10;
                    m++;
                }
                m--;
                j=i;
                int d = pow(10,m),t=1,kol=0,p=d;
                for(k=0;k<m;++k)
                {
                    t*=10;
                    x = (j%t)*d+j/t;
                    d/=10;
                    if (x<p) continue;
                   // cout<<i<<' '<<x<<"!!"<<j<<" "<<j%t<<' '<<d<<' ';
                    if (x!=i && x>=a && x<=b && !c[x]){ kol++;c[x]=1;}
                }
                ll r=min(1,kol);

              //  cout<<i<<' '<<"("<<kol<<")\n";
                r = (1+kol)*kol/2;
                res+=r;
            }
        }
        h++;
        cout<<"Case #"<<h<<": "<<res<<endl;
    }
    return 0;
}
