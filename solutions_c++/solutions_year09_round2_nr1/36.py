
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
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; }
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
#define maxn 20000
string tree;
int cas;
struct node {
	ld prob;
	string feature;
	int l, r;
};

node T[maxn];
int k = 0;
stringstream w;

void parseTree(int act) {
	T[act].l = T[act].r = -1;
	T[act].prob = -1;
	char c;
	w >> c;
//	debug(int(c));
//	debug(act);
//	debug(k);
//	debug(c);
	w >> T[act].prob;

	string part;
	w >> part;
//	debug(part);
//	debug(T[act].prob);
	if (part == "") while (1);
	if (part == ")") return ;
	T[act].feature = part;

	T[act].l = ++k;
	parseTree(k);
	T[act].r = ++k;	
	parseTree(k);

	w >> c;
}

int main(){
	cin >> cas;
	fup(c, 1, cas) {
		k = 0;
		int A, n;
		cin >> A;
		string line;
		getline(cin, line);
		tree = "";
		fup(i, 1, A) {
			getline(cin, line);
			tree += " " + line;
		}
		string z = tree;
		tree = "";
		fup(i, 0, siz(z) - 1) {
			char c = z[i];
			if (c == '(' || c == ')') {
				tree += " " + string(1, c) + " ";
			} else tree += string(1, c);
		}

		w.str(tree);
		//debug(w.str());
		cin >> n;
		k = 1;
		parseTree(1);
		printf("Case #%d:\n", c);
		fup(i, 1, n) {
			set<string> feat;
			string name; 
			int cech;
			cin >> name >> cech;
			fup(i, 1, cech) { string act; cin >> act; feat.insert(act); }
			ld p = 1;
			int act = 1;
			while (act != -1 ) {
				p *= T[act].prob;
				if (T[act].l == -1) break;
				if (feat.find(T[act].feature) != feat.end()) {
					act = T[act].l;
				} else act = T[act].r;
			}
			printf("%.8lf\n", p);
		}
	}

	return 0;	
}


