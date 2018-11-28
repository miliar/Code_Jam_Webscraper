#include<iostream>
#include <cstdio>
#include <algorithm>
#define E 1e-8
#define MAX 1000001
using namespace std;
 

double arr[MAX];
 
bool solvable(int n, double t, double d) {
  double x = arr[0]-d;
  
  for (int i = 1; i < n; ++i) {
    if (arr[i]+d<x+t) return false;
    x = max(arr[i]-d,x+t);
  }
  return true;
}
 
int main() {
  int T,P,V;
  scanf("%d", &T);
  for(int I=1;I<=T;I++) {
    int C, D,N=0;
    scanf("%d%d", &C, &D);
    for (int i=0; i<C;i++){
		scanf("%d%d",&P,&V);
		for(int j=0;j<V;j++) arr[N++]=P;
	}
    sort(arr,arr+N);
    double st = 0, en = 1,mid;
    while (!solvable(N, D, en)) en*=2;
    while (st+E<en) {
      mid = (st+en)/2;
      if (solvable(N,D,mid)) en = mid;
      else st = mid;
    }
    printf("Case #%d: %.8lf\n",I,mid);
  }
}
 
