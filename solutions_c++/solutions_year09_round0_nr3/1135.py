#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<iomanip>

using namespace std;

void dump(const vector<vector<int> >& v){
  for(int i=0;i<v.size();++i){
    for(int j=0;j<v[i].size();++j)
      cout << v[i][j] << " ";
    cout << endl;
  }
  cout << endl;
}
int dp(const string L){
  string S = "welcome to code jam";
  const int N = L.size();
  const int M = S.size();
  vector<vector<int> > DP(N, vector<int>(M));

  for(int i=0;i<N;++i){
    if(L[i] == S[0])
      DP[i][0] = 1;
    for(int j=1;j<M;++j){
      if(L[i] == S[j]){
	for(int k=i-1;k>=0;--k){
	  if(L[k] == S[j-1]){
	    DP[i][j] = (DP[i][j] + DP[k][j-1])%10000;
	  }
	}
      }
    }
  }
  //  dump(DP);
  int ret = 0;
  for(int i=0;i<N;++i)
    ret = (ret + DP[i][M-1])%10000;

  return ret;
}
int main(){  
  int N; cin >> N;
  string line;
  getline(cin, line);
  for(int t=0;t<N;++t){
    getline(cin, line);
    int ret = dp(line);

    cout << "Case #" << (t+1) << ": " << setw(4) << setfill('0') << ret << endl;
  }
  
}
