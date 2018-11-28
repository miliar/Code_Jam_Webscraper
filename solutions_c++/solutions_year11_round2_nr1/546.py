#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1e-9;

int tc, n;
char A[105][105];
double owp[105], oowp[105];

int main(){
   cin >> tc;
   for (int TC = 1; TC <= tc; TC++){
      printf("Case #%d:\n", TC);
      cin >> n;
      for (int i = 0; i < n; i++) scanf("%s",A[i]);
      for (int i = 0; i < n; i++){
         // calculate OWP
         double totalwp = 0.0;
         int cnt = 0;
         for (int j = 0; j < n; j++){
            if (j == i || A[i][j] == '.') continue;
            int total = 0, win = 0;
            for (int k = 0; k < n; k++){
               if (A[j][k] == '.' || k == i) continue;
               if (A[j][k] == '1') win++;
               total++;
            }
            totalwp += (double) win/total;
            cnt ++ ;
         }
         owp[i] = totalwp / cnt;
      }
      for (int i = 0; i < n; i++){
         oowp[i] = 0.0;
         int cnt = 0;
         for (int j = 0; j < n; j++){
            if (i == j || A[i][j] == '.') continue;
            oowp[i] += owp[j];
            cnt++;
         }
         oowp[i] /= cnt;
      }
      for (int i = 0; i < n; i++){
         int win = 0, total = 0;
         for (int j = 0; j < n; j++){
            if (A[i][j] == '.') continue;
            if (A[i][j] == '1') win++;
            total++;
         }
         double ans = 0.25 * (double) win / total + 0.5 * owp[i] + 0.25 * oowp[i];
         printf("%.9lf\n", ans);
      }
   }
   return 0;
}

