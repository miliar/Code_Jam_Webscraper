#include <assert.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string>
#include <list>
#include <stack>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <list>
#define INF 0x3fffffff
#define LINF 0x3fffffffffffffffll
#define DINF 1e100
#define EPS 0.000000000001

typedef long long ll;
#define PII pair<int, int>
#define PLL pair<ll, ll>
#define PDD pair<double, double>
#define PIL pair<int, ll>
#define PLI pair<ll, int>
#define PID pair<int, double>
#define PDI pair<double, int>
#define PLD pair<ll, double>
#define PDL pair<double, ll>

#define NUL(x) memset(x, 0, sizeof(x))
#define MINUS(x) memset(x, 0xff, sizeof(x))
#define PQ(x) priority_queue< x >  //highest first
#define PQR(x) priority_queue< x , vector< x > , greater < x > > //lowest first
#define MP make_pair
#define PB push_back
#define IT(x) for (typeof((x).begin()) it = (x).begin() ; it != (x).end() ; it++)
#define IT2(x) for (typeof((x).begin()) it2 = (x).begin() ; it2 != (x).end() ; it2++)
#define FOR(i, a, b) for (int i = (a) ; i< (b) ; i++)
#define DEB(x...) fprintf(stderr,x)
//#define DEB

using namespace std;

char mp[255];

char* orig[3]={
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char* dec[3]={
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up"
};

void prec() {
  NUL(mp);
  FOR(i,0,3) {
    assert(strlen(orig[i])==strlen(dec[i]));
    FOR(j,0,strlen(orig[i]))
      mp[orig[i][j]] = dec[i][j];
  }

  /*  FOR(i,'a','z'+1) if (!mp[i]) {
    DEB("Missing %c\n", i);
    }*/

  mp['z']='q';
  mp['q']='z';
}

bool testc(int tc=0) {
  char buf[200];
  gets(buf);
  int i=-1;
  while(buf[++i]) buf[i] = mp[buf[i]];
  printf("Case #%i: %s\n", tc, buf);
}



int main()
{
  prec(); 
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);

  return 0;
}
