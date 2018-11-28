#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
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
#define LOLDBG1
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

vector<pair<double,double> > v;

int main()
{
    ios_base::sync_with_stdio(0);
    int X,S,T,t,N;
    double R;
    cin>>T;
    FOR(abc,T)
    {
        cin>>X>>S>>R>>t>>N;
        R-=S;
        v.clear();
        double bez=X;
        FOR(i,N)
        {
            int b,e;
            cin>>b>>e;
            double w;cin>>w;
            v.pb(mp(S+w,e-b));
            bez-=e-b;
        }
        v.pb(mp(S,bez));
        sort(ALL(v));
        DBG(v);
        double wyn1;
        double bieg=t;
        double czas=0;
        double wyn=0;
        //REPD(i,v.sz-1,0)
        FOR(i,v.sz)
        {
            double droga=v[i].se;
            //DBG(bieg);
            if (bieg>0.0)
            {
                if (bieg*(v[i].fi+R)>=droga)
                {
                    czas+=droga/(v[i].fi+R);
                    bieg-=droga/(v[i].fi+R);
                }
                else
                {
                    czas+=bieg;
                    droga-=bieg*(v[i].fi+R);
                    bieg=0.0;
                    czas+=droga/(v[i].fi);
                }
            }
            else
            {
                czas+=droga/(v[i].fi);
            }
        }
        wyn1=czas;
        REPD(i,v.sz-1,0)
        {
            double droga=v[i].se;
            //DBG(bieg);
            if (bieg>0.0)
            {
                if (bieg*(v[i].fi+R)>=droga)
                {
                    czas+=droga/(v[i].fi+R);
                    bieg-=droga/(v[i].fi+R);
                }
                else
                {
                    czas+=bieg;
                    droga-=bieg*(v[i].fi+R);
                    bieg=0.0;
                    czas+=droga/(v[i].fi);
                }
            }
            else
            {
                czas+=droga/(v[i].fi);
            }
        }
        wyn1=min(wyn1,czas);
        printf("Case #%d: %.10lf\n",abc+1,wyn1);
    }

    return 0;
}
