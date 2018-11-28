#include <iostream>

using namespace std;

int main(int argc,char*argv[]){
  int t,n,k;
  cin >> t;
  for(int i=1;i<=t;++i){
    cin >> n >> k;
    int mod = 1<< n;
    k = k %(1<<n);
    cout << "Case #" << i << ": ";
    if(k == (mod -1)) cout << "ON" << endl;
    else cout << "OFF" << endl;
  }
  return 0;
}
    
			
    
