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
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }

double wp[1000],owp[1000],oowp[1000];
string s[1000];

int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    REP(test,1,t)
    {
        int n;cin>>n;
        FOR(i,n) cin>>s[i];
        FOR(i,n)
        {
            double ile=0.0,ilew=0.0;
            FOR(j,n) if (s[i][j]!='.')
            {
                ile+=1;
                if (s[i][j]=='1') ilew+=1;
            }
            wp[i]=ilew/ile;
        }
        FOR(i,n)
        {
            double ile=0.0,ilew=0.0;
            double z=0;
            FOR(j,n) if (s[i][j]!='.')
            {
                double ile1=0.0,ile1w=0.0;
                FOR(k,n) if (s[j][k]!='.' && k!=i)
                {
                    ile1+=1;
                    if (s[j][k]=='1') ile1w+=1;
                }
                ile+=1;
                ilew+=ile1w/ile1;
            }
            owp[i]=ilew/ile;
        }
        FOR(i,n)
        {
            double ile=0.0,ilew=0.0;
            FOR(j,n) if (s[i][j]!='.')
            {
                ile+=1;
                ilew+=owp[j];
            }
            oowp[i]=ilew/ile;
        }

        printf("Case #%d:\n",test);
        FOR(i,n)
        {
            printf("%.12lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }
    }

    return 0;
}
