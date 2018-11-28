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
	
	string cm;
	for (int t = 1; t <= tc; ++t) {
		int n, num;
		cin >> n;
		
		vector<int> o, b, ord;
		
		for (int i = 0; i < n; ++i) {
			cin >> cm >> num;
			
			if (cm == "O") o.pb(num);
			else b.pb(num);
			
			ord.pb(cm == "O");
		}
		
		int poso = 1, posb = 1;
		int indo = 0, indb = 0;
		
		int moves = 0;
		for (int i = 0; i < n; ++i) {
			if (ord[i]) {
				int add = o[indo] - poso;
				
				if (indb < b.size()) {
					if (b[indb] < posb) posb -= min(abs(add) + 1, posb - b[indb]);
					else if (b[indb] > posb) posb += min(abs(add) + 1, b[indb] - posb);
				}
				
				moves += abs(add) + 1;
				poso += add;
				
				indo++;
			}
			else {
				int add = b[indb] - posb;
				
				if (indo < o.size()) {
					if (o[indo] < poso) poso -= min(abs(add) + 1, poso - o[indo]);
					else if (o[indo] > poso) poso += min(abs(add) + 1, o[indo] - poso);
				}
				
				moves += abs(add) + 1;
				posb += add;
				
				indb++;
			}
		}
		
		cout << "Case #" << t << ": " << moves << '\n';
	}
	
	
	return 0;
}




























