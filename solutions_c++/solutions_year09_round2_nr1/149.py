#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>
#include <limits>
#include <iterator>
#include <sstream>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i != _b; ++i)
#define REP(i, N) FOR(i, 0, N)
#define REPK(K) REP(_crazyName, K)

#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()

template<typename CType, typename VType>
inline void REMOVE(CType &container, const VType &value) {
	container.erase(remove(ALL(container), value), container.end());
}

#define sz() size()
#define len() length()
#define mp(a, b) make_pair(a, b)
#define pb(x) push_back(x)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef long long LL;

struct Tree {
	double weight;
	string feature;
	Tree *left, *right;

	explicit Tree(double _weight = 0.0, string _feature = "", Tree *l = 0, Tree *r = 0) : weight(_weight), feature(_feature), left(l), right(r) { }
};

Tree *readTree(const string &desc, int &first) {
	double wt = 0;
	while (desc[first] == '(' || desc[first] == ' ')
		++first;
//)
	while (isdigit(desc[first])) {
		wt *= 10;
		wt += desc[first] - '0';
		++first;
	}
	if (desc[first] == '.') {
		++first;
		double p = 0.1;
		while (isdigit(desc[first])) {
			wt += (p * (desc[first] - '0'));
			p /= 10.0;
			++first;
		}
	}

	while (isspace(desc[first]))
		++first;

	Tree *root = new Tree(wt);
	if (desc[first] == ')') {
		++first;
		return root;
	}

	string feat = "";
	while (desc[first] != '(' && desc[first] != ')' && !isspace(desc[first])) {
		feat += desc[first];
		++first;
	}

	root->feature = feat;

	while (isspace(desc[first])) ++first;
	if (desc[first] == '(') {
		root->left = readTree(desc, first);
		++first;
		root->right = readTree(desc, first);
	}

	while (isspace(desc[first])) ++first;

	++first;

	return root;
}

void preorder(const Tree *root) {
	cout << "(" << root->feature << ", " << root->weight << ")" << endl;
	if (root->left) {
		cout << "LEFT" << endl;
		preorder(root->left);
	}
	if (root->right) {
		cout << "RIGHT " << endl;
		preorder(root->right);
	}
}

long double calc(const Tree *root, const set<string> &features) {
	long double prob = root->weight;
	const Tree *cur = root;

	while (cur && (cur->left || cur->right)) {
		if (!features.count(cur->feature))
			cur = cur->right;
		else
			cur = cur->left;
		if (cur)
			prob *= cur->weight;
	}

	return prob;
}

int main() {
	int T;
	cin >> T;

	REP (kase, T) {
		int L;
		cin >> L;

		string treeDesc = "";
		REP (i, L) {
			string temp;
			getline(cin, temp);
			if (temp.len() == 0) {
				--i;
				continue;
			}
			treeDesc += ' ';
			treeDesc += temp;
		}

// cout << "DESC: " << treeDesc << endl;
		int first = 0, last = 0;
		while (isspace(treeDesc[first])) ++first;

		Tree *root = readTree(treeDesc, first);

// preorder(root);

		int A;
		cin >> A;

		cout << "Case #" << (kase + 1) << ":" << endl;
		while (A--) {
			string animal;
			set<string> features;
			int K;

			cin >> animal >> K;
			REP (i, K) {
				string s;
				cin >> s;
				features.insert(s);
			}

			cout << fixed << setprecision(7) << calc(root, features) << endl;
		}
	}
}
