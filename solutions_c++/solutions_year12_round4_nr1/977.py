#include <iostream>
#include <cstdlib>
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
typedef vector<pair<LL,LL> > VPLL;
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

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

int TT;
int N,D;
int dlz[10500];
int vzd[10500];
double naj[10500];

double gts(int prep, int odv){
  return sqrt( prep * prep - odv * odv );  
}

int main(){
  scanf("%d ",&TT);
  FOR(tt,TT){
    scanf("%d ",&N);
    FOR(i,N){
      scanf("%d %d ",&vzd[i],&dlz[i]);
      naj[i] = -1;
    }
    scanf("%d ",&D);
    naj[0] = vzd[0];
    //MAME za sebou i lian
    FOR(i,N-1){
      naj[i+1] = -1;
      FOR(j,i+1){
	if (naj[j] >= (vzd[i+1] - vzd[j])){
	  //uble dokazem = gts(naj[j], vzd[i+1] - vzd[j]) + naj[j];
	  double dokazem = vzd[i+1] - vzd[j];
	  if (dokazem > dlz[i+1]) dokazem = dlz[i+1];
	  if (dokazem > naj[i+1]) naj[i+1] = dokazem;
	}
      }  
      if (naj[i+1] < 0) break;
    }

//    FOR(i,N) printf("liana %d: %lf\n",i,naj[i]);

    //pome
    int bol = 0;
    FOR(i,N) if (naj[i] > -1) if (D - vzd[i] <= naj[i]) bol = 1;
    printf("Case #%d: ",tt+1);
    if (bol) printf("YES\n");
    else printf("NO\n");

  }
}
