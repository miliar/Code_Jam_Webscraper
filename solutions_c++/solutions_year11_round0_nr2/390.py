#include <string>
#include <vector>
#include <algorithm>
#include <functional>
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

map<pair<int,int>,char> mut;
set<pair<int,int> > st;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    FOR(test,t)
    {
        int c,d,n;
        cin>>c;
        mut.clear();
        st.clear();
        FOR(i,c)
        {
            string s;cin>>s;
            mut[mp(s[0],s[1])]=s[2];
            mut[mp(s[1],s[0])]=s[2];
        }
        cin>>d;
        FOR(i,d)
        {
            string s;cin>>s;
            st.insert(mp(s[0],s[1]));
            st.insert(mp(s[1],s[0]));
        }
        cin>>n;
        string s;cin>>s;
        vector<char> stos;
        FOR(i,n)
        {
            char l=s[i];
            if (stos.sz==0)
            {
                stos.pb(l);
                continue;
            }
            char gora=stos.back();
            if (IN(mp(gora,l),mut))
            {
                stos.pop_back();
                stos.pb(mut[mp(gora,l)]);
                continue;
            }
            bool ok=1;
            FOR(j,stos.sz)
            {
                if (IN(mp(stos[j],l),st))
                {
                    ok=0;
                    break;
                }
            }
            if (ok) stos.pb(l);
            else stos.clear();
        }
        cout<<"Case #"<<test+1<<": [";
        FOR(i,stos.sz)
        {
            cout<<stos[i];
            if (i!=stos.sz-1) cout<<", ";
        }
        cout<<"]"<<endl;
    }

    return 0;
}
