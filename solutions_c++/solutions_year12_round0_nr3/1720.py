#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<ctime>	// srand( time(NULL) )
#include<iostream>
#include<iomanip>
#include<sstream>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<utility>
#include<algorithm>
#include<map>
#include<set>
#include<bitset>

using namespace std;

// Typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair< int, pair<int, int> > iii;
typedef vector<iii> viii;
typedef vector< vector<int> > vvi;
typedef vector< vector<ii> > vvii;
typedef vector< vector<iii> > vviii;

// Macros
#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, a) for(int i = 0; i < a; ++i)
#define FORE(i, a, b) for(int i = a; i >= b; --i)
#define all(v) v.begin(), v.end()
#define sz(A) int((A).size())
#define pb push_back
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define LSOne(S) (S & (-S)) // bit menos significativo
#define first(x) x.first	// lidam com triplas
#define second(x) x.second.first
#define third(x) x.second.second

// Constantes
const double PI = 2*asin(1.0);
const int INF = 1000000000;	// 9 zeros
const double EPS = 1e-10;

// Matematica basica
inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
inline ll gcd(ll n1, ll n2) {return n2==0? abs(n1) : gcd(n2,n1%n2);}
inline ll lcm(ll n1, ll n2) {return n1==0||n2==0? 0 : abs(n1*(n2/gcd(n1,n2)));}

int a, b;

int d(int n) {
	if(n <= 9) return 1;
	int res = 0;
	while(n > 0) {
		n /= 10;
		res++;
	}
	return res;
}

int mypow(int n, int p) {
	int res = 1;
	FORR(i, p) res *= n;
	return res;
}

ll go() {
	ll res = 0;
	FOR(i, a, b+1) {
		int n = i;
		int power = mypow(10, d(i)-1);
		ll cnt = 0LL;
		do {
			int aux = n%10;
			n /= 10;
			n = aux*power+n;

			if(aux != 0 && n > i && n <= b) {
				cnt++;
//				printf("[%d, %d] => (%d, %d)\n", a, b, i, n);
			}
		} while(n != i);
		res += cnt;
	}
	return res;
}

int main() {
	int tests = 0;
	cin >> tests;

	FORR(caseNum, tests) {
		cin >> a >> b;
		
		printf("Case #%d: %lld\n", caseNum+1, go());
	}

	return 0;
}
