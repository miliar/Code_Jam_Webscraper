#include <iostream>

using namespace std;

int
main() {
  int T;
  
  cin >> T;
  
  for(int i = 1; i <= T; i++) {
    int R, C;
    bool possible = true;
    
    cin >> R >> C;
    
    char* m = new char[(R+1)*(C+1)];
    for(int r = 0; r < R; r++) {
      for(int c = 0; c < C; c++) {
        cin >> (m[r*C+c]);
      }
    }
    
    for(int r = 0; (r < R) && possible; r++) {
      for(int c = 0; (c < C) && possible; c++) {
        if(m[r*C+c] == '#') {
         m[r*C+c] = '/';
          if(((c+1) < C) && (m[r*C + c+1] == '#')) {
            m[r*C + c+1] = '\\';
          } else {
            possible = false;
          }
          
          if(((r+1) < R) && (m[(r+1)*C + c] == '#')) {
            m[(r+1)*C + c] = '\\';
          } else {
            possible = false;
          }
          if(((r+1) < R) && ((c+1) < C) && (m[(r+1)*C + c+1] == '#')) {
            m[(r+1)*C + c+1] = '/';
          } else {
            possible = false;
          }
        }
      }
    }
    
    cout << "Case #" << i << ":" << endl;
    if(possible) {
      for(int r = 0; r < R; r++) {
        for(int c = 0; c < C; c++) {
          cout << m[r*C + c];
        }
        cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
    
    delete[] m;
  }
  
  return 0;
}
