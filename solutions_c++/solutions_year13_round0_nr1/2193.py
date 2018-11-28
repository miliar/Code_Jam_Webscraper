#include <iostream>
#include <string>
using namespace std;

const string ans[4] = {"X won","O won","Draw","Game has not completed"};

int do_case(){
  string A[4];
  for(int i=0;i<4;i++)
    cin >> A[i];
  
  int ctr[128];
  // Row win?
  for(int i=0;i<4;i++){
    ctr['X'] = ctr['O'] = ctr['T'] = 0;
    for(int j=0;j<4;j++) ctr[A[i][j]]++;
    if(ctr['X'] + ctr['T'] == 4) return 0;
    if(ctr['O'] + ctr['T'] == 4) return 1;
  }
  
  // Column win?
  for(int j=0;j<4;j++){
    ctr['X'] = ctr['O'] = ctr['T'] = 0;
    for(int i=0;i<4;i++) ctr[A[i][j]]++;
    if(ctr['X'] + ctr['T'] == 4) return 0;
    if(ctr['O'] + ctr['T'] == 4) return 1;
  }
  
  // Diagonal (forward) win?
  ctr['X'] = ctr['O'] = ctr['T'] = 0;
  for(int i=0;i<4;i++) ctr[A[i][i]]++;
  if(ctr['X'] + ctr['T'] == 4) return 0;
  if(ctr['O'] + ctr['T'] == 4) return 1;
  
  // Diagonal (backward) win?
  ctr['X'] = ctr['O'] = ctr['T'] = 0;
  for(int i=0;i<4;i++) ctr[A[i][3-i]]++;
  if(ctr['X'] + ctr['T'] == 4) return 0;
  if(ctr['O'] + ctr['T'] == 4) return 1;

  // Game complete?
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      if(A[i][j] == '.')
        return 3;
  
  // Must be a draw!
  return 2;
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--)
    cout << "Case #" << C++ << ": " << ans[do_case()] << endl;
  return 0;
}
