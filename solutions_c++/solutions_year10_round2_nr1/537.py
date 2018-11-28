#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <sstream>
#include <bitset>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000+1;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b); x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for (VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

vector<map<string,int> > g;

char s[1000];

void go(int n) {
	REP(i,n) {
		gets(s);
		int curd=0;
		string left(s);
		left = left.substr(1,SIZE(left)-1);
		left += '/';
		while (SIZE(left)) {
			string newd=left.substr(0,left.find('/'));
//			cout << newd << endl;
		  	if (g[curd].find(newd) == g[curd].end()) {
				g[curd].insert(pair<string,int>(newd,SIZE(g)));
				g.PB(map<string,int>());
			}
//			cout << SIZE(newd) << ' ' << SIZE(left) << endl;
			left=left.substr(SIZE(newd)+1,SIZE(left)-SIZE(newd)-1);
//			cout << "H " << endl;
			curd = g[curd][newd];
		}
	}
}

void scase() {
	int n, m;
	scanf("%d%d\n",&n,&m);
	g=vector<map<string,int> >();
	g.PB(map<string,int>());
	go(n);
	int before=SIZE(g);
	go(m);
	int after=SIZE(g);
	printf("%d\n",after-before);
}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) {
		printf("Case #%d: ",i+1);
		scase();
	}

	return 0;
}
