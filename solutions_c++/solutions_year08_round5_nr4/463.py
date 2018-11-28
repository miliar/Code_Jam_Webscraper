/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long ll;

int koles[100][100];
bool zle[100][100];

void testcase() {
  int h, w, r;
  scanf("%d%d%d", &h, &w, &r);
  FOR(i,0,h) FOR(j,0,w) {  zle[i][j] = false; koles[i][j] = 0; }
  FOR(i,0,r) {
	int x, y;
	scanf("%d%d", &x, &y);
	zle[x-1][y-1] = true;
  }
  koles[0][0] = 1;
  if(zle[0][0] == true) koles[0][0] = 0;
  FOR(i,0,h) FOR(j,0,w) {
	if(zle[i][j]) continue;
	if(i > 0 && j > 1) koles[i][j] += koles[i-1][j-2];
	if(i > 1 && j > 0) koles[i][j] += koles[i-2][j-1];
	koles[i][j] %= 10007;
  }
  printf("%d", koles[h-1][w-1]);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,0,t) {
	printf("Case #%d: ", i+1);
	testcase();
	printf("\n");
  }
  return 0;
}
