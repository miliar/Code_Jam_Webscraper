#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))
#define pch putchar
#define gch getchar()
#define FORD(i,a,b) for (int i=(a); i<=(b); i++)
#define FORP(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,n) for (int i=0; i<(n); i++)
#define clean(v) memset(v,0,sizeof(v))

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

template<typename T> T sqr(const T& c) {return c*c;} 

typedef long long ll;
typedef double lf;

ll d[501][501];
ll C[501][501];
ll ans[501];

const ll big = 100003;


int main() {
	int tests, n;
	
	clean(d); clean(C);
	
	C[0][0] = 1;
	FORD(i,1,500) {
		C[i][0] = 1;
		FORD(j,1,i) C[i][j] = (C[i-1][j-1] + C[i-1][j]) % big;
	}

	/*FORD(i,0,10) {
		FORD(j,0,i) cerr << C[i][j] << ' ';
		cerr << '\n';
	}*/

	
	d[1][0] = 1;// - ???
	//d[2][1] = 1;
	FORD(i,2,500) {//biggest number
		ans[i] = d[i][1] = 1;
		FORD(j,2,i-1) {//how many numbers are in subset
			d[i][j] = 0;
			FORD(k,1,j-1) {//how many numbers are less or equal than j
				d[i][j] += d[j][k]* C[i-j-1][j-k-1] % big;
				d[i][j] %= big;
			}
			ans[i] += d[i][j], ans[i] %= big;
		}                                     	
		
	}

	/*FORD(i,2,10) {
		FORD(j,1,i-1) cerr << d[i][j] << ' ';
		cerr << '\n';
	}*/

	//FORD(i,2,500) cerr << ans[i] << ' ';

	scanf("%d",&tests);
	FORD(curTest,1,tests) {
		scanf("%d",&n);
		printf("Case #%d: %I64d\n",curTest,ans[n]);
	}
}
