#include <iostream>
using namespace std;

int main(){
  int t,o;
  cin >> t;
  o = t;
  int x[55],v[55];
  
  while (t--){
    cout << "Case #"<<o-t<<": ";
    int n,t,k,b;
    cin >> n >> k >> b >> t;
    for (int i = 0; i < n; ++i)
      cin >> x[i];
    for (int i = 0; i < n; ++i){
      cin >> v[i];
      x[i]+=v[i]*t;
    }
    int passed = 0,failed = 0,ans = 0;
    for (int i = n-1; i >=0;--i){
      if (x[i]>=b){
	++passed;
	ans+=failed;
      }      
      else{
	++failed;
      }      
      if (passed==k){
	cout << ans <<endl;
	break;
      }
    }
    if (passed!=k)
      cout << "IMPOSSIBLE\n";
    
  }
}
