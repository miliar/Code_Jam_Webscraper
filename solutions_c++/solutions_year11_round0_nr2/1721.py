#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;

const double pi = acos(-1.0);
const int inf = numeric_limits<int>::max();

#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

string to_list(stack<char> l) {	
	vector<char> t; t.reserve(l.size());
	while(!l.empty()) {
		t.push_back(l.top());
		l.pop();
	}
	
	string s = "[";
	for(int i = t.size() - 1; i >= 0; i--) {
		s += t[i];
		s += (i ? ", " : "");
	}
	s += "]";
	
	return s;
}

string solve() {
	char C[256][256], D[256][256];
	vector<int> ex(256, 0);
	memset(C, 0, sizeof(C));
	memset(D, 0, sizeof(D));
	
	int c, d, n;
	
	cin >> c;
	for(int i = 0; i < c; i++) {
		char x, y, z; cin >> x >> y >> z;
		C[(int)x][(int)y] = C[(int)y][(int)x] = z;
	}
	
	cin >> d;
	for(int i = 0; i < d; i++) {
		char x, y; cin >> x >> y;
		D[(int)x][(int)y] = D[(int)y][(int)x] = 1;
	}
	
	stack<char> l;
	cin >> n;
	for(int i = 0; i < n; i++) {
		char x; cin >> x;
		
		if(l.size()) {
			char y = l.top();
			if(C[(int)x][(int)y]) {
				l.pop();
				ex[(int)y]--;
				l.push(C[(int)x][(int)y]);
				ex[C[(int)x][(int)y]]++;
			} else {
				l.push(x);
				ex[(int)x]++;
			}
		} else {
			l.push(x);
			ex[(int)x]++;
		}

		x = l.top();
		for(char z = 'A'; z <= 'Z'; z++)
			if(ex[(int)z] && D[(int)x][(int)z]) {
				l = stack<char>();
				ex.assign(256, 0);
				break;
			}
	}
	
	return to_list(l);
}

int main ( )
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T; cin >> T;
	for(int test = 1; test <= T; test++) {
		cout << "Case #" << test << ": " << solve() << endl;
	}
}