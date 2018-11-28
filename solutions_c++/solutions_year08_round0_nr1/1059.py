#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)

#define dlong unsigned long long int  /* 64b for unix    : %llu  */
// #define dlong __int64              /* 64b for windows : %I64u */

#define INF 1000000000

int N;
int S;
int Q;
char name [101];
map<string,int> SE;
int QT [1001];
int memo [101][1001];

int go (int se, int pos) {
  int p = pos, res = INF;
  if (memo[se][p] != -1) return memo[se][p];
  
  while (p < Q && QT[p] != se) ++p;
  if (p == Q) return 0;

  FORU(s,0,S-1) {
    if (s != se) {
      int ret = 1 + go(s,p);
      res = min(res,ret);
    }
  }

  memo[se][pos] = res;
  return res;
}

int main () {

  scanf("%d\n",&N);
  FORU(i,0,N-1) {
    SE.clear();

    scanf("%d\n",&S);
    FORU(j,0,S-1) {
      gets(name);
      SE.insert(MP(name,j));
    }
    scanf("%d\n",&Q);
    FORU(j,0,Q-1) {
      gets(name);
      QT[j] = SE[name];
    }
    
    FORU(s,0,100) FORU(p,0,1000) memo[s][p] = -1;

    int best = INF;
    FORU(s,0,S-1) {
      int res = go(s,0);
      best = min(best, res);
    }

    printf("Case #%d: %d\n",i+1,best);
  }

  return 0;
}
