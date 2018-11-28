/*    muriloadriano @ topcoder
 *    muriloufg @ codeforces
 */
#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <deque>
#include <ctime>
#include <cfloat>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <climits>
#include <sstream>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back
#define ff first
#define ss second
#define ti(x) typeof(x.begin())
#define all(x) x.begin, x.end()
#define fill(x, y) memset(x, y, sizeof(x)) 

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int INF = 0x3f3f3f3f;
const double EPS = 1e-5;

template <typename T> T abs(const T& a) { if (a >= 0) return a; return -a; }


int main()
{
	ios::sync_with_stdio(false);
	int tc;
	cin >> tc;
	
	string str;
	for (int t = 1; t <= tc; ++t) {
		int comb, op, sz;
		
		map<char, map<char, char> > C;
		map<char, set<char> > O;
		
		cin >> comb;
		for (int i = 0; i < comb; ++i) {
			cin >> str;
			C[str[0]][str[1]] = str[2];
			C[str[1]][str[0]] = str[2];
		}
		
		cin >> op;
		for (int i = 0; i < op; ++i) {
			cin >> str;
			O[str[0]].insert(str[1]);
			O[str[1]].insert(str[0]);
		}
		
		cin >> sz >> str;
		
		vector<char> q;
		
		q.pb(str[0]);
		int qpos = 1;
		for (int i = 1; i < sz; ++i) {
			if (qpos && C[q[qpos-1]].find(str[i]) != C[q[qpos-1]].end()) {
				q[qpos-1] = C[q[qpos-1]][str[i]];
			}
			else {
				bool flag = true;
				for (int j = qpos-1; j >= 0; --j) {
					if (O[q[j]].find(str[i]) != O[q[j]].end()) {
						q.clear();
						flag = false;
						qpos = 0;
						break;
					}
				}
				
				if (flag) { q.pb(str[i]); qpos++; }
			} 
		}
		
		cout << "Case #" << t << ": ["; if (q.empty()) cout << "]\n"; else cout << q[0];
		
		sz = q.size();
		for (int i = 1; i < sz; ++i) cout << ", " << q[i];
		
		if (sz) cout << "]\n"; 
		
	}
	
	
	return 0;
}




























