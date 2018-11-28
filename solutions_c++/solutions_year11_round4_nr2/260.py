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
#define MAXPR 1000008
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }


int t[505][505];

int R,C,D;

bool licz(int x,int y,int k)
{
    if (x+k>=R || y+k>=C) return 0;
    int xx=2*x+k;
    int yy=2*y+k;
    int sx=0,sy=0;
    REP(i,x,x+k) REP(j,y,y+k)
    {
        sx+=(2*i-xx)*t[i][j];
        sy+=(2*j-yy)*t[i][j];
    }

    REP(i,0,1) REP(j,0,1)
    {
        sx-=(2*(x+i*k)-xx)*t[x+i*k][y+j*k];
        sy-=(2*(y+j*k)-yy)*t[x+i*k][y+j*k];
    }
    //DBG(k);
    if (x==1 && y==1)
    {
        DBG(x);
        DBG(y);
        DBG(k);
        DBG(sx);
        DBG(sy);
    }

    if (sx==0 && sy==0) return 1;
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    FOR(abc,T)
    {
        
        cin>>R>>C>>D;
        FOR(i,R)
        {
            string s;cin>>s;
             FOR(j,C) t[i][j]=s[j]-'0';
        }
        int best=0;
        FOR(i,R) FOR(j,C) FOR(k,20)
        {
            if (licz(i,j,k)) REMAX(best,k);
        }
        best+=1;
        if (best>=3)
        cout<<"Case #"<<abc+1<<": "<<best<<endl;
        else
        cout<<"Case #"<<abc+1<<": IMPOSSIBLE"<<endl;

    }

    return 0;
}
