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

void scase(int CID){
  int N;
  scanf("%d",&N);
  
  if(!N){
    printf("Case #%d: 0\n",CID);
    return;
  }
  
  int T[10001];
  REP(i,10000)T[i] = 0;
  REP(i,N){
    int a;
    scanf("%d",&a);
    T[--a]++;
  }
  vector<int> mins;
  REP(i,10000){
    int k = (i==0)?T[i]:T[i] - T[i-1];
    REP(s,k)mins.pb(i); 
  }
  REP(i,mins.size())
    T[mins[i]]--;

  int result = 1;
  while(true){
    REP(i,mins.size())
      if(T[mins[i]+result] == 0){
        goto output;
      }else T[mins[i]+result]--;
    result++;
  }
  output:
    printf("Case #%d: %d\n",CID, result);
}

int main(){
  int T;
  scanf("%d",&T);
  FOR(CID,1,T+1)scase(CID);
}
