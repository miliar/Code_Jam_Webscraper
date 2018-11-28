#include <vector>
#include <cassert>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

int n, J[256], X;

double go(int i)	{
	double lo = 0., hi = 1.;
	FOR (it, 0, 1000)	{
		double mid = (lo + hi) / 2.;
		double me = mid * X + J[i];
		
		double totneed = mid;
		FOR (j, 0, n)	if (j != i)	{
			double need = max(0., (me - J[j]) / X);
			totneed += need;
		}
		if (totneed >= 1)	{
			hi = mid;
		}
		else	{
			lo = mid;
		}
	}
	return lo;
}

int main(void)	{
	int T;
	
	cin >> T;
	FOR (nc, 1, T+1) {
		cin >> n;
		X = 0;
		int nz = 0;
		FOR (i, 0, n)	{
			cin >> J[i];
			X += J[i];
		}
		cout << "Case #" << nc << ":";
		double tot = 0.;
		FOR (i, 0, n)	{
			double ans = go(i) * 100.;
			printf(" %0.6lf", ans);
			tot += ans;
		}
		//cout << endl << tot << endl;
		assert(fabs(tot - 100.)<=1e-6);
		cout << endl;
	}
}
