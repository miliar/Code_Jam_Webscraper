#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define STRING(x) #x
#define PING cerr << "(" << __LINE__ << "): " << __FUNCTION__ << endl
#define PRINT(x) cerr << STRING(x) << " = " << (x) << endl

typedef long long LL;
typedef unsigned long long ULL;
const int INF = 1000000000; const LL INFLL = LL(INF) * LL(INF);
template<class T> inline int size(const T&c) { return c.size(); }

const int N = 'z' - 'a';

char map[N + 1];

int main() {
  map['a' - 'a'] = 'y';
  map['b' - 'a'] = 'h';
  map['c' - 'a'] = 'e';
  map['d' - 'a'] = 's';
  map['e' - 'a'] = 'o';
  map['f' - 'a'] = 'c';
  map['g' - 'a'] = 'v';
  map['h' - 'a'] = 'x';
  map['i' - 'a'] = 'd';
  map['j' - 'a'] = 'u';
  map['k' - 'a'] = 'i';
  map['l' - 'a'] = 'g';
  map['m' - 'a'] = 'l';
  map['n' - 'a'] = 'b';
  map['o' - 'a'] = 'k';
  map['p' - 'a'] = 'r';
  map['q' - 'a'] = 'z';
  map['r' - 'a'] = 't';
  map['s' - 'a'] = 'n';
  map['t' - 'a'] = 'w';
  map['u' - 'a'] = 'j';
  map['v' - 'a'] = 'p';
  map['w' - 'a'] = 'f';
  map['x' - 'a'] = 'm';
  map['y' - 'a'] = 'a';
  map['z' - 'a'] = 'q';
  int T;
  scanf("%d\n", &T);
  char str[128];
  REP(t, T) {
    gets(str);
    const int len = strlen(str);
    REP(i, len) if (str[i] != ' ') str[i] = map[str[i] - 'a'];
    printf("Case #%d: ", t + 1);
    puts(str);
  }
  return 0;
}


