#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL; 
typedef vector<int> VI; 
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS; 
typedef long double LD; 

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;} 
inline LL MIN(LL a, LL b){ return a < b ? a : b;} 

//inline LABS(LL a){}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int TT;
int N;
char C[150][150];
int pld[150],won[150];
double WP[150],OWP[150],OOWP[150],rpi[150];

int main(){
  scanf("%d ",&TT);
  FOR(tt,TT){
    scanf("%d ",&N);
    FOR(j,N){
      scanf("%s ",C[j]);
    }
    memset(pld,0,sizeof(pld));
    memset(won,0,sizeof(won));
    FOR(i,N){
      FOR(j,N){
        if (C[i][j] != '.') pld[i]++;
        if (C[i][j] == '1') won[i]++;
      }
    }
    FOR(i,N){
      rpi[i] = (double)won[i]/(4*pld[i]);
      double sm = 0.0;
      FOR(j,N){
        OWP[j] = 0;
//        if (C[i][j] == '.') OWP[j] = (double)won[j]/pld[j];
        if (C[i][j] == '0') OWP[j] = (double)(won[j]-1)/(pld[j]-1);
        if (C[i][j] == '1') OWP[j] = (double)won[j]/(pld[j]-1);
        sm += OWP[j];
      }
  //    printf("OWP %d %lf\n",i,sm/pld[i]);
      rpi[i] += sm/(2*pld[i]);
//      printf("bw %lf\n",rpi[i]);
      OOWP[i] = sm/pld[i];
//      printf("%d %lf\n",i,OOWP[i]);

    }
    FOR(i,N){
      double sm = 0;
      FOR(j,N) if (C[i][j] !='.') sm += OOWP[j];
      rpi[i] += sm/(4*pld[i]);
//      printf("bw %lf\n",rpi[i]);
    }
    printf("Case #%d:\n",tt+1);
    FOR(i,N){
      printf("%.10lf\n",rpi[i]);
    }
  }
  return 0;
}
