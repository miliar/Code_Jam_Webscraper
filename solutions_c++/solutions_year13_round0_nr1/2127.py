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
#include<climits>

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
#define CLR(x, a) memset(x, a, sizeof(x))

// Constantes
const double PI = 2*asin(1.0);
const int INF = 1000000000;	// 9 zeros
const double EPS = 1e-10;

// Matematica basica
inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }
inline ll gcd(ll n1, ll n2) {return n2==0? abs(n1) : gcd(n2,n1%n2);}	// MUDAR PARA O PKU!
inline ll lcm(ll n1, ll n2) {return n1==0||n2==0? 0 : abs(n1*(n2/gcd(n1,n2)));}	// MUDAR PARA O PKU!

vector<string> tab;

bool diagonal1 (char token) {
	FORR (i, 4)	if (tab[i][i]!='T'&&tab[i][i]!=token) return false;
	return true;
}

bool diagonal2 (char token) {
	FORR (i, 4)	if (tab[i][3-i]!='T'&&tab[i][3-i]!=token) return false;
	return true;
}

bool horizontal (int pos, char token) {
	FORR (i, 4)	if (tab[pos][i]!='T'&&tab[pos][i]!=token) return false;
	return true;
}

bool vertical (int pos, char token) {
	FORR (i, 4)	if (tab[i][pos]!='T'&&tab[i][pos]!=token) return false;
	return true;
}

bool test (char token){
	FORR (i, 4) if (vertical (i, token)) return true;
	FORR (i, 4) if (horizontal (i, token)) return true;
	if (diagonal1 (token)) return true;
	if (diagonal2 (token)) return true;
	return false;
}

bool has_dot (){
	FORR (i, 4) FORR (j, 4) if (tab[i][j]=='.') return true;
	return false;
}

int main() {
	int T;
	cin>>T;
	FORR (k, T){
		string str;
		tab.clear();
		FORR (i, 4){
			cin>>str;
			tab.pb(str);
		}
		cout << "Case #" << (k+1) << ": ";
		if (test('X')){
			cout << "X won" << endl;
		} else if (test('O')) {
			cout << "O won" << endl;
		} else if (has_dot()) {
			cout << "Game has not completed" << endl;
		} else {
			cout << "Draw" << endl;
		}
	}
}
