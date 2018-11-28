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
#define COMMENT 1
using namespace std;

typedef unsigned uint;
typedef long long int llint;
typedef pair<int,int> PII;

int T,N,K;

int main(){
  scanf("%d",&T);
  for (int t=1; t<=T; t++){
    scanf("%d %d",&N,&K);
    bool ok=true;
    for (int i=0; i<N; i++)
      if (!((K>>i)&1)) ok=false;
    printf("Case #%d: %s\n",t,ok?"ON":"OFF");
  }
}
