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
  int n,pd,pg;
  cin >> n >> pd >> pg;
  
  if((pd!=100 && pg==100) || (pd!=0 && pg==0)){
    cout << "Broken" << endl;
    return;
  }

  int min;
  for(int i=1; i<=100; i++){
    if((pd*i)%100 == 0){
      min = i;
      break;
    }
  }
  
  if(min > n){
    cout << "Broken" << endl;
    return;
  }

  cout << "Possible" << endl;
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
