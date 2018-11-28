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
char S[300];
void scase(int CID){
  scanf("%s",S);
  int N = strlen(S);
  reverse(S,S+N);
  LL liczba = 0;
  vector<int> unknown;
  REP(i,N){
    if(S[i] == '?')
      unknown.pb(i);
    else if(S[i] == '1')
      liczba += (1LL<<i);
  }
  
  REP(mask,(1<<unknown.size())){
    LL temp = liczba;
    REP(i,unknown.size()){
      if(mask&(1LL<<i))
        temp += (1LL<<(unknown[i]));
    }
    LL s = sqrt((long double)temp);
    if(s*s == temp || (s+1)*(s+1) == temp){
      printf("Case #%d: ",CID); 
      int k = 63;
      while(!((1LL<<k)&temp))--k;
      while(k>=0){
        printf("%lld",((1LL<<k)&temp)>>k);
        --k;
      }
      printf("\n");
      break;
    }   
  }
  
  
}

int main(){
  int T;
  scanf("%d",&T);
  FOR(CID,1,T+1)scase(CID);
}
