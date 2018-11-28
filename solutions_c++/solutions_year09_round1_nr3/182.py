#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

double choose(int A,int B) {

  if(B == 0) return 1;
  return choose(A-1,B-1)*((double)A/B);

}

double transition(int i, int j, int C, int N) {
	int m = j-i;
  if(m > N) return 0;
  if(m < 0) return 0;
  return choose(C-i,m) * choose(i,N-m) / choose(C,N);
}

int main(void)
{
  int T;
  cin >> T;

  for (int c = 1; c <= T; c++) {
    int N, C;
    cin >> C >> N;
    double P[C+1][C+1];
    double E[C+1];

    for(int i = 0; i <= C; i++) {
	    E[i] = 0;
      for(int j = 0; j <= C; j++) {
        P[i][j] = transition(i,j,C,N);
      }
    }
    E[C] = 0;
  
    for(int i = C-1; i >= 0; i--) {
      E[i] = 0;
      for(int j = i+1; j <= C; j++) {
        E[i] += P[i][j]*E[j]; 
      }
      E[i] += 1;
      E[i] /= (1 - P[i][i]);
    }

    /*
  for(int i = 0; i <= C; i++) {
      for(int j = 0; j < i; j++) {
        printf("         ");
      }
      for(int j = i; j <= C; j++) {
        printf("%1.6f ", P[i][j]);
      }
      printf(": %1.6f ", E[i]);
      printf("\n");
    }*/

    printf("Case #%d: %f\n", c, E[0]);
  }
}
