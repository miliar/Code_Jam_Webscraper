#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

#define TEST_NAME "C-large"

class MaxMatching {
     int n1,n2,matchsz;
     struct edge {
	  int w,cap,dup;
	  edge(int W=0,int C=0,int D=-1):w(W),cap(C),dup(D) {}
     };
     vector<vector<edge> > adj;
     vector<int> prv;
     unsigned sedge;
     inline void IntAddEdge(int v1,int v2) {
	  adj[v1].push_back(edge(v2,1,SZ(adj[v2])));
	  adj[v2].push_back(edge(v1,0,SZ(adj[v1])-1));
     }
     bool start_path() {
	  prv[n1+n2]=1000000000;
	  for(;sedge<SZ(adj[n1+n2]);sedge++)
	       for(int i=0,sz=SZ(adj[n1+n2]);i<sz;i++)
		    if(adj[n1+n2][sedge].cap&&find_path(adj[n1+n2][sedge].w,adj[n1+n2][sedge].dup))return true;
	  return false;
     }
     bool find_path(int v,int e) {
	  if(v==n1+n2+1) {
	       matchsz++;
	       prv[v]=e;
	       for(int i=n1+n2+1;i!=n1+n2;i=adj[i][prv[i]].w) {
		    adj[i][prv[i]].cap++;
		    adj[adj[i][prv[i]].w][adj[i][prv[i]].dup].cap--;
	       }
	       start_path();
	       return true;
	  }
	  else if(prv[v]>=0)return false;
	  else {
	       prv[v]=e;
	       for(int i=0,sz=SZ(adj[v]);i<sz;i++)
		    if(adj[v][i].cap&&find_path(adj[v][i].w,adj[v][i].dup))return true;
	       return false;
	  }
     }
public:
     MaxMatching(int N1,int N2):n1(N1),n2(N2),matchsz(0),adj(N1+N2+2) {
	  int i;
	  for(i=0;i<n1;i++)IntAddEdge(n1+n2,i);
	  for(i=0;i<n2;i++)IntAddEdge(i+n1,n1+n2+1);
     }
     inline void AddEdge(int v1,int v2) {IntAddEdge(v1,n1+v2);}
     int Match() {
	  do {
	       prv=vector<int>(n1+n2+2,-1);
	       sedge=0;
	  }while(start_path());
	  prv.clear();
	  return matchsz;
     }
};

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int n,test;
	
     for(cin>>n,test=1;test<=n;++test) {
          int n,k;
          cin>>n>>k;          
          VVI p(n,VI(k));
          VVI lower(n,VI(n,true));
          REP(i,n)REP(j,k)cin>>p[i][j];
          MaxMatching matching(n,n);
          REP(i,n)REP(j,n) {
               REP(x,k)if(p[i][x]>=p[j][x]) {
                    lower[i][j]=false;
                    break;
               }
               if(lower[i][j])matching.AddEdge(i,j);
          }
          int ans=n-matching.Match();
          printf("Case #%d: %d\n",test,ans);
          
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
