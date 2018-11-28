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

char buf[100][100];
const int max_n = 80*80;

int mate1[max_n], visited[max_n], n1, n2, number, mate2[max_n];
bool edge[max_n][max_n];

bool search(int b) {
  FOR(a,0,n1)
	if(edge[a][b] && visited[a] != number) {
	  visited[a] = number;
	  if(mate1[a] == -1 || search(mate1[a])) {
		mate1[a] = b;
		mate2[b] = a;
		return true;
	  }
	}
  return false;
}

int compute_bcm() {
  int result = 0;
  FOR(i,0,n1) mate1[i] = -1;
  FOR(i,0,n2) mate2[i] = -1;
  FOR(i,0,n1) visited[i] = -10;
  number = 0;
  FOR(b,0,n2) {
	++number;
	if(search(b)) ++result;
  }
  return result;
}

bool kolory[80][80];
int numerek[80][80];

void testcase() {
  int n, m;
  scanf("%d%d", &n, &m);
  FOR(i,0,n) scanf("%s", buf[i]);
  FOR(i,0,n) FOR(j,0,m) kolory[i][j] = false;
  int ile_bialych = 0, ile_czarnych = 0;
  FOR(i,0,n) FOR(j,0,m) if( (j%2 == 0) ) {
	kolory[i][j] = true;
	numerek[i][j] = ile_bialych++;
  } else numerek[i][j] = ile_czarnych++;
  n1 = ile_bialych;
  n2 = ile_czarnych;
  FOR(i,0,n1) FOR(j,0,n2) edge[i][j] = false;
  FOR(i,0,n) FOR(j,0,m) if(kolory[i][j] && buf[i][j] == '.') {
	if(j > 0 && buf[i][j-1] == '.') edge[ numerek[i][j] ][ numerek[i][j-1] ] = true;
	if(j < m-1 && buf[i][j+1] == '.') edge[ numerek[i][j] ][ numerek[i][j+1] ] = true;
	if(i > 0) {
	  if(j > 0 && buf[i-1][j-1] == '.') edge[ numerek[i][j] ][ numerek[i-1][j-1] ] = true;
	  if(j < m-1 && buf[i-1][j+1] == '.') edge[ numerek[i][j] ][ numerek[i-1][j+1] ] = true;
	}
	if(i < n-1) {
	  if(j > 0 && buf[i+1][j-1] == '.') edge[ numerek[i][j] ][ numerek[i+1][j-1] ] = true;
	  if(j < m-1 && buf[i+1][j+1] == '.') edge[ numerek[i][j] ][ numerek[i+1][j+1] ] = true;
	
	}
	
  }
  int res = compute_bcm();
  FOR(i,0,n) FOR(j,0,m) if( (kolory[i][j] && (mate1[ numerek[i][j] ] == -1)) || ((!kolory[i][j]) && mate2[ numerek[i][j] ] == -1) ) // jesli jest nieskojarzony koles
	if(buf[i][j] == '.') ++res;
  printf("%d", res);
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
