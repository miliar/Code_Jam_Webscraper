#include <iostream>

using namespace std;

int main() {
      int T=0;
      int N=0;
      long long K=0;
      long long  p = 1;

      cin >> T;

      for(int i=0; i < T; i++) {
	    p = 1;

	    cin >> N;
	    cin >> K;

	    p = (p<< N);
	
	    if(((K+1)%p) == 0)
		  cout << "Case #" << (i+1) << ": " << "ON" << endl;
	    else
		  cout << "Case #" << (i+1) << ": " << "OFF" << endl;
      }
}
