#include <iostream>
#include <sstream>
#include <string>
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

#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define pb push_back
#define sz(c) (int)c.size()
#define all(c) c.begin(),c.end()

#define mp make_pair
#define X first
#define Y second

typedef long int Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1000000000;
const double PI = acos(-1.0);

pair<pair<double, string>, PII> tree[100000];
int n;

int read_tree(){
	char c;
	cin >> c; // read '('
	string s;
	cin >> s;
	if (s[sz(s)-1] == ')'){
		s[sz(s)-1] = ' ';
		c = ')';
	}
	else
		cin >> c;
	sscanf(s.c_str(), "%lf", &tree[n].X.X);

	int nn=n;
	if (c!=')'){
		tree[n].X.Y = c;
		char cc;
		scanf("%c", &cc);
		while (cc >= 'a' && cc <= 'z'){
			tree[n].X.Y += cc;
			scanf("%c", &cc);
		}

		++n;
		tree[nn].Y.X = read_tree();
		tree[nn].Y.Y = read_tree();
		cin >> c;
	}
	else
		++n;
	return nn;
}


int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR(test, 0, T){
		cout << "Case #" << test+1 << ":\n";
		int t;
		scanf("%d\n", &t);
		FILL(tree, 0);
		n = 0;
		read_tree();
		int r;
		scanf("%d\n", &r);
		FOR(i, 0, r){
			string s;
			cin >> s;
			int m;
			cin >> m;
			set<string> st;
			FOR(i, 0, m){
				cin >> s;
				st.insert(s);
			}
			double p = 1;
			int node = 0;
			while (tree[node].X.Y != ""){
				p *= tree[node].X.X;
				if (st.find(tree[node].X.Y)!=st.end())
					node = tree[node].Y.X;
				else
					node = tree[node].Y.Y;
			}
			p *= tree[node].X.X;
			printf("%.7lf\n", p);
		}
	}
	return 0;
}