#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

int solve(int N, int S, int p, vector<int> T){
  int result = 0;
  
  for(int i = 0; i < N; i++){
    bool f = false;
    for(int j = 0; j <= 10; j++){
      for (int k = 0; k <= 10; ++k){
	for(int l = 0; l <= 10; ++l){
	  if(j+k+l != T[i]) continue;
	  int max_v=0, min_v=100;
	  max_v = max(j, max(k,l));
	  min_v = min(j, min(k,l));
	  if(max_v < p) continue;
	  if(max_v - min_v > 2) continue;
	  else if(max_v - min_v == 2){
	    f = true;
	  }
	  else if(max_v - min_v < 2){
	    result++;
	    f = false;
	    goto label;
	  }
	}
      }
    }
  label:;
    if(f && S > 0){
      result++;
      S--;
    }
  }

  return result;
}

int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; i++){
    int N, S, p;
    vector<int> T;
    cin >> N >> S >> p;
    for (int j = 0; j < N; ++j){
      int a;
      cin >> a;
      T.push_back(a);
    }
    cout << "Case #" << i+1 << ": " << solve(N, S, p, T) << endl;
  }
  return 0;
}
