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
#include <complex>
#define eps 1e-8
#define DET(X,Y,Z) ((Y.fi-X.fi)*(Z.se-X.se)-(Z.fi-X.fi)*(Y.se-X.se))
#define M 25
using namespace std;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef complex<double> zesp;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }


bool przecinanie(pdd A, pdd B,pdd C, pdd D)//wlasciwe
{
    double a1,a2;
    a1=DET(A,B,C);
    a2=DET(A,B,D);
    if (!((a1<-eps && a2>eps) || (a2<-eps && a1>eps))) return 0;
    a1=DET(C,D,A);
    a2=DET(C,D,B);
    if (!((a1<-eps && a2>eps) || (a2<eps && a1>eps))) return 0;
    return 1;
}

pdd wiel[10000];
pdd pkt[M+2];
vector<int> wie[M+2];
vector<pii> kr;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    REP(test,1,t)
    {
        int n,m;
        cin>>n>>m;
        wiel[0]=mp(1,0);
        double alfa=2*M_PI/n;
        zesp ob=zesp(cos(alfa),sin(alfa));
        zesp z(1,0);
        REP(i,1,n-1)
        {
            z*=ob;
            wiel[i]=mp(z.real(),z.imag());
            //DBG(wiel[i]);
        }
        pkt[0]=mp(0.9,0);
        alfa=2*M_PI/M;
        ob=zesp(cos(alfa),sin(alfa));
        zesp w(0.9,0);
        REP(i,1,M-1)
        {
            w*=ob;
            pkt[i]=mp(w.real(),w.imag());
            //DBG(wiel[i]);
        }
        FOR(i,M) wie[i].clear();
        kr.resize(m);
        FOR(i,m)
        {
            cin>>kr[i].fi;
            kr[i].fi--;
        }
        FOR(i,m)
        {
            cin>>kr[i].se;
            kr[i].se--;
        }
        FOR(i,M)
        {
            //DBG(pkt[i]);
            FOR(u,n)
            {
                bool ok=1;
                FOR(j,m)
                {
                    if (przecinanie(wiel[kr[j].fi],wiel[kr[j].se],pkt[i],wiel[u])) ok=0;
                }
                if (ok) wie[i].pb(u);
                
            }
            //DBG(wie[i]);
        }
        vector<int> kol(n);
        vector<int> wyn;
        bool jest[10];
        int k=0;
        bool ok=1;
        while(ok)
        {
            ok=0;
            k++;
            FOR(sdgsdg,1000000/2)
            {
                if (ok) break;
                FOR(i,n) kol[i]=rand()%k;
                bool zle=0;
                FOR(i,M)
                {
                    FOR(j,k) jest[j]=0;
                    FOR(j,wie[i].sz) jest[kol[wie[i][j]]]=1;
                    int ile=0;
                    FOR(j,k) ile+=jest[j];
                    if (ile!=k)
                    {
                         zle=1;
                         break;
                    }
                }
                if (!zle)
                {
                    ok=1;
                    wyn=kol;
                }
            }
        }
        k--;
        //DBG(wyn);

        printf("Case #%d: %d\n",test,k);
        FOR(i,n) printf("%d ",wyn[i]+1);
        puts("");
        
    }

    return 0;
}
