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
#define eps 1e-13
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }

double x[2][2000],y[2][2000];

double area(double q)
{
    double wyn=0.0;
    int i=1;
    while(q>x[0][i])
    {
        wyn+=(y[0][i-1]+y[0][i])*.5*(x[0][i]-x[0][i-1]);
        //DBG(wyn);
        i++;
    }
    double dl=x[0][i]-x[0][i-1];
    double dl1=q-x[0][i-1];
    //DBG(i);
    //DBG(dl1);
    //DBG(wyn);
    if (dl1>eps)
    {
        double yu=y[0][i-1]+(dl1/dl)*(y[0][i]-y[0][i-1]);
        wyn+=dl1*(y[0][i-1]+yu)*0.5;
    }
    //DBG(wyn);
    i=1;
    while(q>x[1][i])
    {
        wyn-=(y[1][i-1]+y[1][i])*.5*(x[1][i]-x[1][i-1]);
        i++;
    }
    dl=x[1][i]-x[1][i-1];
    dl1=q-x[1][i-1];
    if (dl1>eps)
    {
        double yu=y[1][i-1]+(dl1/dl)*(y[1][i]-y[1][i-1]);
        wyn-=dl1*(y[1][i-1]+yu)*0.5;
    }
    return -wyn;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;cin>>t;
    REP(test,1,t)
    {
        int w,l,u,g;
       
        cin>>w>>l>>u>>g;
        //DBG(w);
        FOR(j,2) FOR(i,2000) x[j][i]=y[j][i]=0.0;
        FOR(i,l)
        {
            cin>>x[0][i]>>y[0][i];
            //y[0][i]+=2000;
        }
        FOR(i,u)
        {
            cin>>x[1][i]>>y[1][i];
            //y[1][i]+=2000;
        }
        printf("Case #%d:\n",test);
        double sum=area(w);
        //DBG(sum);
        
        FOR(i,g-1)
        {
            double ile=sum*(i+1);
            ile/=g;
            //DBG(ile);
            double lo=0.0,hi=w,mid;
            FOR(sdgsdg,200)
            {
                //DBG(lo);
                //DBG(hi);
                mid=(lo+hi)*.5;
                if (area(mid)>ile)
                    hi=mid;
                else 
                    lo=mid;
            }
            printf("%.12lf\n",lo);
        }

    }

    return 0;
}
