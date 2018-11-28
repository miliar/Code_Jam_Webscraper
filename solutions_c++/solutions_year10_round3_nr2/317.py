#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <ctime>
// #define NDEBUG
#include "assert.h"
#include "string.h"
#define MP make_pair
#define COMMENT 0
using namespace std;

typedef unsigned uint;
typedef long long int llint;
typedef pair<int,int> PII;

int T,R=0,C,P,L;

int main(){
  scanf("%d",&T);
  while (R++<T){
    scanf("%d %d %d",&L,&P,&C);
    int cnt,tmp;
    if (C!=1){
      cnt=-1,tmp=P;
      while (tmp>L){
	cnt++;
	if (tmp%C!=0) tmp=1+tmp/C;
	else tmp/=C;
#if COMMENT
	printf("%d\n",tmp);
#endif
      }
#if COMMENT
      printf("cnt %d\n",cnt);
#endif
    }
    else cnt=P-L-1;
    
    int p=1,sol=0;
    for (int i=0; i<33; i++) {
      if (cnt<p) break;
      else {p*=2; sol++;}}
    printf("Case #%d: %d\n",R,sol);
  }
}
