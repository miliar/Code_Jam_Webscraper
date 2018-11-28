#include <iostream>
#include <fstream>
using namespace std;




int main() {
     int ndata;
     int N, K, aux;
     bool ok = 1;
     
     cin >> ndata;
     
     for (int i = 0; i < ndata; i++) {
	  cin >> N >> K;
	  aux = K+1;
	  ok = 1;
	  for (int j = 0; j < N; j++) {
	       if (aux%2 != 0) { 
		    ok = 0;
		    break;
	       }
	       aux /= 2;	       
	  }
	  if (ok)
	       cout << "Case #" << i+1 << ": ON" << endl;
	  else
	       cout << "Case #" << i+1 << ": OFF" << endl;
     }
}
