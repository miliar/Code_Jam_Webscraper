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

const int duzo = 100000;

bool zmienialne[10001];
bool endzior[10001];
bool wartosc[10001];
int ile[10001][2];
int emka, limit;

void szukaj(int v) {
  if(v > emka) return;
  ile[v][0] = ile[v][1] = duzo;
  if(v > limit) { if(wartosc[v]) ile[v][1] = 0; else ile[v][0] = 0; return; } // jesli jest lisciem
  szukaj(2*v);
  szukaj(2*v+1);
	if(endzior[v]) {
	  ile[v][0] = min(ile[v][0], min(ile[2*v][0], ile[2*v+1][0]));
	  ile[v][1] = min(ile[v][1], ile[2*v][1]+ile[2*v+1][1]);
	}
	else {
	  ile[v][0] =  min(ile[v][0], ile[2*v][0]+ile[2*v+1][0]);
	  ile[v][1] = min(ile[v][1], min(ile[2*v][1], ile[2*v+1][1]));
	}
  if(zmienialne[v]) {
	if(endzior[v]) { // zmieniamy na ORa
	  ile[v][0] =  min(ile[v][0], ile[2*v][0]+ile[2*v+1][0]+1);
	  ile[v][1] = min(ile[v][1], min(ile[2*v][1], ile[2*v+1][1])+1);	
	} else {
	  ile[v][0] = min(ile[v][0], min(ile[2*v][0], ile[2*v+1][0])+1);
	  ile[v][1] = min(ile[v][1], ile[2*v][1]+ile[2*v+1][1]+1);	
	}
  }
}

void testcase() {
  int M, V;
  scanf("%d%d", &M, &V);
  limit = (M-1)/2;
  emka = M;
  FOR(i,1,limit+1) {
	int g, c;
	scanf("%d%d", &g, &c);
	zmienialne[i] = c;
	endzior[i] = g;
  }
  FOR(i,limit+1,M+1) {
	int x;
	scanf("%d", &x);
	wartosc[i] = x;
  }
  szukaj(1);
  if(ile[1][V] >= duzo)  { printf("IMPOSSIBLE"); }
  else printf("%d", ile[1][V]);
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
