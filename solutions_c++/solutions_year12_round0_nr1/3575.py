#include<iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef long double LD;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-10
#define INF 10000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

map<char,char> M;

int main(){
  M['a'] = 'y';
  M['b'] = 'h';
  M['c'] = 'e';
  M['d'] = 's';
  M['e'] = 'o';
  M['f'] = 'c';
  M['g'] = 'v';
  M['h'] = 'x';
  M['i'] = 'd';
  M['j'] = 'u';
  M['k'] = 'i';
  M['l'] = 'g';
  M['m'] = 'l';
  M['n'] = 'b';
  M['o'] = 'k';
  M['p'] = 'r';
  M['q'] = 'z';
  M['r'] = 't';
  M['s'] = 'n';
  M['t'] = 'w';
  M['u'] = 'j';
  M['v'] = 'p';
  M['w'] = 'f';
  M['x'] = 'm';
  M['y'] = 'a';
  M['z'] = 'q';
  int TT;
  cin >> TT;
  scanf("%*c");
  FOR(tt,TT){
    char C[1050];
    cin.getline(C,1020);
    int ln = strlen(C);
    printf("Case #%d: ",tt+1);
    FOR(i,ln){
      if (C[i] == ' ') printf(" ");
      else printf("%c",M[C[i]]);
    }
    printf("\n");
  }

}
