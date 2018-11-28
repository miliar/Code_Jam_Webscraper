
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

struct node {
	map<string, int> mapa;
};

int jest;
node T[1000000];

vector<string> parse(string x) {
	fup(i, 0, siz(x) - 1) if (x[i] == '/') x[i] = ' ' ;
	vector<string> odp;
	stringstream w(x);
	string a;
	while (w >> a) {
		odp.PB(a);
	}
	return odp;
}
int root;

int getNode() {
	++jest;
	T[jest].mapa.clear();
	return jest;
}
int dodaj(vector<string> x) {
	int sum = 0;
	int act = root;
	FORE(it, x) {
		string name = *it;
		if (T[act].mapa.find(name) != T[act].mapa.end()) {
			act = T[act].mapa[name];
		} else {
			int x = getNode();
			T[act].mapa[name] = x;
			act = x;
			sum++;
		}
	}
	return sum;
}

int main() {
	int cas;
	cin >> cas;
	int c = 0;
	while (cas--) {
		++c;
		int n, m;
		cin >> n >> m;
		jest = 0;
		root = getNode();
		int sum = 0;
		fup(i, 1, n) {
			string x;
			cin >> x;
			vector<string> y = parse(x);
			dodaj(y);
		}

		fup(i, 1, m) {
			string x;
			cin >> x;
			vector<string> y = parse(x);
			int s = dodaj(y);
			sum += s;

		}

		printf("Case #%d: %d\n", c, sum);


	}
	return 0;
}


