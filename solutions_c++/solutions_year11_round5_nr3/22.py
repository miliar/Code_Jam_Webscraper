#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD; 
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define MAP(i,j) (C*(i)+(j))

char board[1000][1000];

const int K = 13000;
list<int> adj[2*K];

int match[2*K];

void dfs(int v){
  FOREACH(it,adj[v])
    if(match[*it] == -1){
      match[v] = *it;
      match[*it] = v;
      FOREACH(it2,adj[*it])
        if(match[*it2] == -1)dfs(*it2);
    } 
      

}

void scase(int CID){
  int R,C;
  scanf("%d%d",&R,&C);
  int neigh[R*C][2];   
  REP(i,R)scanf("%s",board[i]);
  REP(i,R)REP(j,C){
    if(board[i][j] == '-'){
      neigh[MAP(i,j)][0] = MAP(i,(j+1)%C);
      neigh[MAP(i,j)][1] = MAP(i,(j+C-1)%C);      
    }else if(board[i][j] == '|'){
      neigh[MAP(i,j)][0] = MAP((i+1)%R,j);
      neigh[MAP(i,j)][1] = MAP((i+R-1)%R,j);      
    }else if(board[i][j] == '/'){
      neigh[MAP(i,j)][0] = MAP((i+R-1)%R,(j+1)%C);
      neigh[MAP(i,j)][1] = MAP((i+1)%R,(j+C-1)%C);      
    }else if(board[i][j] == '\\'){
      neigh[MAP(i,j)][0] = MAP((i+R-1)%R,(j+C-1)%C);
      neigh[MAP(i,j)][1] = MAP((i+1)%R,(j+1)%C);
    }      
  }
  int N = R*C;
  
  REP(i,2*K)adj[i].clear();
  
  REP(i,N)REP(j,2){
    adj[i].pb(K+neigh[i][j]);
    adj[K+neigh[i][j]].pb(i);    
  }
  
  REP(i,2*K)
    match[i] = -1;
  
  queue<int> Q;
  bool fail = false;
  int indeg[2*K];
  REP(i,2*K) indeg[i] = adj[i].size();
  REP(i,N){
    if(indeg[i] == 0)fail = true;
    else if(indeg[i] == 1)Q.push(i);
    if(indeg[K+i] == 0)fail = true;
    else if(indeg[K+i] == 1)Q.push(K+i);    
  }
  
  while(!Q.empty()){
    int v = Q.front();
    Q.pop();
    if(!indeg[v])fail = true;
    FOREACH(it,adj[v])
      if(match[*it] == -1){
        match[*it] = v - K;
        match[v] = *it;
        FOREACH(it2,adj[*it]){
          indeg[*it2]--;
          if(indeg[*it2] == 1)Q.push(*it2);
        }
      }    
  }
  
  int result = fail?0:1;
  
  if(!fail){
    REP(i,N)
      if(match[i] == -1){
        dfs(i);
        result = (2*result)%1000003;
      }
  }
  
  printf("Case #%d: %d\n",CID,result%1000003);
}

int main(){
  int T;
  scanf("%d",&T);
  FOR(CID,1,T+1)scase(CID);
}
