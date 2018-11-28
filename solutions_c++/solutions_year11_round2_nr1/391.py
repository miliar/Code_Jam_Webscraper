#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  string str;
  int n;
  FOR (test, tests){
    cin >> n;
    int m[n][n];
    SET(m, 255);
    FOR (i, n){
      cin >> str;
      FOR (j, n)
        if (str[j] == '1')
          m[i][j] = 1;
        else if (str[j] == '0')
          m[i][j] = 0;
    }
    
    double wp[n];
    FOR (i, n){
      double cnt = 0.0, w = 0.0;
      FOR (j, n){
        cnt += m[i][j] != -1;
        w += m[i][j] == 1;
      }
      if (cnt > 1e-9)
        wp[i] = w / cnt;
      else
        wp[i] = 0.0;
    }
    
    double owp[n];
    SET(owp, 0);
    FOR (i, n){
      double cc = 0.0, s = 0.0;
      FOR (j, n){
        if (m[i][j] == -1)
          continue;
        cc += 1.0;
        double cnt = 0.0, w = 0.0; 
        FOR (k, n){
          if (k == i)
            continue;
          cnt += m[j][k] != -1;
          w += m[j][k] == 1;
        }

        if (cnt > 1e-9)
          s += w / cnt;
      }
      if (cc > 1e-9)
        owp[i] = s / cc;
    }

    double oowp[n];
    FOR (i, n){
      double s = 0.0, cnt = 0.0;
      FOR (j, n){
        if (m[i][j] == -1)
          continue;
        s += owp[j];
        cnt++;
      }
      if (cnt > 1e-9)
        oowp[i] = s / cnt;
    }
    

    cout << "Case #" << (test + 1) << ": ";
    cout << "\n";
    FOR (i, n)
      printf("%.11lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
  }
  return 0;
}
