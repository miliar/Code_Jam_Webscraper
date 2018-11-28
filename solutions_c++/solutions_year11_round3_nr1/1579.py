#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

bool doTheMath(int p_rows, int p_cols, char array[50][50]) {
  for(int i = 0; i < p_rows; ++i)
    for(int j = 0; j < p_cols; ++j) {
      if(array[i][j] == '#') {
        if(i+1 >= p_rows || j+1 >= p_cols)
          return false;
        
        if(array[i+1][j] != '#' || array[i][j+1] != '#' || array[i+1][j+1] != '#')
          return false;
        
        array[i][j] = '/', array[i+1][j] = '\\';
        array[i][j+1] = '\\', array[i+1][j+1] = '/';
      }
    }
  
  return true;
}

int main() {
  int l_test_cases, rows, cols;
  char array[50][50];
  
  cin >> l_test_cases;
  
  for(int i = 0; i < l_test_cases; ++i) {    
    cin >> rows >> cols;
    
    for(int j = 0; j < rows; ++j)
      for(int k = 0; k < cols; ++k)
        cin >> array[j][k];
    
    cout << "Case #" << (i+1) << ": " << endl;
    
    if(doTheMath(rows, cols, array)) {
      for(int j = 0; j < rows; ++j) {
        for(int k = 0; k < cols; ++k)
          cout << array[j][k];
        
        cout << endl;
      }
    }
    else
      cout << "Impossible" << endl;
  }
  
  return 0;
}
