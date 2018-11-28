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
  int n,s,p;
  vector<int> googlers;
  cin >> n >> s >> p;
  for(int i=0; i<n; i++){
    int tmp;
    cin >> tmp;
    googlers.push_back(tmp);
  }

  sort(googlers.begin(), googlers.end(), greater<int>());
  
  int res = 0;
  for(int i=0; i<n; i++){
    if(googlers[i] >= 3*p-2){
      res++;
    }else if(0 < s && ((p==1 && googlers[i] >= 1) || (p!=1 && googlers[i] >= 3*p-4))){
      res++;
      s--;
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
