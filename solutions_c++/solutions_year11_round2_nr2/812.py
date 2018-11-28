#include <iostream>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX 220

int cpos[MAX], ci[MAX];
int n;
int d;

bool poss(double k) {
  double lastpos = -99999999999.0;
  for (int i = 0; i<n; i++) {
    lastpos = max(lastpos, cpos[i]-k);
    lastpos = lastpos + (ci[i]-1)*d;
    //cout << lastpos << " " << cpos[i]+k << endl;
    if (lastpos > cpos[i]+k) {
      return false;
    }
    lastpos+=d;
  }
  return true;
}

double bs(double start, double end){
  double mid = start;
  
  while (start + 1e-8 <= end){
      mid = (start + end) / 2;
      //cout << "--- " << start << " " << mid << " " << end << endl;
      if (poss(mid)) end = mid;
      else start = mid;
   }
   return mid;
}

int main() {
  int tt; 
  cin >> tt;
  for (int t = 1; t<=tt; t++) {
    cin >> n >> d;
    long long num = 0;
    for (int i = 0; i < n; i++) {
      cin >> cpos[i] >> ci[i];
      num+=ci[i];
    }
    //cout << num*(cpos[n-1]-cpos[0]) << endl;
    double ans = bs(0, num*1000000);
    printf("Case #%d: %.8lf\n",t, ans);
  }
  return 0;
}
