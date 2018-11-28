#include<stdio.h>
#include<vector>
#include<string>

using namespace std;

vector<string> V, Q;
int N, query;
const int inf = 100000000;

int dp[1030];

int memo(int u) {
    if( u == query ) return 0;
    if( dp[u] != -1 ) return dp[u];
    
    int i, j;
    int res = inf;
    for(i=0; i<V.size();i++) {
      if( V[i] != Q[u] ) {
        for(j=u+1;j<query;j++) {
          if( Q[j] == V[i] ) {
            int k = 1 + memo(j);
            res <?= k;
            break;
          }
        }
        if( j == query ) {
            return dp[u] = 0;
        }
      }
    }
    return dp[u] = res;
}



int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    char ss[100];
    gets(ss);
    sscanf(ss, "%d", &t);
    int cases = 1;
    int i;
    while( t-- ) {
         V.clear();
         gets(ss);
         sscanf(ss, "%d", &N);
         for(i=0;i<N;i++) {
            char str[200];
            gets(str);
            string s = str;
            V.push_back(str);                
         } 
         Q.clear();
         gets(ss);
         sscanf(ss, "%d", &query);
         for(i=0;i<query;i++) {
           gets(ss);
           string s = ss;
           Q.push_back(s);
         }
         
         int res = inf;
         for(i=0;i<query;i++)
           dp[i] = -1;
         
         res = memo(0);
         printf("Case #%d: %d\n", cases++, res);
         
    }
    return 0;
}
