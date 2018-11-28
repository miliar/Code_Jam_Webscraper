#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int bs(int i, int asum, int bsum, int rasum, int rbsum, vector <int> c, int n){
  static int total = 0;
  if(i == 0) total = 0;

  if(i == n){
    //  cout << asum << " " << bsum << endl;
  if(asum == bsum && !(rasum == 0 || rbsum == 0)) total = max(total, max(rasum, rbsum));
    return total;
  }
  if(bs(i+1, asum ^ c[i], bsum, rasum + c[i], rbsum, c, n)){
  }
  if(bs(i+1, asum, bsum ^ c[i], rasum, rbsum + c[i], c, n)){
  }
  return total;
}

int main(){
  int t;
  cin >> t;

  for(int i = 1; i <= t; i++){
    int n;
    cin >> n;

    vector <int> c(n);
    for(int j = 0; j < n; j++)
      cin >> c[j];

    int asum = 0, bsum = 0, rasum = 0, rbsum = 0;
    int s = bs(0, asum, bsum, rasum, rbsum, c, n);
    cout << "Case #" << i << ": "; 
    if(s == 0) cout << "NO\n";
    else cout << s << "\n";
  }

  return 0;
}
