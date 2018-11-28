#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
int X[10], Y[10], R[10];
double dist(int a, int b){
  return sqrt(((X[a]-X[b])*(X[a]-X[b]))+((Y[a]-Y[b])*(Y[a]-Y[b])));
}
int main(){
  int c;
  scanf("%d", &c);
  for(int i=0; i<c; i++){
    int n;
    scanf("%d", &n);
    for(int j=0; j<n; j++){
      scanf("%d%d%d", &X[j], &Y[j], &R[j]);
    }
    double wynik=20000000;
    double loc;
    if(n==3){
      //sytuacje (0, 1) i 2
      loc=max(dist(0, 1)+R[0]+R[1], (double)(2*R[2]));
      //printf("1: %lf", loc);
      wynik=min(loc, wynik);
      //sytuacja (1, 2) i 0
      loc=max(dist(1, 2)+R[1]+R[2], (double)(2*R[0]));
      //printf("2: %lf", loc);
      wynik=min(loc, wynik);
      //sytuacja (0, 2) i 1
      loc=max(dist(0, 2)+R[0]+R[2], (double)(2*R[1]));
      //printf("3: %lf", loc);
      wynik=min(loc, wynik);
    }else if(n==2){
      wynik=max(2*R[0], 2*R[1]);
    }else if(n==1){
      wynik=2*R[0];
    }
    printf("Case #%d: %.6lf\n", i+1, wynik/2);
  }
  return 0;
}
