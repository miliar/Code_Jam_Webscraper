#include <iostream>
#include <vector>
#include <string>
#include <memory.h>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <list>
#include <map>
#include <cmath>

#include <memory.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define FORE(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FIR(k) FOR(i,0,k)
#define FJR(k) FOR(j,0,k)
#define FI FIR(n)
#define FJ FJR(n)
#define ALL(v) v.begin(), v.end()
#define LL long long

typedef vector<int> VI;
typedef pair<int, int> PI;

int  p[100];

int main() {
static const string FILENAME = "A-large";
freopen((FILENAME + ".in").c_str(), "rt", stdin);
freopen((FILENAME + ".out").c_str(), "w", stdout);	
	
	int ncase; cin >> ncase;
	FORE(caze, 1, ncase) {
		int n;
		cin >> n;
		string s;
		FI {
			cin >> s;
			p[i+1] = 0;
			FJ if (s[j] == '1') p[i+1] = j + 1;
		}

		int res = 0;
		p[0] = 100;
		
		for (int i = 1; i <=n; ++i) {
			if (p[i] > i) {
				int j = i + 1;
				while (p[j] > i) ++j;
				while (j > i) {
					swap(p[j], p[j-1]);
					--j;
					++res;
				}
			}
		}
		
		

		printf("Case #%d: %d\n", caze, res);
	}

}