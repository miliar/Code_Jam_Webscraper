#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

typedef long long int lli;

int main(){
  int tn;
  cin >> tn;

  for(int tc = 1; tc<=tn; tc++){
    int n,l,h;
    cin >> n >> l >> h;
    vector<int> oh(n,0);
    for(int i=0; i<n; i++){
      cin >> oh[i];
    }
    int ans = 0;
    for(int i=l; i<=h; i++){
      for(int j=0; j<n; j++){
	if(oh[j] % i != 0 && i % oh[j] != 0){
	  break;
	}
	if(j == n-1){
	  ans = i;
	}
      }
      if(ans != 0)break;
    }
    cout << "Case #" << tc << ": ";
    if(ans == 0)cout << "NO" << endl;
    else cout << ans << endl;
  }

  return 0;
}
