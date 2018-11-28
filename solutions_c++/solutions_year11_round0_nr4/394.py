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

/*double rp[1005];

int main()
{
    ios_base::sync_with_stdio(0);
    rp[0]=0.0;
    rp[1]=0.0;
    REP(i,2,1000)
    {
        double w=i-1;
        REP(j,1,i-1)
        {
            w+=rp[j]+rp[i-j];
        }
        w/=double(i-1);
        rp[i]=w;
    }
    DBG(vector<double>(rp,rp+40));

    return 0;
}*/

int t[20000];
bool odw[20000];

int main()
{
    ios_base::sync_with_stdio(0);
    int tt;cin>>tt;
    FOR(test,tt)
    {
        int n;
        cin>>n;
        FOR(i,n)
        {
            int a;cin>>a;
            t[i]=a-1;
        }
        FOR(i,n) odw[i]=0;
        double w=0.0;
        FOR(i,n)
        {
            if (odw[i]) continue;
            int cykl=0;
            int k=i;
            while(!odw[k])
            {
                cykl++;
                odw[k]=1;
                k=t[k];
            }
            w+=cykl-1;
            if (cykl>1) w+=1;
        }
        printf("Case #%d: %.9f\n",test+1,w);
    }

    return 0;
}
