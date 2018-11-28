#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

string fileName = "C-large";

bool used[2222222];
void solveSingle(int testNumber) {
	int a, b;
	scanf("%d%d", &a, &b);
	int res = 0, x;
	vector<int> v;
	string s, t;
	for (int i = a; i <= b; i++) {
		s = tostring(i);
		v.clear();
		for (int j = 1; j < s.size(); j++) {
			t = s.substr(j) + s.substr(0, j);
			if (t[0] == '0') continue;
			x = toint(t);
			if (x > i && x <= b && used[x] == false) {
				v.pb(x);
				used[x] = true;
			}
		}
		res += v.size();
		for (int j = 0; j < v.size(); j++)
			used[v[j]] = false;
	}
	printf("Case #%d: %d\n", testNumber, res);
	fflush(stdout);
}

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
	}
	return 0;
}
