//Ulf LundstrÅˆm

#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
const enum {SIMPLE, FOR, WHILE} mode = FOR;

#define ever (;;)
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef map<string,bool> msb;
  
char name[1000];

bool solve(int P) {
  int S;
  scanf("%d",&S);
  gets(name);
  msb used;
  for (int i = 0; i < S; ++i) {
    gets(name);
    used[string(name)] = false;
  }
  int Q;
  scanf("%d",&Q);
  gets(name);
  int n = 0, res = 0;
  for (int i = 0; i < Q; ++i) {
    gets(name);
    //printf("%s: n=%d, res=%d\n",name,n,res);
    msb::iterator it;
    if ((it=used.find(string(name)))!=used.end()) {
      n += !it->second;
      it->second = true;
    }
    if (n == S) {
      for (msb::iterator it2 = used.begin(); it2 != used.end(); ++it2)
	it2->second = false;
      it->second = true;
      ++res;
      n = 1;
    }
  }
  printf("Case #%d: %d\n",P+1,res);
  return true;
}

int main() {
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%i", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
