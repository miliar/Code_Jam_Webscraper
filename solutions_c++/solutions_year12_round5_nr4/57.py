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

int lit[200];
int alt[200];
int d[200][200];
int indeg[200];
int outdeg[200];
bool jest[200];
bool odw[200];

vi wie;

void dfs(int u)
{
    wie.pb(u);
    odw[u]=1;
    FOR(j,200)
    {
        if (d[u][j] && !odw[j])
        {
            dfs(j);
        }
    }
}

int main()
{
    FOR(i,200) lit[i]=i;
    FOR(i,200) alt[i]=i;
    alt['o']='0';
    alt['i']='1';
    alt['e']='3';
    alt['a']='4';
    alt['s']='5';
    alt['t']='7';
    alt['b']='8';
    alt['g']='9';
    int T;cin>>T;
    FOR(te,T)
    {
        int k;cin>>k;
        string s;cin>>s;
        int n=s.sz;
        FOR(i,200) FOR(j,200) d[i][j]=0;
        FOR(i,200) jest[i]=odw[i]=0;
        FOR(i,n-1)
        {
            string g=s.substr(i,2);
            FOR(a,2) FOR(b,2)
            {
                string h=g;
                if (a) h[0]=g[0]; else h[0]=alt[g[0]];
                if (b) h[1]=g[1]; else h[1]=alt[g[1]];
                jest[h[0]]=jest[h[1]]=1;
                d[h[0]][h[1]]=1;
                //DBG(h);
            }
        }
        FOR(i,200) indeg[i]=outdeg[i]=0;
        FOR(i,200) FOR(j,200) indeg[i]+=d[j][i];
        FOR(i,200) FOR(j,200) outdeg[i]+=d[i][j];
        int suma=0;
        int ile=0;
        FOR(i,200)
        {
            if (!jest[i]) continue;
            wie.clear();
            if (!odw[i]) dfs(i);
            bool dobrze=1;
            FOR(j,wie.sz)
            {
                int a=wie[j];
                if (indeg[a]!=outdeg[a])
                {
                    dobrze=0;
                    if (outdeg[a]>indeg[a]) suma+=outdeg[a]-indeg[a];
                }
            }
            
        }

        //DBG(suma);
        if (suma) suma--;
        FOR(i,200) FOR(j,200) suma+=d[i][j];
        printf("Case #%d: ",te+1);
        printf("%d\n",suma+1);
    }

    return 0;
}
