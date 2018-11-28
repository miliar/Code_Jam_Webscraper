#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define forn(i,n) for(tint i=0;i<(n);i++)
#define dforn(i,n) for(tint i=(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

typedef long long tint;

tint solve(vector<tint>const&c,vector<tint>&m,tint x)
{
    tint pp=m.size();
    //cerr<<pp<<" "<<x<<endl;
    if(2*x>=pp)
    {
        tint a=x%(pp/2);
        if(m[2*a]<0 || m[2*a+1]<0)return 1000000000000LL;
        if(m[2*a]==0 || m[2*a+1]==0)return c[x];else return 0;
    }
    tint mr=c[x]+solve(c,m,2*x)+solve(c,m,2*x+1);
    tint y=x,n=0;
    while(y){n++;y/=2;}
    forn(i,pp/(1<<(n-1)))m[(pp/(1<<(n-1)))*(x%(1<<(n-1)))+i]--;
    mr=min(mr,solve(c,m,2*x)+solve(c,m,2*x+1));
    //forn(i,m.size())cerr<<m[i]<<" ";cerr<<endl;
    forn(i,pp/(1<<(n-1)))m[(pp/(1<<(n-1)))*(x%(1<<(n-1)))+i]++;
    //cout<<x<<" "<<mr<<" "<<n<<endl;
    return mr;
}

int main()
{
    tint T;
    cin>>T;
    forn(t,T)
    {
        tint p;
        cin>>p;
        vector<tint>m(1<<p);
        forn(i,1<<p)cin>>m[i];
        vector<tint>c,d;
        forn(i,p)
        {
            d.clear();
            forn(j,1<<(p-i-1))
            {
                tint x;
                cin>>x;
                d.pb(x);
            }
            c.insert(c.begin(),all(d));
        }
        c.insert(c.begin(),0);
        cout<<"Case #"<<t+1<<": "<<solve(c,m,1)<<endl;
    }
}
