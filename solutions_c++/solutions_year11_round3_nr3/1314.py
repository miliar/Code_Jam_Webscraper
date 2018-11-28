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
  long long L,H;
  long long  note[1<<16];
  cin >> N >> L >> H;
  for(int i=0; i<N; i++){
    cin >> note[i];
  }

  for(int i=L; i<=H; i++){
    bool t = true;
    for(int j=0; j<N; j++){
      long long a,b;
      if(note[j] >= i){
        a = note[j];
        b = i;
      }else{
        a = i;
        b = note[j];
      }
      if(a%b != 0 ){
        t = false;
        break;
      }
    }
    if(t){
      cout << i << endl;
      return;
    }
  }
  
  cout << "NO" << endl;
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
