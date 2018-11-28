#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

#define REP(i, to) for(int i=0; i<to; i++)

using namespace std;
typedef unsigned int uInt;
typedef long long int llInt;

char T[128][128];
double W[128][128];
double WP[128][128];
double OWP[128];
double OOWP[128];

double avg(double* A, int N, int team, int without = -1){
    double result = 0.0;
    int played = 0;
    REP(i, N) if(T[team][i] != '.' && i != without){
      played++;
      result += A[i];  
    }
    if(played == 0) return 0.0;
    return result / ((double) played);
}


int main()
{
  int Te;
  scanf("%d", &Te);
  REP(t, Te){
    int N;
    scanf("%d", &N);
    REP(i, N) scanf("%s", T[i]);
    REP(i, N) REP(j, N) W[i][j] = ((T[i][j]=='1')?1.0:0.0);
      
    REP(i, N) REP(j, N) WP[i][j] = avg(W[j], N, j, i);
    REP(i, N) OWP[i] = avg(WP[i], N, i);
    REP(i, N) OOWP[i] = avg(OWP, N, i);
    
    printf("Case #%d:\n", t+1);
    REP(i, N) printf("%.10f\n", 0.25 * WP[i][i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
  }
  
  return 0;
}
