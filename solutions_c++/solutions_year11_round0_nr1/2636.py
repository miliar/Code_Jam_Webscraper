#include <iostream>
#include <stdlib.h>

using namespace std;

int
main() {
  int N;
  
  cin >> N;
  
  for(int i = 0; i < N; i++) {
    int T;
    // Blue - 0; Orange - 1
    int time[2] = {0, 0};
    int position[2] = {1, 1};
    int t = 0;
    
    cin >> T;
    
    for(int j = 0; j < T; j++) {
      char rc;
      int b;
      
      cin >> rc >> b;
      
      int r = (rc == 'B') ? 0 : 1;
      
      t += max(1, 1+abs(position[r]-b)-(t-time[r]));
      time[r] = t;
      position[r] = b;
    }
      
    cout << "Case #" << (i+1) << ": " << t << endl;
  }
  
  return 0;
}
