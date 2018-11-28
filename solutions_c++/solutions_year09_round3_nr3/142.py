#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

vector<int> tab;
map<pI, int> dp;

int find(int first, int last, int beg, int end) {
	if (end<=beg) return 0;

	if (dp.count(pI(first,last)))
		return dp[pI(first,last)];

	int res = last - first;
	int best = INT_MAX;
	for(int i=beg; i<end; ++i)
	{
		int x = res + find(first, tab[i]-1, beg, i) + find(tab[i]+1, last, i+1, end);
		if (x < best)
			best = x;
	}

	dp[pI(first,last)] = best;

	return best;
}

int main(void) {
    int n; cin>>n;
    FOR(_i,n) {
		int p,q;
		cin>>p>>q;
		tab.clear();
		dp.clear();
		FOR(i,q) {
			int x; cin >> x;
			tab.push_back(x);
		}

		int res = find(1,p,0,tab.size());

        printf("Case #%d: %d\n", _i+1, res);
    }
    return 0;
}
