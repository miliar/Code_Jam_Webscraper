#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
using namespace std;

typedef long long LL;
#define pb push_back
#define mp make_pair
#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define INF (int)1e9
#define fii freopen("ip.txt","r",stdin)
#define fio freopen("out.txt","w",stdout)
vector<vector<int> > v;
int mark[1011],ans;
void dfs(int n,int s)
{
    mark[n]=1;
    REP(i,v[n].size()) if(v[n][i]!=s) 
    {
         if(mark[v[n][i]]){ ans=1;return;}
         else dfs(v[n][i],s);
    }
    return;
}
int main()
{
    fii;fio;
    int t,n,m,kase=1;
    t=GI;
    while(t--)
    {
         n=GI;
         v.clear();
         v.resize(n+1);
         REP(i,n)
         {
                 cin>>m;
                 REP(j,m) v[i].pb(GI-1);
         }
         SET(mark,0);
         int f=0;
         cout<<"Case #"<<kase++<<": ";
         REP(i,n)
         {
           ans=0;
           dfs(i,i);
           if(ans){ cout<<"Yes\n";f=1;break;}
           else {SET(mark,0);}
         }
         if(!f) cout<<"No\n";
    }
    return 0;
}
