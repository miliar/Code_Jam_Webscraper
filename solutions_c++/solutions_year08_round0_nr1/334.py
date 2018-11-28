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
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second


int main(void)
{
	int n;
	cin >> n;
	FOR(i,n) {
		int s; cin >> s;
		map<string,int> engines;
		FOR(j,s) {
			string eng;
			do {
				getline(cin, eng);
			} while(eng.empty());
			engines[eng] = j;
		}
		int q; cin >> q;
		vs queries(q);
		FOR(j,q) {
			do {
				getline(cin, queries[j]);
			} while(queries[j].empty());
		}

		vector<bool> used(s);
		int left = s;
		int res = 0;
		FOR(j,q) {
			const string &que = queries[j];
			if (engines.count(que)) {
				int engNum = engines[que];
				if (used[engNum] == false) {
					if (--left == 0) {
						++res;
						used.assign(s, false);
						left = s - 1;
					}
					used[engNum] = true;
				}
			}
		}

		printf("Case #%d: %d\n", i+1, res);
	}

    return 0;
}
