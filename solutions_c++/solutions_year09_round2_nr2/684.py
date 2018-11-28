#include <vector>
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
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-9;

int a, b;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
	int T;
	cin >> T;
	for1(Q, T){
		printf("Case #%d: ", Q);
		string s;
		cin >> s;
		bool last = true;
		int minV = INF;
		fore(i, 1, sz(s)){
			if(s[i] - '0' > s[i - 1] - '0'){
				last = false;
				break;
			}
			if(s[i] != '0') minV = min(minV, s[i] - '0');
		}
		minV = min(minV, s[0] - '0');
		if(last){
			string ans;
			ans += char(minV + '0');
			sort(all(s));
			s.erase(s.find(ans), 1);
			ans += '0';
			ans += s;
			cout << ans << endl;
		}else{
			string ans = s;
			while(next_permutation(all(ans))){
				if(ans[0] != '0' && ans > s){
					cout << ans << endl;
					break;
				}
			}
		}
	}
    return 0;
}
