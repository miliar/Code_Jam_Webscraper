#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>

using namespace std;

template<class T> inline T gcd(T a, T b){return b==0?a:gcd(b,a%b);}
template<class T> inline T lcm(T a, T b){return a*(b/gcd(b,a%b));}
const double pi=acos(-1.0);


int main(){
  int n_testcases;
  cin >> n_testcases;

  int d[100];

  for (int testcase = 1; testcase <= n_testcases; testcase++){
    int N;
    cin >> N;
    char l[100];
    cin.getline(l, 100);
    for (int i = 0; i < N; i++){
      cin.getline(l, 100);
      d[i] = string(l).find_last_of('1');
      //cerr << d[i] << endl;
    }

    int c = 0;
    while(1){
      //find first unhappy
      int u = 0;
      while (u >= d[u] && u < N)
        u++;
      if (u == N)
        break;

      //search first index t after u with d[t] <= u
      int t;
      for (t = u+1; d[t] > u; t++)
        ;

      c += (t - u);
      int temp = d[t];
      for (int i = t; i > u; i--)
        d[i] = d[i-1];
      d[u] = temp;
    }

    cout << "Case #" << testcase << ": " << c << endl;
  }
  return 0;
}
