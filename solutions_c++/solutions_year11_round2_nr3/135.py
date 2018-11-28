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

#define TEST_NAME "C-small-attempt0"

int n;
VVI adj;
VVI pos;
VVI used;
VVI rooms;
VI color;
int ansc;

void trace_room(int cur,int prv,int targ) {
     int nxt;
//      cerr<<"trace_room "<<cur<<" "<<prv<<" "<<targ<<endl;
     while(cur!=targ) {
          rooms.back().pb(cur);
          nxt=pos[cur][prv]-1;
          if(nxt<0)nxt+=SZ(adj[cur]);
          nxt=adj[cur][nxt];
//           cerr<<"cur="<<cur<<" "<<"prv="<<prv<<" nxt="<<nxt<<endl;
          used[cur][nxt]=true;
          prv=cur;
          cur=nxt;
     }
}

bool find_perm(int k) {
     if(k>=n) {
          REP(r,SZ(rooms)) {
               VI us(ansc,false);
               REP(k,SZ(rooms[r]))
                    us[color[rooms[r][k]]]=true;
               REP(k,ansc)
                    if(!us[k])return false;
          }
          return true;
     }
     else {
          for(color[k]=0;color[k]<ansc;++color[k])
               if(find_perm(k+1))return true;
          return false;
     }
}

int main() {
     freopen(TEST_NAME ".in","r",stdin);
     freopen(TEST_NAME ".out","w",stdout);
     int testcount,test;
	
     for(cin>>testcount,test=1;test<=testcount;++test) {
          int m;
          scanf("%d%d",&n,&m);
          VI u(m),v(m);
          REP(i,m){scanf("%d",&u[i]);--u[i];}
          REP(i,m){scanf("%d",&v[i]);--v[i];}

          adj=VVI(n);
          REP(i,m) {
               adj[u[i]].pb(v[i]);
               adj[v[i]].pb(u[i]);
          }
          REP(i,n) {
               adj[i].pb((i+1)%n);
               adj[(i+1)%n].pb(i);
          }
          REP(i,n)SORT(adj[i]);

          pos=VVI(n,VI(n,-1));
          used=VVI(n,VI(n));
          REP(i,n) {
               REP(j,SZ(adj[i])) {               
                    pos[i][adj[i][j]]=j;
               }
          }
          rooms.clear();
          REP(i,n) {
               REP(j,SZ(adj[i]))
                    if(!used[i][adj[i][j]]) {
                         int k=adj[i][j];
//                          cerr<<"room: "<<i<<" ";
                         rooms.push_back(VI());
                         used[i][k]=true;
                         rooms.back().pb(i);
                         trace_room(k,i,i);
                         if(rooms.back().size()==n)rooms.pop_back();
//                          else {
//                               cerr<<"room={";
//                               REP(i,SZ(rooms.back()))cerr<<rooms.back()[i]<<" ";
//                               cerr<<"}"<<endl;
//                          }
                    }
          }

          ansc=n+1;
          int begr=-1;
          REP(k,SZ(rooms)) {
               if(ansc>SZ(rooms[k])) {
                    ansc=SZ(rooms[k]);
                    begr=k;
               }
          }

          color=VI(n);
          find_perm(0);
          
          printf("Case #%d: %d\n",test,ansc);
          REP(i,n) {
               if(i)printf(" ");
               printf("%d",color[i]+1);
          }
          printf("\n");
               
}
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
