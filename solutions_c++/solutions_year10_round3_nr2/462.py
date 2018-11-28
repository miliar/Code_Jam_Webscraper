#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void) {
  int n;
  cin >> n;
  for (int i=0; i<n; i++) {
    long long int p, li;
    int l, c;
    cin >> l >> p >> c;
    
    int cnt;
    li = l;
    for (cnt=0; li < p; li*= c) {
       cnt++;
    }  
    //cout << cnt << endl;
    
    int lg = 0;
    for (int ll = 1; ll < cnt; ll*=2) {
      lg++;
    }
//    cout << lg << endl;
    
    cout << "Case #" << (i+1) << ": " << lg << endl;
  }

  return 0;
}