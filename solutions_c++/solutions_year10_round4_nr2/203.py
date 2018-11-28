#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;
string readLine();
int readIntLine();
vector<int> readVI(int n);
vector<string> readVS(int n);
vector<int> itokens(string s, string sep);
vector<string> stokens(string s, string sep);

class Tree {
public:
	Tree() { l = 0, r = 0, canMiss = 0, cost = 0; memo.resize(11, -1); }
	~Tree() { if (l) delete l; if (r) delete r; }
	Tree* l;
	Tree* r;
	int canMiss;
	int cost;
	vector<int> memo;

	void build(vector<int> &cm, vector<vector<int> > &costs, int i, int j) {
		cost = costs[i][j];
		l = new Tree;
		r = new Tree;
		if (i) {
			l->build(cm, costs, i-1, j*2);
			r->build(cm, costs, i-1, j*2+1);
		} else {
			l->canMiss = cm[j*2];
			r->canMiss = cm[j*2+1];
			for (int i = 0; i < 11; i++) l->memo[i] = r->memo[i] = 0;
		}
		canMiss = l->canMiss;
		if (r->canMiss < canMiss) canMiss = r->canMiss;

		for (int x = 0; x < canMiss-i; x++) {
			memo[x] = 0;
		}
		int sx = i > canMiss ? 0 : canMiss-i;
		for (int x = sx; x <= canMiss; x++) {
			memo[x] = cost + l->minCost(x) + r->minCost(x);
			if (l->canMiss >= x+1 && r->canMiss >= x+1) {
				int c2 = l->minCost(x+1) + r->minCost(x+1);
				if (c2 < memo[x]) memo[x] = c2;
			}
		}
	}
	void print(int depth) {
		for (int i = 0; i < depth; i++) printf(" ");
		printf("%2d %4d\n", canMiss, cost);
		if (l) { l->print(depth+1); r->print(depth+1); }
	}
	int minCost(int missed) { return memo[missed]; }
};


int solveIt(int P, vector<int> &cm, vector<vector<int> > &costs) {
	Tree *root = new Tree;
	root->build(cm, costs, P-1, 0);
	if (dbg > 1) root->print(0);
	int res = root->minCost(0);
	delete root;
	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int P;
		scanf("%d ", &P);
		vector<int> cm = readVI(1<<P);
		vector<vector<int> > costs(P);
		for (int i = 0; i < P; i++) costs[i] = readVI(1<<(P-i-1));

		long long res = solveIt(P, cm, costs);
		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}








string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}
int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}
vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep = " \n\r\t") {
	vector<string> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

