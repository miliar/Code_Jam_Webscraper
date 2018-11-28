#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;

const int inf = 123456789;
int cas = 0;
int k;
char S[60000];
void doit() {
  scanf("%d",&k);
  scanf("%s",S);

  vector<int> pi(k,0);
  FOR(i,k) pi[i] = i;

  int ans = inf;

  do {
    char Sk[60000];
    strcpy(Sk,S);

    for (int i = 0; Sk[i]; i += k) {
      FOR(j,k) {
	Sk[i+j] = S[i+pi[j]];
      }
    }

    char prev = '~';
    int me = 0;
    for (int i = 0; Sk[i]; i++) {
      if (Sk[i] != prev) {
	me++;
	prev = Sk[i];
      }
    }
    ans <?= me;
  } while (next_permutation(BEND(pi)));

  printf("Case #%d: %d\n",++cas,ans);
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}
