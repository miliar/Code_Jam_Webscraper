#include <cstdio>
#include <map>
#include <string>
#include <iostream>

#define INF 1000000

using namespace std;

int dp[102][1002];
int q[1002];

int main() {
	int N, Q, S;
	scanf("%d\n", &N);
	for(int caso = 1; caso <= N; ++caso) {
	  map<string, int> mapa;
	  mapa.clear();
	  memset(dp, 0, sizeof(dp));
	  memset(q, 0, sizeof(q));
	  string str;
	  scanf("%d\n", &S);
	  for(int i = 0; i < S; ++i) {
	    getline(cin, str);
	    mapa[str] = i;
	  }
	  scanf("%d\n", &Q);
	  for(int i = 0; i < Q; ++i) {
	    getline(cin, str);
	    q[i] = mapa[str];
	  }
	  for(int i = 0; i < S; ++i)
	    dp[i][0] = 0;
      dp[0][q[0]] = INF;
      for(int i = 1; i < Q; ++i) {
	    for(int j = 0; j < S; ++j) {
	      dp[i][j] = dp[i - 1][j];
	      if(q[i] == j) dp[i][j] = INF;
	      for(int k = 0; k < S; ++k) {
 		    if(k != j && dp[i - 1][k] + 1 < dp[i][j])
 		      dp[i][j] = dp[i - 1][k] + 1;
	      }
	    }
	  }
	  int melhor = dp[Q - 1][0];
	  for(int j = 1; j < S; ++j)
	    if(dp[Q - 1][j] < melhor)
	      melhor = dp[Q - 1][j];
      printf("Case #%d: %d\n", caso, melhor);
			
	}
	
	
	
	return 0;
}
