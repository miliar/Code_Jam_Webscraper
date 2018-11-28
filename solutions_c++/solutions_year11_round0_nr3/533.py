
#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

#define REP(i, n) for(int i = 0; i < (int)(n); ++i)

using namespace std;

int table[1234];

int main(void) {
  int nCases;
  cin >> nCases;
  REP(iCase, nCases){
    int n;
    cin >> n;
    int xors = 0;
    int sum = 0;
    int mini = 12345678;
    REP(i, n){
      cin >> table[i];
      xors ^= table[i];
      sum += table[i];
      mini = min(mini, table[i]);
    }
    
    if(xors == 0){
      cout << "Case #" << (iCase+1) << ": " << (sum - mini) << endl;
    }else{
      cout << "Case #" << (iCase+1) << ": NO" << endl;
    }
  }
  return 0;
}
