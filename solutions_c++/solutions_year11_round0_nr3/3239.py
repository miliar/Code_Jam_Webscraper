#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
     int n;
     cin >> n;
     vector<int> v(n);
     for (int j=0; j<v.size(); j++) cin >> v[j];
     int maxim = -1;
     for (int j=1; j<(1<<n)-1; j++) {
      int suma_a,suma_b;
      suma_a = suma_b = 0;
      int a,b;
      a = b = 0;
      for (int k=0; k<n; k++) {
          if (j>>k & 1) {
             a^=v[k];
             suma_a+=v[k];
          }
          else {
               b^=v[k];
               suma_b+=v[k];
          }    
      }
      if (a == b and max(suma_a,suma_b) > maxim) maxim = max(suma_a,suma_b);      
     }
     cout << "Case #" << i+1 << ": ";
     if (maxim == -1) cout << "NO" << endl;
     else cout << maxim << endl;   
    }
}
