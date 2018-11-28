#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751

	  int A, B, P;


void merge(int T[], int a, int b) {
	if(T[a] == T[b]) return;
	int s = T[b];
	for(int i = A; i <= B; i++) if(T[i] == s) T[i] = T[a];
}

int Prim[1001];

int main() {

	for(int i = 2; i < 1000; i++) {
		Prim[i] = 1;
		for(int j = 2; j*j <= i; j++)
			if(i % j == 0) Prim[i] = 0;
	}


  int C;
  cin >> C;
  for(int i = 1; i <= C; i++) {
	  cin >> A >> B >> P;

	  int T[1001];
	  for(int k = A; k <= B; k++) 
		  T[k] = k;

	  for(int p = P; p <= B; p++) if(Prim[p]) {
		  int kmin = A/p;
		  if(kmin*p < A) kmin++;
		  for(int k = kmin+1; k*p <= B; k++) merge(T, kmin*p, k*p);
	  }

	  set<int> Set;
	  for(int k = A; k <= B; k++) Set.insert(T[k]);

    cout << "Case #" << i << ": " << Set.size() << endl;
  }
}
