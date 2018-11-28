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
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

int main(){
  int T;
  scanf("%d",&T);
  REP(CID,T){
    int N;
    scanf("%d",&N);
    int K = 0;
    int c;
    for(int i = 1; i<=N; i++){
      scanf("%d",&c);
      K+=(c != i);
    }
    printf("Case #%d: %d\n",CID+1,K>0?K:0);
  }
}
