#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <complex>
#define MP              make_pair
#define CMNT            1
#define INF             0x3fffffff
#define MM(s,a)         memset((s),(a),sizeof((s)))
using namespace std;

typedef unsigned           uint;
typedef long long int     llint;
typedef pair<int,int>       PII;
typedef pair<double,double> PDD;

int T,N;
int at[2]; // current pos
int P[101]; // destination (task) pos
int C[101]; // destination (task) color

int main(){
  scanf("%d",&T);
  for (int t=1; t<=T; t++){
    scanf("%d",&N);
    memset(P,0,sizeof P);
    memset(at,0,sizeof at);
    memset(C,0,sizeof C);
    char color; 
    for (int i=0; i<N; i++) {
      scanf(" %c %d",&color,&P[i]);
      P[i]--;
      if (color=='O') C[i]=0; 
      else            C[i]=1;
    }
    
    int time=0;
    for (int i=0; i<N; i++){
      int ct=C[i],cf=(C[i]==0)?1:0;
      int move=abs(at[ct]-P[i])+1;
      time+=move;
      at[ct]=P[i];

      for (int j=i+1; j<N; j++)
	if (C[j]==cf){
	  if (at[cf]<P[j]) at[cf]+=min(move,abs(P[j]-at[cf]));
	  else             at[cf]-=min(move,abs(P[j]-at[cf]));
	  break;
	}
    }
    printf("Case #%d: %d\n",t,time);
  }
}
