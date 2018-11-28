#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int main () {
  int C;
  scanf("%d", &C);
  
  for (int c = 1; c <= C; c++) {
    int N;
    scanf ("%d", &N);
    double resp;
    vector<int> plantx (N), planty(N), radius(N);
    for (int i = 0; i < N; i++)
      scanf ("%d%d%d", &(plantx[i]), &(planty[i]), &(radius[i]));
    
    if (N == 1)
      resp = radius[0];
    else if (N == 2) {
      if (radius[0] > radius[1])
        resp = radius[0];
      else
        resp = radius[1];
    }
    else {
      double maxR = 10000000.0;
      double dist = sqrt((plantx[1] - plantx[0])*(plantx[1] - plantx[0]) + (planty[1] - planty[0])*(planty[1] - planty[0])) + radius[0] + radius[1];
      dist /= 2;
      if (dist > radius[2]) {
        if (dist < maxR)
          maxR = dist;
      }
      else {
        if (radius[2] < maxR)
          maxR = radius[2];
      }
      
      dist = sqrt((plantx[2] - plantx[0])*(plantx[2] - plantx[0]) + (planty[2] - planty[0])*(planty[2] - planty[0])) + radius[0] + radius[2];
      dist /= 2;
      if (dist > radius[1]) {
        if (dist < maxR)
          maxR = dist;
      }
      else {
        if (radius[1] < maxR)
          maxR = radius[1];
      }
      
      dist = sqrt((plantx[2] - plantx[1])*(plantx[2] - plantx[1]) + (planty[2] - planty[1])*(planty[2] - planty[1])) + radius[2] + radius[1];
      dist /= 2;
      if (dist > radius[0]) {
        if (dist < maxR)
          maxR = dist;
      }
      else {
        if (radius[0] < maxR)
          maxR = radius[0];
      }
      resp = maxR;
    }
    
    printf ("Case #%d: %.6f\n", c, resp);
  }
  return 0;
}
