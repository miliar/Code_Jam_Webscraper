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
  int T;
  cin >> T;
  for(int i=1; i<=T; i++){
    int R, k, N;
    vector <int> g;
    cin >> R;
    cin >> k;
    cin >> N;
    for(int j=0; j<N; j++){
      int value;
      cin >> value;
      g.push_back(value);
    }

    long long res = 0;
    int r=1;
    int j=0;
    vector <pair <int, int> > calculated(N);
    for(int a=0; a<N; a++){
      calculated[a] = make_pair(-1, -1);
    }
    while(true){
      if(r==R+1){
        break;
      }
      if(calculated[j] == make_pair(-1, -1)){
        int t = j;
        long long value=0;
        for(int a=0; a<N; a++){
          if(k < value + g[j]){
            break;
          }
          value += g[j];
          j = (j+1) % N;
        }
        res += value;
        calculated[t] = make_pair(value, j);
        r++;
      }else{
        int c=0;
        int value=0;
        int next=j;
        while(true){
          value += calculated[next].first;
          next = calculated[next].second;
          c++;
          if(next == j){
            break;
          }
        }
        res += value * ((R-r+1)/c);
        r = R-(R-r+1)%c+1;
        fill(calculated.begin(), calculated.end(), make_pair(-1, -1));
      }
    }
    printf("Case #%d: %ld\n", i, res);
  }
  return 0;
}
 
