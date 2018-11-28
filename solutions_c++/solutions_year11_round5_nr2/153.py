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
#define eps 1e-13
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }

int tab[111111];
int d[111111];
int n;


bool check(int x)
{
    if (n==0 && x>0) return 0;
    if (x==1) return 1;
    FOR(i,11111) d[i]=tab[i];
    int mx,pos;
    int ile=0;
    while(ile<n)
    {
        //DBG(ile);
        mx=0;
        FOR(i,10004)
        {
            if (d[i]>mx)
            {
                mx=d[i];
                pos=i;
            }
        }
        //DBG(mx);
        //DBG(pos);
        int k=0;
        while(1)
        {
            if (d[pos]==0) return 0;
            d[pos]--;
            ile++;
            k++;
            if (k>=x && d[pos+1]<=d[pos])
            {
                break;
            }
            else pos++;
        }
    }
    return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    REP(test,1,t)
    {
        cin>>n;
        FOR(i,11111) tab[i]=0;
        FOR(i,n)
        {
            int a;cin>>a;
            tab[a]++;
            
        }
        int lo=0,hi=n+1,mid;
        DBG(n);
        while(hi-lo>1)
        {
            
            mid=(lo+hi)/2;
            //DBG(mid);
            if (check(mid)) lo=mid;
            else hi=mid;
        }
        printf("Case #%d: %d\n",test,lo);
    }

    return 0;
}
