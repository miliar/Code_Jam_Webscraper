#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

const int N = 100000;

map<string, int> id;
map<int, string> fromId;
int n;

double weight[N];
vector<vector<int> > children;

double eval(int root, double p, const vector<bool> has) {
	p *= weight[root];
	if (children[root].empty())
		return p;
	for (int i = 0; i < children[root].size(); i++) {		
		if (has[children[root][i]])
			return eval(children[root][i], p, has);
		else
			return eval(children[root][i + 1], p, has);
	}	
	assert(false);
}


istringstream iss;
string input;
void parse(int root) {
	char c;
	iss >> c;
	assert(c == '(');
	string s;
	iss >> s;
	sscanf(s.c_str(), "%lf", &weight[root]);	
	iss >> s;	
	if (s[0] == ')')
		return;
	if (id.find(s) == id.end()) {
		id[s] = n;
		fromId[n] = s;
	}
	children[root].pb(n);	
	parse(n++);
	children[root].pb(n);
	parse(n++);
	iss >> c;
	assert(c == ')');
}

void solve() {
	n = 1;
	id.clear();
	fromId.clear();
	children.assign(N, vector<int>());

	int L;
	scanf("%d", &L);
	getchar();
	input = "";
	for (int i = 0; i < L; i++) {
		char buf[512];
		gets(buf);
		input += string(buf);
	}	
	string z = input;
	input = "";
	for (int i = 0; i < z.size(); i++)
		if (z[i] == '(')
			input += " ( ";
		else if (z[i] == ')')
			input += " ) ";
		else
			input += z[i];
	
	

	iss.str(input);	
	parse(0);	
	int A;
	scanf("%d", &A);
	for (int i = 0; i < A; i++) {
		int nFeatures;
		char buf[1024];		
		scanf("%s", buf);
		scanf("%d", &nFeatures);
		vector<bool> has(N);
		for (int j = 0; j < nFeatures; j++) {
			scanf("%s", buf);
			if (id.find(buf) != id.end())
				has[id[buf]] = true;
		}
		printf("%.15lf\n", eval(0, 1, has));
	}
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	getchar();
	for (int T = 1; T <= nTests; T++) {
		printf("Case #%d:\n", T);
		solve();
	}
	fclose(stdin); fclose(stdout);
	return 0;
}
