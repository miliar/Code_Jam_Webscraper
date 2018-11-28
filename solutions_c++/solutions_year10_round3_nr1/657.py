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
  int N,A[1000],B[1000];
  int res=0;
  cin >> N;
  for(int i=0; i<N; i++){
    cin >> A[i] >> B[i];
  }
  for(int i=0; i<N; i++){
    for(int j=0; j<i; j++){
      if((A[j]-A[i])*(B[j]-B[i]) < 0){
        res++;
      }
    }
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
