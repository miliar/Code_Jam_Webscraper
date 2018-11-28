#include <iostream>
#include <vector>
using namespace std;
long long dp[1001][1001];
int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    
    long long n,m,x,y,z;
    cin >> n >> m >> x >> y >> z;
    vector<long long> data(m);
    for(int i=0;i<m;i++){
      cin >> data[i];
    }
    vector<long long> array(n);
    for(int i=0;i<n;i++){
      array[i] = data[i%m];
      data[i%m] = (x*data[i%m]+y*(i+1))%z;
    }
    for(int i=0;i<=n;i++){
      for(int j=0;j<=n;j++){
	dp[i][j] =0;
      }
    }
    for(int i=0;i<n;i++){
      for(int j=0;j<i;j++){
	dp[i+1][j] += dp[i][j];
	dp[i+1][j] %= 1000000007;
	if(array[j] < array[i]){
	  dp[i+1][i] += dp[i][j];
	  dp[i+1][i] %= 1000000007;
	}
      }
      dp[i+1][i] += 1;
      dp[i+1][i] %= 1000000007;
    }
    long long ret = 0;
    for(int i=0;i<n;i++){
      ret += dp[n][i];
      ret %= 1000000007;
    }
    cout << ret << endl;
  }
  return 0;
}
