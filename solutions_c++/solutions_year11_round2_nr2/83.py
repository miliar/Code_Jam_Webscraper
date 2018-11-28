#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <sstream>
#include <iostream>
#include <cstring>
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define REPD(i,x,v)for(int i=x;i>=v;i--)
#define FOR(i,v)for(int i=0;i<v;i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REMIN(x,y) (x)=min((x),(y))
#define REMAX(x,y) (x)=max((x),(y))
#define pb push_back
#define sz size()
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define IN(x,y) ((y).find((x))!=(y).end())
#define LOLDBG
#ifdef LOLDBG
#define DBG(vari) cout<<#vari<<" = "<<vari<<endl;
#define DBG2(v1,v2) cout<<(v1)<<" - "<<(v2)<<endl;
#else
#define DBG(vari)
#define DBG2(v1,v2)
#endif
#define CZ(x) scanf("%d",&(x));
#define CZ2(x,y) scanf("%d%d",&(x),&(y));
#define ALL(x) (x).begin(),(x).end()
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }


vector<pii> v;
double d;

bool ok(double x)
{
    double poprz=v[0].fi-x;
    FOR(i,v.sz)
    {
        poprz=max(poprz,v[i].fi-x);
        double f=(v[i].se-1)*d;
        if (poprz+f>v[i].fi+x) return 0;
        poprz+=f+d;
    }
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    REP(test,1,t)
    {
        v.clear();
        int c;
        
        cin>>c>>d;
        v.resize(c);
        FOR(i,c)
        {
            cin>>v[i].fi>>v[i].se;
        }
        sort(ALL(v));
        double lo=0.0,hi=1e20,mid;
        FOR(sdgsdgs,1000)
        {
            mid=(lo+hi)*.5;
            if (ok(mid)) hi=mid;
            else lo=mid;
        }

        printf("Case #%d: %.15lf\n",test,hi);
        
    }

    return 0;
}
