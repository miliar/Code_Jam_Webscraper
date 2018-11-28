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
#define MAXPR 1000008
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }


bool sito[MAXPR+10];
vector<int> primes;


ll p,k,a,g;
void situj()
{
    FOR(i,MAXPR+1) sito[i]=1;
    REP(i,2,MAXPR) if (sito[i]) {primes.pb(i);for(int j=i;j<=MAXPR;j+=i) sito[j]=0;}
}


int main()
{
    ios_base::sync_with_stdio(0);
    situj();
    int T;
    cin>>T;
    FOR(abc,T)
    {
        ll n;cin>>n;
        ll wyn=0;
        FOR(i,primes.sz)
        {
            p=primes[i];
            int k=0;
            while(p<=n)
            {
                p*=primes[i];
                k++;
            }
            if (k>1) wyn+=k-1;
        }
        if (n!=1) wyn++;
        cout<<"Case #"<<abc+1<<": "<<wyn<<endl;

    }

    return 0;
}
