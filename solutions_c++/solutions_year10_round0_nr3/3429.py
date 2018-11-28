#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

ll memo[1001][1001];

ll simulate(ll R, ll k, int N, vector<ll> groups){
  for(int i=0; i<N; i++){
    for(int j=0, jj=i; j<N; j++){
      if(j==0){
	memo[i][j] = groups[i];
      }else{
	memo[i][j] = groups[jj] + memo[i][j-1];
      }
      if(++jj>=N) jj=0;
    }
  }
  /*
  for(int i=0; i<N; i++){
    for(int j=0; j<N; j++){
      cout << memo[i][j];
    }
    cout << endl;
  }
  */
  int now = 0;
  ll ret = 0;
  for(ll i=0; i<R; i++){
    if(N==1) if(k>=groups[0]) ret+=groups[0];
    for(int j=1; j<N; j++){
      if(k<memo[now][j]){
	ret+=memo[now][j-1];
	now=(now+j)%N;
	break;
      }
      if(j==N-1 && k>=memo[now][j]){
	ret+=memo[now][j];
      }
    }
    //cout << i << " " << ret << endl;
  } 
  return ret;
}

int main(){
  int cases;
  cin >> cases;
  for(int c=1; c<=cases; c++){
    ll R, k, tmp;
    int N;
    cin >> R >> k >> N;
    vector<ll> groups;
    for(int i=0; i<N; i++){
      cin >> tmp;
      groups.push_back(tmp);
    }
    //cout << "->" << R << " " << k << " " << N << endl;
    //cout << "->"; for(int i=0; i<N; i++) cout << groups[i] << " "; cout << endl;
    cout << "Case #" << c << ": " << simulate(R, k, N, groups) << endl;
  }
  return 0;
}
