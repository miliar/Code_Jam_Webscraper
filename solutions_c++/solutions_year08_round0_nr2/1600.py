#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define pi acos(-1.)
#define eps 1e-7
#define inf 1000000000
#define maxn 512
#define maxp 1100000

//ifstream fin("data.in");
//#define cin fin

/*
  idea: convert into minimum flow problem with lower/upper capacity
  each trip correspond to vertex with upper = lower capacity = 1
  each trip has transition to another trip if it is possible to use same train
  upper=1, lower=0
  there is super source and super sink
  
  we can solve it using mincost flow easily
 */
vector<int> flow[maxn],adj[maxn],cap[maxn],rev[maxn],cost[maxn];
void init() {
  for(int i=0;i<maxn;i++)
    flow[i].clear(),adj[i].clear(),cap[i].clear(),rev[i].clear(),
      cost[i].clear();
}
void add(int a,int b,int c,int v) {
  int an=adj[a].size(),bn=adj[b].size();
  adj[a].push_back(b), flow[a].push_back(0),
    rev[a].push_back(bn), cap[a].push_back(c), cost[a].push_back(v);
  adj[b].push_back(a), flow[b].push_back(0),
    rev[b].push_back(an), cap[b].push_back(0), cost[b].push_back(-v);
}
int min_cost_max_flow(int n,int s,int t,int& netcost){
  int pre[maxn],pot[maxn],d[maxn],w,x,v,y,i,j;
  priority_queue<pair<int,int> > que;
  if(s==t) return inf;
  memset(pot,0,sizeof(pot));
  for(netcost=0;;) {
    for(i=0;i<n;i++) d[i]=inf, pre[i]=-1;
    d[s]=0,que.push(make_pair(0,s));
    while(que.size()) {
      w=-que.top().first, x=que.top().second, que.pop();
      if(d[x]==w)
        for(i=0;i<adj[x].size();i++)
          if(cap[x][i]-flow[x][i]&&
             d[x]+cost[x][i]+pot[x]-pot[v=adj[x][i]]<d[adj[x][i]])
            d[v]=d[x]+cost[x][i]+pot[x]-pot[v], pre[v]=rev[x][i],
              que.push(make_pair(-d[v],v));
    }
    if(d[t]==inf) break;
    for(i=t,y=inf;i!=s;i=v)
      v=adj[i][pre[i]],j=rev[i][pre[i]],y<?=cap[v][j]-flow[v][j];
    for(i=0;i<n;i++) pot[i]+=d[i];
    for(netcost+=pot[i=t]*y;i!=s;i=v)
      flow[v=adj[i][pre[i]]][rev[i][pre[i]]]+=y,flow[i][pre[i]]-=y;
  }
  for(j=i=0;i<adj[s].size();j+=flow[s][i++]);
  return j;
}

int convert(string s) {
  int a = atoi(s.substr(0,2).c_str());
  int b = atoi(s.substr(3).c_str());
  return a*60+b;
}

int turn,na,nb,times[maxn][2];

int main() {
  int T;
  cin>>T;
  for(int C=1; C<=T; C++) {
    cin>>turn>>na>>nb;
    string s,t;
    REP(i,na) {
      cin>>s>>t;
      times[i][0]=convert(s);
      times[i][1]=convert(t);
    }
    REP(i,nb) {
      cin>>s>>t;
      times[i+na][0]=convert(s);
      times[i+na][1]=convert(t);
    }
    init();
    int ss = 2*(na+nb), tt = ss+1, source = ss+2, sink = ss+3;
    REP(i,na) REP(j,nb) {
      // using same train is possible?
      if(times[i][1]+turn<=times[j+na][0]) add(2*i+1,2*(j+na),1,0);
      if(times[j+na][1]+turn<=times[i][0]) add(2*(j+na)+1,2*i,1,0);
    }
    REP(i,na+nb) {
      // connect them
      add(ss,2*i,1,0);
      add(2*i+1,tt,1,0);
    }
    add(tt,ss,na+nb,1);
    REP(i,na+nb) {
      // supply and demand of each node
      add(source,2*i+1,1,0);
      add(2*i,sink,1,0);
    }
    int totcost,val,sola=0,solb=0;
    val = min_cost_max_flow(sink+1,source,sink,totcost);
    //cout << val<<' '<<totcost<<endl;
    REP(i,adj[ss].size()) {
      int j = adj[ss][i];
      if(j==tt) continue;
      int k = j/2;
      if(!flow[ss][i]) continue;
      if(k<na) sola++;
      else solb++;
    }
    cout << "Case #"<<C<<": "<<sola<<' '<<solb<<endl;
  }
}
