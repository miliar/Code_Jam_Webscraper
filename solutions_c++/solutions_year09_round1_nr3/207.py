#include <iostream>

using namespace std;

#define for_to(i,j,k) for(i=j; i<=k; ++i)
#define for_downto(i,j,k) for(i=j; i>=k; --i)

#define MAX 45

//doub
int i,j,k;
int n_tests,test;
int C,N,n;
double T[MAX][MAX];
double E[MAX];

int main() {
  for_to(n,0,40) {
    T[n][0] = 1.0;
    for_to(k,1,n-1) {
      T[n][k] = T[n-1][k] + T[n-1][k-1];
    }
    T[n][n]=1.0;
  }
  for_to(i,0,20) {
    //cout << T[10][i] << endl;
  }
  //cout << "---" << endl;
  scanf("%d",&n_tests);
  for_to(test,1,n_tests) {
    scanf("%d %d",&C,&N);

    E[0] = 0;
    for_to(i,1,C) {
      E[i] = 0;
      for_to(j,1,min(N,i)) {
        if (C-i >= N-j)
        E[i] += T[i][j]*T[C-i][N-j]*E[i-j];
      }
      E[i] /= T[C][N];
      E[i] += 1;
      if (C-i>=N)
      E[i] /= (1 - (T[C-i][N]/T[C][N]));
      //cout << "E[" << i << "]=" << E[i] << endl;
    }
    printf("Case #%d: %.7lf\n",test,E[C]);
  }
  return 0;
}
