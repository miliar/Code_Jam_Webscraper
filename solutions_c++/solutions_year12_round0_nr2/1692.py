#include <iostream>

using namespace std;


#define REP(n,i) for (int i=0;i<(n);i++)

int main(void) {
  int T;
  int N;
  int S;
  int p;
  int t[100];

  int r; 
  int max;
  int surprise;
  cin >> T;
  REP(T,i) {
    int num=0;
    cin >> N >> S >> p;
    REP(N,j) cin >> t[j];
    
    REP(N,j) {
      r = t[j] % 3;
      if (r == 2) {
        max = t[j]/3 + 1;
        surprise = max+1;
      }
      if (r == 1) {
        max = t[j]/3+1;
        surprise = max;
      }
      if (r == 0) {
        max = t[j]/3;
        if (t[j] > 0) 
          surprise = max+1;        
        else
          surprise = max;
      }  
      
//      cout << "MAX: " << max << " Suprise: " << surprise << " S: " << S << " p: " << p << endl;
      if (max >= p) num++;
      else {
        if (surprise >= p && S>0) {
          num++;
          S--;
        }
      }                  
    }
    cout << "Case #" << i+1 << ": " << num << endl;
  
  }
  
}