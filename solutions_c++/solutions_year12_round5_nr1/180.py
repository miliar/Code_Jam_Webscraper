#include<algorithm>
#include<bitset>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<functional>
#include<iostream>
#include<limits>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#include<numeric>
#include<ext/numeric>  // iota
//#include<ext/hash_set>
//#include<ext/hash_map>

using namespace std;
using namespace __gnu_cxx; // Pour utiliser les ext/...

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> pii;
//typedef int int128 __attribute__ ((mode(TI)));
//typedef unsigned int uint128 __attribute__ ((mode(TI)));
//
typedef std::pair<double, int> Pair;


struct CmpPair
{
      bool operator()(const Pair& a, const Pair& b)
            { return (a.first < b.first || a.first == b.first && a.second < b.second); }
};

#define MAX 1002
int infty = numeric_limits<int>::max();

vector<Pair> stuff;
int cost[MAX];

int main(int argc, char **argv) {
  int T, i, A, B, j;
  int N;
  long double p[MAX];
  int buf, buf2;
  scanf("%d", &T);
  for (i=0; i<T; i++) {
    scanf("%d", &N);
    stuff.clear();
    for (j=0; j<N; j++) {
      scanf("%d", &buf2);
      cost[j] = buf2;
    }
    for (j=0; j<N; j++) {
      scanf("%d", &buf);
      stuff.push_back(Pair(((double) buf)/cost[j], MAX-j));
    }
    sort(stuff.begin(), stuff.end(), CmpPair());
    printf("Case #%d: ", i+1);
    for (j=0; j<N; j++) {
      int c = stuff.back().second;
      stuff.pop_back();
      printf("%s%d", !j?"":" ", MAX-c);
    }
    printf("\n");
  }
  return 0;
}
