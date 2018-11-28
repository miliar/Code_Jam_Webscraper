/*
 * A.cpp
 *
 *  Created on: May 8, 2010
 *      Author: Hamzawy
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
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
using namespace std;
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
const long double PI = (2.0 * acos(0.0));

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	//freopen("1.in", "rt", stdin);
	freopen("1.txt", "wt", stdout);
#endif
	int XXXXXXXX = clock();

	int n, x, y;
	scanf("%d", &n);
	rep(i,n) {
		scanf("%d%d", &x, &y);
		if ((y & ((1 << x) - 1)) == ((1 << x) - 1))
			printf("Case #%d: ON\n", i + 1);
		else
			printf("Case #%d: OFF\n", i + 1);
	}

	return 0;
}
