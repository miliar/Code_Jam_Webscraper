#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

int _cl[128*128]; //empieza con todos en -1
tint cl(tint i) { return (_cl[i] == -1 ? i : _cl[i] = cl(_cl[i])); }
void join(tint i, tint j) { if(cl(i)!=cl(j)) _cl[cl(i)] = cl(j); }

char wa[] = "welcome to code jam";
char wb[512];
int la, lb;

int mem[32][512];
int din(int a, int b) {
	if (a < 0 || b < 0) return 0;
	if (b > lb) return 0;
	if (a == la && b <= lb) return 1;
	int &res = mem[a][b];
	if (res != -1) return res;
	res = din(a, b+1);
	if (wa[a] == wb[b]) res += din(a+1, b+1);
	res %= 1000;
	return res;
}


int main() {
	int tt;
	cin >> tt;
	string __; getline(cin, __);
	la = strlen(wa);

	forn(t, tt) {
		memset(mem, 0xff, sizeof(mem));
		fgets(wb, 512, stdin);
		lb = strlen(wb);
		int res = din(0, 0);
		printf("Case #%d: %.4d\n", t+1, res);
	}
	return 0;
}
