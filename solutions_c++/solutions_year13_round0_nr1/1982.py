#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>

#include <ctime>
#include <deque>
#include <bitset>
#include <cctype>
#include <utility>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long ull;

#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define Repd(i,n) for(int i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(int i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(int i = (a); i >= (b); --i)
#define Fit(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); ++i)
#define Fitd(i,v) for(__typeof((v).rbegin()) i = (v).rbegin(); i != (v).rend(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))

template<class F, class T> T convert(F a, int p = -1) { stringstream ss; if (p >= 0) ss << fixed << setprecision(p); ss << a; T r; ss >> r; return r; }
template<class T> T gcd(T a, T b) { T r; while (b != 0) { r = a % b; a = b; b = r; } return a; }
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> T sqr(T x) { return x * x; }
template<class T> T cube(T x) { return x * x * x; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return s == 0 ? 0 : cntbit(s >> 1) + (s & 1); }
const int bfsz = 1 << 16; char bf[bfsz + 5]; int rsz = 0;int ptr = 0;
char gc() { if (rsz <= 0) { ptr = 0; rsz = (int) fread(bf, 1, bfsz, stdin); if (rsz <= 0) return EOF; } --rsz; return bf[ptr++]; }
void ga(char &c) { c = EOF; while (!isalpha(c)) c = gc(); }
int gs(char s[]) { int l = 0; char c = gc(); while (isspace(c)) c = gc(); while (c != EOF && !isspace(c)) { s[l++] = c; c = gc(); } s[l] = '\0'; return l; }
template<class T> bool gi(T &v) {
    v = 0; char c = gc(); while (c != EOF && c != '-' && !isdigit(c)) c = gc(); if (c == EOF) return false; bool neg = c == '-'; if (neg) c = gc();
    while (isdigit(c)) { v = v * 10 + c - '0'; c = gc(); } if (neg) v = -v; return true;
}

#define maxn 500005

int test;
string s[4];

int calrow(int id){
	int a[3]; ms(a, 0);
	Rep(i, 4) {
		if(s[id][i] == 'X') a[1]++;
		if(s[id][i] == 'O') a[2]++;
		if(s[id][i] == 'T') a[0]++;
	}

	if(a[1] == 4 || (a[1] == 3 && a[0] == 1)) return 1;
	if(a[2] == 4 || (a[2] == 3 && a[0] == 1)) return 2;
	return 0;

}

int calcol(int id){
	int a[3]; ms(a, 0);
	Rep(i, 4) {
		if(s[i][id] == 'X') a[1]++;
		if(s[i][id] == 'O') a[2]++;
		if(s[i][id] == 'T') a[0]++;
	}

	if(a[1] == 4 || (a[1] == 3 && a[0] == 1)) return 1;
	if(a[2] == 4 || (a[2] == 3 && a[0] == 1)) return 2;
	return 0;
}

int caldia(){
	int a[3]; ms(a, 0);
	Rep(i, 4) {
		if(s[i][i] == 'X') a[1]++;
		if(s[i][i] == 'O') a[2]++;
		if(s[i][i] == 'T') a[0]++;
	}
	if(a[1] == 4 || (a[1] == 3 && a[0] == 1)) return 1;
	if(a[2] == 4 || (a[2] == 3 && a[0] == 1)) return 2;
	ms(a, 0);
	Rep(i, 4) {
		if(s[i][3 - i] == 'X') a[1]++;
		if(s[i][3 - i] == 'O') a[2]++;
		if(s[i][3 - i] == 'T') a[0]++;
	}
	if(a[1] == 4 || (a[1] == 3 && a[0] == 1)) return 1;
	if(a[2] == 4 || (a[2] == 3 && a[0] == 1)) return 2;
	return 0;
}

bool fill(){
	Rep(i, 4) Rep(j, 4) if(s[i][j] == '.') return false;
	return true;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> test;
	For(itest, 1, test){
		Rep(i, 4) cin >> s[i];
		int res = 0;
		Rep(i, 4) if(calrow(i)){
			res = calrow(i);
			break;
		}
		if(!res){
			Rep(i, 4) if(calcol(i)){
				res = calcol(i);
				break;
			}
		}
		if(!res){
			res = caldia();
		}
		cout << "Case #" << itest << ": ";
		if(res == 1){
			cout << "X won" << endl;
		}
		else if(res == 2){
			cout << "O won" << endl;
		}
		else if(!fill()){
			cout << "Game has not completed" << endl;
		}
		else cout << "Draw" << endl;
	}

	return 0;
}
