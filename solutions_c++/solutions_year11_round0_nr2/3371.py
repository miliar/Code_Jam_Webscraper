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
#define CMNT            0
#define INF             0x3fffffff
#define MM(s,a)         memset((s),(a),sizeof((s)))
using namespace std;

typedef unsigned           uint;
typedef long long int     llint;
typedef pair<int,int>       PII;
typedef pair<double,double> PDD;

int T,C,D,N;
char SC[37][3]; // combine 
char SD[29][2]; // oppose
char SN[101];   // input string
char SB[]="QWERASDF";

void combine(char *W, int *w){
  for (int i=0; i<C; i++)
    if (
	(W[*w-1]==SC[i][0] && W[*w-2]==SC[i][1]) ||
	(W[*w-1]==SC[i][1] && W[*w-2]==SC[i][0])){
      --*w;
      W[*w-1]=SC[i][2];
    }
}

void oppose(char *W, int *w){
  for (int i=0; i<(*w-1); i++)
    for (int j=0; j<D; j++){
#if CMNT
      printf("opp at %c %c, {%c %c}\n",W[*w-1],W[i],SD[j][0],SD[j][1]);
#endif
      if ((W[i]==SD[j][0] && W[*w-1]==SD[j][1]) ||
	  (W[i]==SD[j][1] && W[*w-1]==SD[j][0])){
	*w=0;
      }
    }
}
  

int main(){
  scanf("%d",&T);
  for (int t=1; t<=T; t++){
    scanf("%d",&C);
    for (int i=0; i<C; i++) scanf("%s",SC[i]);
    scanf("%d",&D);
    for (int i=0; i<D; i++) scanf("%s",SD[i]);
    scanf("%d",&N);
    scanf("%s",SN);
    
    char W[200];
    int w=0;
    for (int i=0; i<N; i++){
      W[w++]=SN[i];
      if (w>1) combine(W,&w);
      if (w>1) oppose(W,&w);
#if CMNT
      for (int i=0; i<w; i++) putchar(W[i]);
      printf("\t\tw=%d\n",w);
#endif
    }
    printf("Case #%d: [",t);
    for (int i=0; i<w-1; i++) printf("%c, ",W[i]);
    if (w>0) printf("%c",W[w-1]);
    printf("]\n");
  }
}
