#include <iostream>
#include <string>
#include <cassert>
using namespace std;

// S = 0    0+0+0=0
// S = 

// S = 3*s    s+s+s->s    (s-1)+s+(s+1)->(s+1)*
// S = 3*s+1  s+s+(s+1)->(s+1)   (s-1)+(s+1)+(s+1)->(s+1)*
// S = 3*s+2  s+(s+1)+(s+1)->(s+1)  s+s+(s+2)->(s+2)* 
   
int  t[100];
int T,N,S,p;

int solve() {
  int r = 0;
  for (int i=0;i<N;++i) {
    int s = t[i]/3;
    int k = t[i] - 3*s;
    if (k>0) s++;
    
    if (s>=p) {
      r++;
    } else if (s<p-1) {
      // nop!
    } else {
      // s == p-1
      if (k==0 || k==2) {
	if (S>0 && t[i]>0 && t[i]<29) {
	  r++;
	  S--;
	}
      }
    }
  }
  return r;
}

int main() {
  cin >> T;
  for (int X=1; X<= T; X++) {
      cin >> N >> S >> p;
      for (int n=0; n<N ; ++n) {
      	  cin >> t[n];	
      }
      cout << "Case #" << X << ": " << solve() << endl;
  }
  return 0;
}
