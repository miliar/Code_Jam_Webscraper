#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cstdio>

using namespace std;

typedef long long ll;

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    int n;
    cin >> n;
    char g[n][n];
    int num[n];
    int wp[n];
    double owp[n];
    for(int i = 0; i < n; ++i){
      num[i] = owp[i] = wp[i] = 0;
      for(int j = 0; j < n; ++j){
        cin >> g[i][j];
        if(g[i][j] != '.'){
          ++num[i];
          if(g[i][j] == '1')
            ++wp[i];
        }
      }
    }

    for(int i = 0; i < n; ++i){
      int cnt = 0;
      for(int j = 0; j < n; ++j){
        if(i != j && g[i][j] != '.'){
          ++cnt;
          if(num[j] > 1){
            owp[i] += (wp[j] - (g[j][i] - '0')) / (double)(num[j] - 1);
          }
        }
      }
      if(cnt != 0) owp[i] /= cnt;
    }


    cout << "Case #" << k+1 << ":" << endl;
    for(int i = 0; i < n; ++i){
      double res = 0;
      if(num[i] > 0) res += 0.25 * wp[i] / num[i];
      res += 0.5 * owp[i];
      double soowp = 0;
      for(int j = 0; j < n; ++j)
        if(g[i][j] != '.')
          soowp += owp[j];
      if(num[i] > 0) res += 0.25 * soowp / num[i];
      printf("%.10lf\n", res);
    }
  }


  return 0;
}
