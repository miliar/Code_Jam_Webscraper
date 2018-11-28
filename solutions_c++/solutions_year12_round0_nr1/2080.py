/*
 TASK:A
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

#define SMALL
//#define LARGE
int T;
char m[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
		'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
string line;
int main() {

	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	cin >> T;
	getline(cin, line);
	rep(tt,T) {
		printf("Case #%d: ", tt + 1);
		getline(cin, line);
		for (int i = 0; i < line.size(); ++i) {
			if (isalpha(line[i])) {
				cout << m[line[i] - 'a'];
			} else
				cout << line[i];
		}
		cout << endl;
		cerr << tt << endl;
	}
	return 0;
}
//end

