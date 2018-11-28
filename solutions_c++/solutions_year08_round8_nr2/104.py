#pragma warning (disable:4786) 
#pragma warning (disable:4996) 
#include <time.h>
#include <algorithm> 
#include <iostream>  
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <stack>
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <cassert>
using namespace std;

#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))
#define FILL(a,b) memset(a, (b), sizeof(a));
typedef long long ll; 
const double EPS = 1e-7;
const int INF = 0x7fffffff;

const int LAST = 10000 - 1;
const string ATTEMPT = "0";
const string TASK = "B";
const string TYPE = "large";
//const string TYPE = "large";
void openfiles() {
	string infile;
	if (TYPE == "large")
		infile = TASK + "-large.in";
	else
		infile = TASK + "-" + TYPE.c_str() + "-attempt" + ATTEMPT.c_str() + ".in";
	freopen(infile.c_str(),"rt",stdin);
	//freopen("test.in","rt",stdin);
	freopen("test.out","wt",stdout);
}

struct Order {
	int c, a, b;
};

bool operator< (const Order& a, const Order& b) {
	return a.a < b.a;
}

vector<Order> orders;

bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
	int aa = a.second == 0 ? orders[a.first].a : orders[a.first].b;
	int bb = b.second == 0 ? orders[b.first].a : orders[b.first].b;
	return aa < bb;
}

void solve() {
	int n;
	scanf("%d ",&n);
	map<string, int> mp;
	int m = 0;
	orders.clear();
	REP(i,n) {
		string c;
		Order O;
		cin >> c >> O.a >> O.b;
		O.a--; O.b--;
		if (mp.find(c) == mp.end()) {
			mp[c] = m++;
		}
		O.c = mp[c];
		orders.push_back(O);
	}
	sort(orders.begin(), orders.end());
	//typedef pair<int, int> pii;
	//vector<pii> v;
	//REP(i,n) {
	//	v.push_back(pii(i, 0));
	//	v.push_back(pii(i, 1));
	//}
	//sort(v.begin(), v.end(), cmp);

	//cout << m << endl;
	int best = INF;
	REP(i,m) FOR(j,i,m) FOR(k,j,m) {
		//cout << i << " " << j << " " << k << endl;
		int end = -1;
		int cnt = 0;
		int ii = 0;
		do {
			cnt++;
			// skip
			int bestnext = -1;
			for (; ii < orders.size() && orders[ii].a <= end + 1; ii++) {
				int cc = orders[ii].c;
				if (cc == i || cc == j || cc == k) {
					if (orders[ii].b > bestnext) {
						bestnext = orders[ii].b;
					}
				}
			}
			// we must advance by at least one
			if (bestnext <= end) {
				break;
			}
			end = bestnext;
		} while (ii < orders.size() && end < LAST);
		if (end == LAST)
			best = min(best, cnt);
	}
	static int test = 0;
	if (best != INF)
		printf("Case #%d: %d\n",++test,best);
	else
		printf("Case #%d: %s\n",++test,"IMPOSSIBLE");
}

int main() {
	openfiles();
	int n;
	scanf("%d ",&n);
	REP(i,n) solve();

	return 0;
}