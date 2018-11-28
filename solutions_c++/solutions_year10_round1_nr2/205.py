#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
#define REP(i,N) for (int i = 0; i<(N); i++) 
#define ll long long

int D,I,M,N;
int cost(int a, int b){
  if (a==b) return 0;
  if (M==0) return (1<<30);
  else return max(0,(abs(a-b) -1)) / M * I;
}

int main(){
  int T;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    cin >> D >> I >> M >> N;
    int A[N];
    for (int i=0; i<N; i++) cin >> A[i];

    int dp[N][256];
    REP(i,N) REP(j,256) dp[i][j] = (1<<30);
    for (int i=0; i<256; i++) dp[0][i] = D;
    dp[0][A[0]] = 0;
    for (int i=0; i<256; i++) dp[0][i] = min( dp[0][i], dp[0][A[0]] + abs(A[0] - i));
    
    for (int i=0; i<N-1; i++){
      for (int j=0; j<256; j++){
	for (int k=0; k<256; k++){
	  dp[i+1][j] = min (dp[i+1][j], dp[i][k] + cost(j,k) + abs(j-A[i+1]));
	  if (j==k) dp[i+1][j] = min( dp[i+1][j], dp[i][k] + D);
	}
      }
    }
    /*
    for (int i=0; i<10; i++){
      for (int j=0; j<10; j++){
	cout << dp[i][j] << " ";
      }cout << endl;
    }cout << endl;
    */
    int ans = (1<<30);
    for (int i=0; i<256; i++){
      ans = min( dp[N-1][i], ans);
    }
    printf ("Case #%d: %d\n", iii+1, ans);
  }
  return 0;
}
