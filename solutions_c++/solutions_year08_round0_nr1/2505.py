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
	int N, S, Q;
	char buf[200];
	map< string, deque<int> > times;
	
	scanf("%d", &N);
	
	rep(i,N) {
		int res = 0;
		string disc;
		
		times.clear();
		scanf("%d", &S);
		getline(cin, disc);
		
		rep(j,S) {
			string name;
			getline(cin, name);
			times[name] = deque<int>();
		}
		
		scanf("%d", &Q);
		getline(cin, disc);
		
		rep(j,Q) {
			string name;
			getline(cin, name);
			times[name].pb(j);
		}
		
		string last = "//////";
		while(1) {
			int max = -1;
			string loclast; 
			bool brk = false;
			
			foreach(it, times) {
				if (it->first != last) {
					if ((it->second).empty()) {
						brk = true;
						break;
					}
					
					if ((it->second).front() > max) {
						loclast = it->first;
						max = (it->second).front();
					}
				}
			}
			last = loclast;
			
			if (brk) break;
			res++;
			
			foreach(it, times) {
				while (!(it->second).empty() && (it->second).front() <= max) (it->second).pop_front();
			}
		}
		
		printf("Case #%d: %d\n", i+1, res);
	}
}








