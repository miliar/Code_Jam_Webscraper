#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <utility>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <bitset>
#include <list>
#include <map>
#include <valarray>
#include <numeric>
#include <cmath>
#include <complex>
#include <ctime>
#include <cassert>
#include <exception>
#include <climits>
#include <limits>
//#include <hash_map>
//#include "regex.h"

#define foreach(container, iterator) for ((iterator) = (container).begin(); (iterator) != (container).end(); ++(iterator))
#define foreachr(container, riterator) for ((riterator) = (container).rbegin(); (riterator) != (container).rend(); ++(riterator))
#define ALL(container) (container).begin(), (container).end()
#define SQR(x) ((x) * (x))

#define SIZE(x) (sizeof(x) / sizeof((x)[0]))
#define CLEAR(x, pat) memset(x, pat, sizeof(x))

#define PB push_back 
#define MP std::make_pair

#define X first
#define Y second

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define REP(i, n) for ((i) = 0; (i) < (n); ++(i)) 
#define FOR(i, l, h) for ((i) = (l); (i) <= (h); ++(i)) 
#define FORD(i, h, l) for ((i) = (h); (i) >= (l); --(i)) 
#define PRESENT(container, element) ((container).find(element) != (container).end())
#define CPRESENT(container, element) (find(ALL(container), (element)) != (container).end())

const double eps = 1e-9;
inline bool eq(double x, double y) {
	return std::abs(x - y) < eps;
}

inline bool eq_rel(double p1, double p2) {
    return std::abs(p1 - p2) < eps * std::min(std::abs(p1), std::abs(p2));
}

typedef double real;
typedef unsigned long ulong;
typedef unsigned int uint;

typedef long long i64;
typedef unsigned long long u64;
const u64 MOD64 = 1000000007LL;

typedef std::vector<i64> VI64;
typedef std::vector<u64> VU64;

typedef std::vector<int> VI;
typedef std::vector<uint> VU;
typedef std::vector<real> VR;
typedef std::vector<std::string> VS;
typedef std::deque<bool> DB;
typedef std::pair<int, int> PII;
typedef std::pair<long, long> PLL;

#define FILE_NAME "A-small"

#ifdef FILE_NAME
	std::ifstream fin(FILE_NAME ".in");
	std::ofstream fout(FILE_NAME ".out");
#else
#define fin (std::cin)
#define fout (std::cout)
#endif

inline int Hash(const std::string &str) {
	int h = 0;
	const int mul = 3731;

	for (int i = 0; i < (int) str.length(); ++i)
		h = mul * h + str[i];

	return h;
}

struct TreeNode {
	double p;
	int hash;
	bool isLeaf;
	TreeNode *left, *right;

	TreeNode(const double _p, const int _h, const bool le) : p(_p), hash(_h), left(), right(), isLeaf(le) {}
};

int getted = 0;
std::stringstream *str = NULL;

inline std::string GetToken() {
	std::string res;
	int ch = 0;
	while (!str || ((ch = str->get()) != '(' || ch != ')')) {
		if (ch == ')' || ch == '(')
			return std::string() + char(ch);
		
		else if (str && *str) {
			str->unget();
			if (*str >> res)
				break;
		}

		std::getline(fin, res);
		if (str)
			delete str;
		str = new std::stringstream(res);
		++getted;
	}

	if (res[res.length() - 1] == ')' && res != ")") {
		delete str;
		std::string tmp = str->str();
		str = new std::stringstream(")" + tmp);
		return res.substr(0, res.size() - 1);
	}
	
	return res;
}

inline double Str2Double(const std::string str) {
	std::stringstream s(str);
	double res;
	s >> res;
	return res;
}

TreeNode *Parse() {
	TreeNode *node;
	std::string t = GetToken();
	assert(t[0] == '(');
	if (t == "(")
		t = GetToken();

	std::string name;
	if (t[t.length() - 1] == ')') {
		if (t[0] == '(')
			node = new TreeNode(Str2Double(t.substr(1, t.length() - 2)), 0, true);
		else
			node = new TreeNode(Str2Double(t.substr(0, t.length() - 1)), 0, true);

		return node;
	}

	name = GetToken();

	if (name[0] != ')') {
		node = new TreeNode(Str2Double(t.substr(1)), Hash(name), false);
		node->left = Parse();
		node->right = Parse();
		//)
		GetToken();
	} else {
		node = new TreeNode(Str2Double(t.substr(1)), 0, true);
	}

	return node;
}

TreeNode *root = NULL;

double Solve(const std::set<int> props, TreeNode *v, double p) {
	p *= v->p;

	if (!v->isLeaf) {
		if (props.find(v->hash) != props.end())
			return Solve(props, v->left, p);
		else
			return Solve(props, v->right, p);
	}
	
	return p;
}

int main(int argc, char *argv[]) {	
	assert(fin && fout);

	int testCnt;
	fin >> testCnt;

	for (int testIdx = 1; testIdx <= testCnt; ++testIdx) {
		int lines;
		fin >> lines >> std::skipws;

		getted = 0;
		std::string str;
		std::getline(fin, str);
		root = Parse();
		while (getted < lines)
			std::getline(fin, str);

		int a;
		fin >> a;
		fout << "Case #" << testIdx << ":\n";

		for (int i = 0; i < a; ++i) {
			std::string name;
			int n;
			fin >> name >> n;
			std::set<int> props;
			for (int j = 0; j < n; ++j) {
				std::string pr;
				fin >> pr;
				props.insert(Hash(pr));
			}

			fout << std::fixed << std::setprecision(7) << Solve(props, root, 1.L) << "\n";
		}
	}

#ifdef FILE_NAME
	fin.close();
	fout.close();
#endif

	return 0;
}
