#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <cassert>
using namespace std;

#define FOR(a,b,c) for(int a=(int)(b);a<(int)(c);a++)
#define ITER(a,b) for(__typeof((b).begin()) a = (b).begin(); a!=(b).end(); a++)
#define MEMSET(dest,val) memset(dest,val,sizeof(dest))
#define PAIR pair<int,int>
#define BEGEND(a) (a).begin(), (a).end()
#define SHIFT(v) (1LL<<(v))
#define SQ(a) ((a) * (a))
#define LSB(a,b) (b<=sizeof(a)?(b & (SHIFT(a)-1)):-1)

#define eps 1E-9
#define PI acos(-1.0)
#define INF 1000000000
#define LINF 90000000000000000000LL
#define LLMAX ((unsigned long long)(-1))

int N, M, V;
int dp[10010][2];
pair<int,int> nodes[10010];

int solve(int node, int val){
   //cout << "Solve: " << node << " " << val << endl;
   if(nodes[node].second == -1) return (val==nodes[node].first)?0:INF;
   if(dp[node][val]!=-1) return dp[node][val];
   int &ret = dp[node][val];

   int A = solve(node*2,val);
   int B = solve(node*2+1,val);

   int OR, AND;

   if(val == 1){
 	OR = min(A,B);
        AND = A + B; if(A==INF||B==INF) AND = INF;
   }
   else{
        OR = A + B; if(A==INF || B==INF) OR = INF;
        AND = min(A,B);
   }
   //cout << "HAVE: " << node << " " << A << " " << B << " " << OR << " " << AND << endl;


   if(nodes[node].second == 0) ret = (nodes[node].first)?AND:OR;
   else if(nodes[node].first==1) ret = min(OR+1,AND);
   else ret = min(OR,AND+1);

   //cout << "Solve: " << node << " " << val << " -> " << ret << endl;

   return ret;    
}
int main(){

  cin >> N;
  FOR(i,0,N){
    MEMSET(dp,-1);  
    cin >> M >> V;
    int k = 1;
    FOR(j,0,(M-1)/2) { cin >> nodes[k].first >> nodes[k].second; k++;}
    FOR(j,0,(M+1)/2) { cin >> nodes[k].first; nodes[k].second = -1; k++;}

//    FOR(k,1,M+1) cout << nodes[k].first << " " << nodes[k].second << endl;
    
    int res = solve(1,V);
    cout << "Case #" << (i+1) << ": ";
    if(res >= INF) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;

  }
  return 0;
}
