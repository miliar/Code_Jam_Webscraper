#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>


using namespace std;


void alg() {
  char T[4][4];
  int v[4] = {0}, h[4] = {0}, d[2] = {0};
  bool finished = true;
  int t_pos[2];
  
  
  for (int i = 0; i < 16; i++) {
    cin >> T[i/4][i%4];
    
    switch (T[i/4][i%4]) {
    case 'X':
      h[i/4]++;
      v[i%4]++;
      d[0] += ((i/4 + i%4) == 3);
      d[1] += (i/4 == i%4);
      break;
    case 'O':
      h[i/4]--;
      v[i%4]--;
      d[0] -= ((i/4 + i%4) == 3);
      d[1] -= (i/4 == i%4);
      break;
    case 'T':
      t_pos[0] = i/4;
      t_pos[1] = i%4;
      break;
    case '.':
      finished = false;
      break;
    default:
      cerr << "ERROR in switch, case not listed." << endl;
    }
  }    
  

  for (int i = 0; i < 4; i++) {
    if(v[i] == 4 || (v[i] == 3 && t_pos[1] == i) || h[i] == 4 || (h[i] == 3 && t_pos[0] == i)) {
      cout << "X won" << endl;
      return;
    }
    
    if(v[i] == -4 || (v[i] == -3 && t_pos[1] == i) || h[i] == -4 || (h[i] == -3 && t_pos[0] == i)) {
      cout << "O won" << endl;
      return;
    }
  }
  
  if(d[0] == 4 || (d[0] == 3 && t_pos[0] + t_pos[1] == 3) || d[1] == 4 || (d[1] == 3 && t_pos[0] == t_pos[1])) {
    cout << "X won" << endl;
    return;
  }
  
  if(d[0] == -4 || (d[0] == -3 && t_pos[0] + t_pos[1] == 3) || d[1] == -4 || (d[1] == -3 && t_pos[0] == t_pos[1])) {
    cout << "O won" << endl;
    return;
  }
  
  if (finished) {
    cout << "Draw" << endl;
    return;
  }
  
  cout << "Game has not completed" << endl;
  
}

int main() {
    int n_cases;
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
      cout << "Case #" << test_case << ": ";
      alg();
    }

    return EXIT_SUCCESS;
}
