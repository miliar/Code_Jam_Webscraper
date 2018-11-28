#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)

#define MAX 5

int n_tests,test;
int i,j,k;
int n;
double X[MAX],Y[MAX],R[MAX],ans;

double f(int a,int b) {
  return (R[a] + R[b] + sqrt((X[a]-X[b])*(X[a]-X[b]) + (Y[a]-Y[b])*(Y[a]-Y[b])))/2;
}

int main() {
  scanf("%d",&n_tests);
  for_to(test,1,n_tests) {
    scanf("%d",&n);
    for_to(i,0,n-1) {
      scanf("%lf %lf %lf",&X[i],&Y[i],&R[i]);
    }
    if (n == 1) {
      ans = R[0];
    } else if (n == 2) {
      ans = max(R[0],R[1]);
    } else {
      ans = min (
            max(R[0],f(1,2)),
            min(
            max(R[1],f(0,2)),
            max(R[2],f(1,0)))
      );
    }
    printf("Case #%d: %.6lf\n",test,ans);
  }
  return 0;
}
