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

#define FOR(i,xx) for(int i=0, upTo##i=xx; i<upTo##i; ++i)
#define REVFOR(i,xx) for(int i=(xx)-1; i>=0; --i)
#define FOR2(i,b,xx) for(int i=b; i<(xx); ++i)
#define REVFOR2(i,b,xx) for(int i=(xx)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define RALL(C) (C).rbegin(), (C).rend()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

int N,K; 
int tab[100][25];

bool okk[100][100];

bool isOk(int t1[25], int t2[25]) {
	bool res = true;
	FOR(z,K) {
		if (t1[z] >= t2[z])
			res = false;
	}

	return res;
}

bool used[100];

int best;

map<vi, int> dp;

int findNext(vi &v, int left) {
	if (left == 0) return v.size();
	if (v.size() >= best) return v.size();

	vi v2(v.begin(), v.end());
	sort(ALL(v2));
	if (dp.find(v2) != dp.end()) return dp[v2];

	int res = N;
	FOR(i,N) {
		if (used[i]) continue;

		bool ok = true;			//najnizszego
		FOR(j,N) {
			if (used[j] || i==j) continue;
			if (okk[j][i]) {
				ok = false;
				break;
			}
		}

		bool added = false;
		if (ok) {
			used[i] = true;

			FOR(j,v.size()) {
				if (okk[v[j]][i]) {
					int tmp = v[j];
					v[j] = i;

					int x = findNext(v, left-1);
					if (x < res) res = x;
					v[j] = tmp;

					added = true;

					if (best <= v.size()) break;
				}
			}

			if (!added) {
				v.push_back(i);
				int x = findNext(v, left-1);
				if (x < res) res = x;
				v.pop_back();
			}

			used[i] = false;
		}

		if (best <= v.size()) break;
	}

	dp[v2] = res;

	return res;
}

int main(void) {
	int xx; cin>>xx;
	FOR(_i,xx) {

		cin>>N>>K;
		FOR(i,N) {
			FOR(j,K) {
				int x; cin >> x;
				tab[i][j] = x;
			}
		}

		FOR(i,N) used[i] = false;
		int64 res=0;

		FOR(i,N) FOR(j,N) okk[i][j] = isOk(tab[i], tab[j]);

		//wszystkich startowych
		vi vec;
		FOR(i,N) {
			bool ok = true;
			FOR(j,N) {
				if (i==j) continue;
				if (okk[j][i]) {
					ok = false;
					break;
				}
			}
			if (ok)
			{
				vec.push_back(i);
				used[i] = true;
			}
		}

		best = N;
		dp.clear();
		res = findNext(vec, N-vec.size());

		printf("Case #%d: %lld\n", _i+1, res);
	}
	return 0;
}
