#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define FORD(i,a,b) for (int i = (int)(a)-1; i >= (int)(b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,a) FORD(i,a,0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-12;
const int INF = 1000000000;

int tc, n, yk1, yk2, r;
string s;
vector<pair<string,int> > q;
vector<int> a, b;
int t1[10000], t2[10000];

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> n;
		a.clear();
		b.clear();
		q.clear();
		REP(i,n){
			cin >> s >> r;
			q.PB(MP(s,r));
			if (s=="O") a.PB(r);
			else b.PB(r);
		};
		if (a.size()) t1[0] = 1+abs(1-a[0]);
		if (b.size()) t2[0] = 1+abs(1-b[0]);
		for (int i = 1; i < a.size(); ++i) t1[i] = 1+abs(a[i]-a[i-1]);
		for (int i = 1; i < b.size(); ++i) t2[i] = 1+abs(b[i]-b[i-1]);
		int l1 = 0, l2 = 0;
		yk1 = yk2 = 0;
		REP(i,n) if (q[i].first=="O"){
			l1 += t1[yk1++];
			if (l1 <= l2) l1 = l2+1;
		}else{
			l2 += t2[yk2++];
			if (l2 <= l1) l2 = l1+1;
		};
		printf ("Case #%d: %d\n", ic+1, max(l1,l2));
	};
	return 0;
};