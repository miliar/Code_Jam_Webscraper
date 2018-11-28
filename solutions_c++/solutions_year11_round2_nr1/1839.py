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
char S[200][200];
double WP[200],OWP[200],OOWP[200];
int noplay,play,lost,win;
int NP[200];

int main(){
  scanf("%d",&T);
  for (int t=1; t<=T; t++){
    memset(NP,0,sizeof NP);
    memset(WP,0,sizeof WP);
    memset(OWP,0,sizeof OWP);
    memset(OOWP,0,sizeof OOWP);
   
    scanf("%d",&N);

    for (int i=0; i<N; i++){
      scanf("%s",S[i]);
      play=0; noplay=0; lost=0; win=0;
      for (int j=0; j<N; j++){
	if (S[i][j]=='.') {noplay++; NP[i]++;}
	else if (S[i][j]=='0') lost++;
	else if (S[i][j]=='1') win++;
	WP[i]=win/((double)(N-noplay));
      }
      //      printf("WP %d: %lf\n",i,WP[i]);
    }

    for (int i=0; i<N; i++){
      for (int j=0; j<N; j++){
	if (S[i][j]=='.') continue;
	play=0; noplay=0; lost=0; win=0;
	for (int k=0; k<N; k++){
	  if (i==k) {noplay++; continue;}
	  if (S[j][k]=='.') noplay++;
	  else if (S[j][k]=='0') lost++;
	  else if (S[j][k]=='1') win++;
	}
	OWP[i]+=  ((double)win/((double)(N-noplay))) /((double)(N-NP[i]));
	//	printf("at %d %d,tmp %lf play %d noplay %d win %d NP %d OWP %lf\n",i,j,(double)win/(double)(N-noplay),play,noplay,win,NP[i],OWP[i]);
      }
      //      printf("OWP %d %lf\n",i,OWP[i]);
    }

    for (int i=0; i<N; i++)
      for (int j=0; j<N; j++){
	if (S[i][j]=='.') continue;
	OOWP[i]+=OWP[j]/((double)(N-NP[i]));
      }

    printf("Case #%d:\n",t);
    for (int i=0; i<N; i++){
      printf("%lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
    }
  }
}

