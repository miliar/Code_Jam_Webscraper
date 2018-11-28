#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 
#define INT_INF 0x7FFFFFFF
// BEGIN CUT HERE
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }


int main() {
	int NC, K;
	scanf("%d",&NC);
	
	rep(i,NC) {
		scanf("%d", &K);
		
		char buf[1010];
		scanf("%s", buf);
		string s(buf);
		//cout << s << endl;
		
		rep(j,1010) {
			buf[j] = '\0';
		}
						
		int res = INT_INF;
		
		vi perm;
		rep(j,K) {
			perm.pb(j);
		}
		sort(all(perm));
		
		do {
			//int count = sz(s)/K;
			//cout << count << endl;
			rep(j, sz(s)) {
				buf[j] = s[ (j/K)*K + perm[j%K] ];
			}
			
			//printf("%s\n", buf);
			
			int poss = 0;
			char last = '\0';
			for (int j = 0; buf[j] != '\0'; j++) {
				if (buf[j] != last) {
					last = buf[j];
					poss++;
				}
			}
			
			res = min(res, poss);
		} while (next_permutation(all(perm)));
		
		printf("Case #%d: %d\n", i+1, res);
	}
}













