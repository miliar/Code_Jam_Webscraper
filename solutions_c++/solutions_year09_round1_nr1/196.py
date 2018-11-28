#include  <cstdio>
#include  <cstdlib>
#include  <string>
#include  <cmath>
#include  <inttypes.h>
#include  <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

#define tr(it,s) for(typeof(s.begin())it=s.begin();it!=s.end();++it)
#define rep(i,n) for(int i=0; i<n; ++i)

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }
  
const long TAM = 10000000;

long H[TAM][11];

long findH(long k, long b) {
	if (H[k][b] >= 0) return H[k][b];
	if (H[k][b] == -2) return 0;
	H[k][b] = -2;
	int k1 = k;
	int kn = 0;
	while (k1 > 0) {
		kn += (k1%b)*(k1%b);
		k1 /= b;
	}
	H[k][b] = findH(kn,b);
	return H[k][b];
}

int ans[1<<9];

main() {
	
	rep(i,11) {
		rep(j,TAM) H[j][i] = -1;
		H[0][i] = 0;
		H[1][i] = 1;
	}
	for(int i = 2; i<= 10; ++i) rep(j,TAM) findH(j,i);
	
	rep(p, 1<<9) ans[p] = -1;
	
	for(int j = 2; j < TAM; ++j) {
		int p = 0;
		for(int i = 2; i <= 10; ++i) if (H[j][i] == 1) p+= 1<<(i-2);
		
		int p1 = p;
		while (p1 > 0) {
			if (ans[p1] == -1) ans[p1] = j;
			p1 = (p1 - 1) & p;
		}
	}
	
	//cout << "int ans[] = {";
	//rep(p,1<<9) cout << ans[p] << ", ";
	//cout << endl << endl;
	
	int T;
	cin >> T;
	string line;
	getline(cin, line);
	rep(t,T) {
		getline(cin, line);
		istringstream ss(line);
		int b, p;
		p = 0;
		while (ss >> b) {
			//cout << "b = " << b << endl;
			p += 1<<(b-2);
		}
		printf("Case #%d: %d\n", t+1, ans[p]);
	}
	
	
	
}
	
	
