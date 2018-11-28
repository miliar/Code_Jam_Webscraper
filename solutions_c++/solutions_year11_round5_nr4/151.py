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
#define ull unsigned long long
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
#define eps 1e-13
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }

string s;




int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    REP(test,1,t)
    {
        cin>>s;
        while(1)
        {
            string g=s;
            ull wz=0;
            ull zn=0;
            FOR(i,s.sz)
            {
                if (s[i]=='?') zn+=(1LL<<(s.sz-i-1));
                else wz+=(1LL<<(s.sz-i-1))*(s[i]-'0');
            }
            ll w=0;
            //DBG(g);
            while(1)
            {
                ll z=w*w;
                if (((z^wz)|zn)==zn)
                {
                    break;
                }
                w++;
            }
            if (1)
            {
                cout<<"Case #"<<test<<": ";
                g="";
                w*=w;
                while(w)
                {
                    g+=('0'+(w%2));
                    w/=2;
                }
                REPD(i,g.sz-1,0) cout<<g[i];
                cout<<endl;
                break;
            }
        }

    }

    return 0;
}
