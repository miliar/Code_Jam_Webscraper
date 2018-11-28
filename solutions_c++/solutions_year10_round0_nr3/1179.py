#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
using namespace std;

int main(){

  int T;
  cin >> T;
  for(int t = 1; t <= T; t++){
    int R, K, N;    
    queue<int> q;
    cin >> R >> K >> N;
    for(int i = 0; i < N; i++){
      int g;
      cin >> g;
      q.push(g);
    }
    int ans = 0;
    while(R--){
      int lim = 0;
      vector<int> pas;
      while(!q.empty() && q.front() + lim <= K){
	lim += q.front();
	pas.push_back(q.front());
	q.pop();	
      }
      ans += lim;
      for(int i = 0; i < pas.size(); i++){
	q.push(pas[i]);
      }
      pas.clear();
    }
    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}
