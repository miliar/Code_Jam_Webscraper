#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void solve(void){
  int N;
  cin >> N; 
  int xB=1,xO=1;
  int freeCountB=0,freeCountO=0;
  int res=0;
 
  for(int i=0; i<N; i++){
    char robot;
    int button;
    int required1;
    int required2;
    cin >> robot >> button;
    if(robot=='B'){
      required1 = abs(button-xB) + 1;
      required2 = max(1, required1 - freeCountB);
      freeCountB = 0;
      freeCountO += required2;
      res += required2;
      xB = button;
    }else{
      required1 = abs(button-xO) + 1;
      required2 = max(1, required1 - freeCountO);
      freeCountO = 0;
      freeCountB += required2;
      res += required2;
      xO = button;
    }
  }
  
  cout << res << endl;
}

int main(void){
  int testCaseCount;
  cin >> testCaseCount;
  for(int i=1; i<=testCaseCount; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
