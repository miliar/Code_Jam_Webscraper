#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
  int T,N,K;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    cin >> N >> K;
    bool ok = true;
    for (int i=0; i<N; i++){
      if ((K&1) == 0){
        ok = false;
        break;
      }
      K>>=1;
    }
    
    if (ok) printf ("Case #%d: ON\n",iii+1);
    else printf ("Case #%d: OFF\n",iii+1);
  }
}
