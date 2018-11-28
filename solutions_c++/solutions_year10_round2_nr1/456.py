#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long Int;

#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define all(c) c.begin(), c.end()
#define sz(c) (int)c.size()
#define pb push_back

#define mp make_pair
#define X first
#define Y second

const double PI = acos(-1.0);
const int INF = 1000000000;

PII operator+(const PII & a, const PII & b){return PII(a.X+b.X, a.Y+b.Y);}
PII operator-(const PII & a, const PII & b){return PII(a.X-b.X, a.Y-b.Y);}
int dot_p(const PII & a, const PII & b){return a.X*b.X + a.Y*b.Y;}
int cross_p(const PII & a, const PII & b){return a.X*b.Y - a.Y*b.X;}

int to_int(string s){
	if (s == "")
		return 0;
	istringstream iss(s);
	int n;
	iss >> n;
	return n;
}

string to_str(int n){
	ostringstream oss;
	oss << n;
	return oss.str();
}


int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		set<string> se;
		FOR(i, 0, n)
		{
			string ss;
			cin >> ss;
			se.insert(ss);
		}
		int old_s = sz(se);
		FOR(i, 0, m)
		{
			string ss;
			cin >> ss;
			string sh;
			sh += ss[0];
			FOR(i, 1, sz(ss))
			{
				if (ss[i] == '/')
					se.insert(sh);
				sh += ss[i];
			}
			se.insert(sh);
		}
		printf("Case #%d: %d", t+1, sz(se)-old_s);		
		if (t != T-1)
			printf("\n");
	}

	return 0;
}