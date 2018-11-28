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
    int time = 0;
    int pos[2] = {1,1};
    int t[2] = {0,0};    
    int N;
    scanf("%d",&N);
    REP(i,N){
      char buf[3];
      int p;
      scanf("%1s %d",buf,&p);
      bool which = (buf[0] == 'O');
      time = max(time+1, t[which]+abs(pos[which] - p)+1);
      pos[which] = p;
      t[which] = time;
    }
    printf("Case #%d: %d\n",CID+1,time);
  }
}
