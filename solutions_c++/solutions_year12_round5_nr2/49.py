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
typedef pair<short,short> pss;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }
#define MS 3002
pss p[MS*2][MS*2];
short sc[MS*2][MS*2];
bool cz[MS*2][MS*2];
int S;
vector<pii> r;
int M;

int dx[]={-1,-1,0,1,1,0};
int dy[]={-1,0,1,1,0,-1};

bool popr(int a,int b)
{
    if (a<1 || a>=2*S) return 0;
    if (b<1 || b>=2*S) return 0;
    return (b<=2*S-1-abs(S-a));
}

bool corner(int a,int b)
{
    return (mp(a,b)==mp(1,1) || mp(a,b)==mp(1,S) || mp(a,b)==mp(S,2*S-1) || mp(a,b)==mp(2*S-1,2*S-1) || mp(a,b)==mp(2*S-1,S) || mp(a,b)==mp(S,1));
}

vector<int> odp;


pss fszuk(int a,int b)
{
    if (p[a][b]==pss(a,b)) return pss(a,b);
    return p[a][b]=fszuk(p[a][b].fi,p[a][b].se);
}

bool funia(int a,int b,int c,int d)
{
    pss A=fszuk(a,b);
    pss B=fszuk(c,d);
    if (A!=B)
    {
        sc[A.fi][A.se]|=sc[B.fi][B.se];
        sc[B.fi][B.se]|=sc[A.fi][A.se];
        if (__builtin_popcount(sc[A.fi][A.se])>2) return 1;
        else p[A.fi][A.se]=B;
    }
    return 0;
}

void forki()
{
    REP(i,0,2*S) REP(j,0,2*S) p[i][j]=pss(i,j);
    REP(i,0,2*S) REP(j,0,2*S) cz[i][j]=0;
    REP(i,0,2*S) REP(j,0,2*S) sc[i][j]=0;
    REP(i,2,S-1) sc[1][i]=1;
    REP(i,2,S-1) sc[i][1]=2;
    REP(i,2,S-1) sc[i][S+i-1]=4;
    REP(i,2,S-1) sc[S+i-1][i]=8;
    REP(i,2,S-1) sc[2*S-1][S+i-1]=16;
    REP(i,2,S-1) sc[S+i-1][2*S-1]=32;
    FOR(i,M)
    {
        int a=r[i].fi;
        int b=r[i].se;
        
        bool jest=0;
        FOR(k,6)
        {
            int a1=a+dx[k];
            int b1=b+dy[k];
            if (!cz[a1][b1]) continue;
            //if (!popr(a1,b1)) continue;
            jest|=funia(a,b,a1,b1);
        }
        if (jest)
        {
            //cout<<i+1<<"\n";
            odp[i]|=4;
            return;
        }
        cz[a][b]=1;
    }
    //cout<<"niema\n";
}

pss rszuk(int a,int b)
{
    if (p[a][b]==pss(a,b)) return pss(a,b);
    return p[a][b]=rszuk(p[a][b].fi,p[a][b].se);
}

bool runia(int a,int b,int c,int d)
{
    pss A=rszuk(a,b);
    pss B=rszuk(c,d);
    if (A!=B)
    {
        if (corner(A.fi,A.se) && corner(B.fi,B.se)) return 1;
        if (corner(A.fi,A.se)) p[B.fi][B.se]=A;
        else p[A.fi][A.se]=B;
    }
    return 0;
}

void rogi()
{
    REP(i,0,2*S) REP(j,0,2*S) p[i][j]=pss(i,j);
    REP(i,0,2*S) REP(j,0,2*S) cz[i][j]=0;
    FOR(i,M)
    {
        int a=r[i].fi;
        int b=r[i].se;
        
        bool jest=0;
        FOR(k,6)
        {
            int a1=a+dx[k];
            int b1=b+dy[k];
            if (!cz[a1][b1]) continue;
            if (!popr(a1,b1)) continue;
            jest|=runia(a,b,a1,b1);
        }
        if (jest)
        {
            odp[i]|=1;
            return;
        }
        cz[a][b]=1;
    }
    //cout<<"niema\n";
}

pss riszuk(int a,int b)
{
    if (p[a][b]==pss(a,b)) return pss(a,b);
    return p[a][b]=riszuk(p[a][b].fi,p[a][b].se);
}

void riunia(int a,int b,int c,int d)
{
    pss A=riszuk(a,b);
    pss B=riszuk(c,d);
    if (A!=B)
    {
        p[A.fi][A.se]=B;
    }
}

void ringi()
{
    REP(i,0,2*S) REP(j,0,2*S) p[i][j]=pss(i,j);
    REP(i,0,2*S) REP(j,0,2*S) cz[i][j]=0;
    FOR(i,M)
    {
        int a=r[i].fi;
        int b=r[i].se;
        
        bool jest=0;
        FOR(k,6)
        {
            int a1=a+dx[k];
            int b1=b+dy[k];
            if (!cz[a1][b1]) continue;
            //if (!popr(a1,b1)) continue;
            int k1=(k+2)%6;
            if (!cz[a+dx[k1]][b+dy[k1]]) continue;
            if (riszuk(a1,b1)!=riszuk(a+dx[k1],b+dy[k1])) continue;
            int B1=0,B2=0;
            REP(l,1,1) B1+=!cz[a+dx[(k+l)%6]][b+dy[(k+l)%6]];
            REP(l,3,5) B2+=!cz[a+dx[(k+l)%6]][b+dy[(k+l)%6]];
            if (B1 && B2) jest=1;
        }
        if (jest)
        {
            odp[i]|=2;
            return;
        }
        FOR(k,6)
        {
            int a1=a+dx[k];
            int b1=b+dy[k];
            if (!cz[a1][b1]) continue;
            //if (!popr(a1,b1)) continue;
            int k1=(k+3)%6;
            if (!cz[a+dx[k1]][b+dy[k1]]) continue;
            if (riszuk(a1,b1)!=riszuk(a+dx[k1],b+dy[k1])) continue;
            int B1=0,B2=0;
            REP(l,1,2) B1+=!cz[a+dx[(k+l)%6]][b+dy[(k+l)%6]];
            REP(l,4,5) B2+=!cz[a+dx[(k+l)%6]][b+dy[(k+l)%6]];
            if (B1 && B2) jest=1;
        }
        if (jest)
        {
            odp[i]|=2;
            return;
        }
        
        FOR(k,6)
        {
            int a1=a+dx[k];
            int b1=b+dy[k];
            if (!cz[a1][b1]) continue;
            riunia(a,b,a1,b1);
        }
        cz[a][b]=1;
    }
    //cout<<"niema\n";
}



int main()
{
    int T;cin>>T;
    FOR(te,T)
    {
        r.clear();
        cin>>S>>M;
        r.resize(M);
        odp.clear();
        odp.resize(M,0);
        FOR(i,M) cin>>r[i].fi>>r[i].se;
        printf("Case #%d: ",te+1);
        rogi();
        forki();
        ringi();
        bool doned=0;
        FOR(i,M)
        {
            if(odp[i])
            {
                if (odp[i]==1) printf("bridge");
                if (odp[i]==2) printf("ring");
                if (odp[i]==4) printf("fork");
                if (odp[i]==3) printf("bridge-ring");
                if (odp[i]==5) printf("bridge-fork");
                if (odp[i]==6) printf("fork-ring");
                if (odp[i]==7) printf("bridge-fork-ring");
                printf(" in move %d\n",i+1);
                doned=1;
                break;
            }
            
        }
        if (!doned)
        {
            puts("none");
        }
    }

    return 0;
}
