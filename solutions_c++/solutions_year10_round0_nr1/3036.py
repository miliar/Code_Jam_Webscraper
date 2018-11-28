#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
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

int main(void){
  int T, N, K;
  cin >> T;
  for(int i=1; i<=T; i++){
    cin >> N;
    cin >> K;
    if((K%(1<<N)) == (1<<N)-1){
      printf("Case #%d: ON\n", i);
    }else{
      printf("Case #%d: OFF\n", i);
    }
  }
  return 0;
}
