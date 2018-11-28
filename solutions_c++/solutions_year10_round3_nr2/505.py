#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

void solve(void){
  int L,P,C;
  cin >> L >> P >> C;
  
  int sep=0;
  while(true){
    L = L*C;
    if(L<P){
      sep++;
    }else{
      break;
    }
  }
  int res=0;
  int i=0;
  while(0<sep){
    res++;
    sep = sep >> 1;
  }

  cout << res << endl;
}

int main(void){
  int caseCount;
  cin >> caseCount;
  for(int i=1; i<=caseCount; i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}
