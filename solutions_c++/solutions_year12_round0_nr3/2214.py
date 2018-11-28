/*
 TASK:C
 LANG:C++
 Muhammad Magdi Muhammad
 Email: moh_magdi@acm.org
 */
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back
#define OO ((int)1e9)
#define MAX 100000

typedef long long ll;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
int I, J;
inline bool valid(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

using namespace std;

//#define SMALL
#define LARGE
int T;
char x[10];

int main() {

	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
#endif

	cin >> T;
	rep(tt,T) {
		set<pair<int, int> > cnt;
		printf("Case #%d: ", tt + 1);
		int a, b;
		cin >> a >> b;
		REP(num,a,b+1) {
			sprintf(x, "%d", num);
			int n = strlen(x);
			string xx = x, first, par;
			int y;
			REP(i,1,n) {
				par = xx.substr(0, i);
				first = xx.substr(i);
				first += par;
				sscanf(first.c_str(), "%d", &y);
				if (y >= a && y <= b && y < num) {
					cnt.insert(mp(y, num));
				}
			}
		}
		printf("%d\n", cnt.size());
		cerr << tt << endl;
	}
	return 0;
}
//end

