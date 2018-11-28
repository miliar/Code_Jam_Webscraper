#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstring>
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define REPD(i,x,v)for(int i=x;i>=v;i--)
#define FOR(i,v)for(int i=0;i<v;i++)
#define FORE(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REMIN(x,y) (x)=min((x),(y))
#define REMAX(x,y) (x)=max((x),(y))
#define pb push_back
#define sz size()
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define IN(x,y) ((y).find((x))!=(y).end())
#define un(v) v.erase(unique(ALL(v)),v.end())
#define LOLDBG
#ifdef LOLDBG
#define DBG(vari) cerr<<#vari<<" = "<<vari<<endl;
#define DBG2(v1,v2) cerr<<(v1)<<" - "<<(v2)<<endl;
#else
#define DBG(vari)
#define DBG2(v1,v2)
#endif
#define CZ(x) scanf("%d",&(x));
#define CZ2(x,y) scanf("%d%d",&(x),&(y));
#define CZ3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z));
#define ALL(x) (x).begin(),(x).end()
#define tests int dsdsf;cin>>dsdsf;while(dsdsf--)
#define testss int dsdsf;CZ(dsdsf);while(dsdsf--)
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }
#define INF 1000000000
ll X[100000];
ll Y[100000];

int main()
{
    int T;cin>>T;
    FOR(te,T)
    {
        int n;cin>>n;
        ll a,b;
        cin>>a>>b;
        vector<pair<ll,int> > v(n);
        FOR(i,n)
        {
            cin>>v[i].fi;
            v[i].se=i;
        }
        sort(ALL(v));
        reverse(ALL(v));
        vector<pair<ll,ll> > poz;
        poz.pb(mp(-INF,-INF));
        FOR(i,n)
        {
            //DBG(poz);
            bool jest=0;
            FOR(j,poz.sz)
            {
                ll x=poz[j].fi;
                ll y=poz[j].se;
                x+=v[i].fi;
                REMAX(x,0LL);
                y+=v[i].fi;
                REMAX(y,0LL);
                //DBG(mp(x,y));
                if (x>a || y>b) continue;
                bool ok=1;
                FOR(k,i)
                {
                    if (abs(X[k]-x)<v[i].fi+v[k].fi && abs(Y[k]-y)<v[i].fi+v[k].fi)
                    {
                        ok=0;
                        break;
                    }
                }
                if (!ok) continue;
                //DBG("OK");
                jest=1;
                X[i]=x;
                Y[i]=y;
                swap(poz[j],poz.back());
                poz.pop_back();
                poz.pb(mp(x-v[i].fi,y+v[i].fi));
                poz.pb(mp(x+v[i].fi,y-v[i].fi));
                sort(ALL(poz));
                break;
            }
            if (!jest)
            {
                cerr<<"LIPA";
                exit(0);
            }
            
        }
        printf("Case #%d: ",te+1);
        FOR(i,n)
        {
            FOR(j,n)
            {
                if (v[j].se==i)
                {
                    cout<<X[j]<<" "<<Y[j]<<" ";
                }
            }
        }
        cout<<"\n";
    }

    return 0;
}
