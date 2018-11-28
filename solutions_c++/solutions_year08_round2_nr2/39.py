/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long ll;

inline int biggest(int x, int y) {
	int tmp = __gcd(x,y);
	int dokad = tmp+1;
	FOR(i,2,dokad)
		while(tmp%i == 0) {
			tmp /= i;
			if(tmp == 1) return i;
		}
	return -1;
}

int f[1001];

int find_set(int v) {
	if(f[v] != v) f[v] = find_set(f[v]);
	return f[v];	
}

void make_union(int a, int b) {
	a = find_set(a);
	b = find_set(b);
	f[a] = b;
}

void testcase() {
	int a, b, p;
	scanf("%d%d%d", &a, &b, &p);
	FOR(i,a,b+1) f[i] = i;
	FOR(i,a,b+1) FOR(j,i+1,b+1) if(biggest(i,j) >= p) make_union(i,j);
	set<int> res;
	FOR(i,a,b+1) res.insert(find_set(i));
	printf("%d", res.size());
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
