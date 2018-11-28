#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, A, N, L, P;
string line, tree;
int next[1000000][2];
double weight[1000000];
string feat[1000000];
set<string> features;

double read_weight() {
	string s;
	while (!isdigit(tree[P]) && tree[P] != '.') P++;
	while (isdigit(tree[P]) || tree[P] == '.') {
		s += tree[P];
		P++;
	}
	istringstream is(s);
	double res;
	is >> res;
	return res;
}

string read_feat() {
	string res;
	while (islower(tree[P])) {
		res += tree[P];
		P++;
	}
	return res;
}

void read_tree(int n) {
	while (tree[P] != '(') P++;
	P++;
	weight[n] = read_weight();
	while (tree[P] != ')' && !islower(tree[P])) P++;
	if (tree[P] == ')') {
		P++;
		next[n][0] = next[n][1] = -1;
		feat[n] = "";
	} else {
		feat[n] = read_feat();
		next[n][0] = N++;
		read_tree(N-1);
		next[n][1] = N++;
		read_tree(N-1);
		while (tree[P] != ')') P++;
		P++;
	}
}

void generate_tree() {
	N = 0, P = 0;
	read_tree(N++);
}

double calc() {
	int n = 0;
	double p = weight[0];
	while (feat[n] != "") {
		if (features.find(feat[n]) != features.end()) {
			n = next[n][0];
		} else {
			n = next[n][1];
		}
		p *= weight[n];
	}
	return p;
}

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> L;
		tree = "";
		getline(cin, line);
		FOR(i, 0, L) {
			getline(cin, line);
			tree += line;
		}
		generate_tree();
		cout << "Case #" << cs << ":" << endl;
		cin >> A;
		FOR(i, 0, A) {
			cin >> line;
			int n;
			cin >> n;
			features.clear();
			FOR(i, 0, n) {
				cin >> line;
				features.insert(line);
			}
			printf("%.7lf\n", calc());
		}
		FOR(i, 0, N) feat[i] = "";
	}
	return 0;
}
