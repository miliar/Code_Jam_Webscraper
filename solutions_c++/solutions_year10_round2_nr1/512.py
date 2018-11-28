#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>

using namespace std;

const int INF = 1000000000;

typedef long long int64; 
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return int(c.size()); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }


typedef map<string, void *> dirs_tree;

vector<string> parse_address (string & address)
{
	vector<string> res;
	int pos = 1, ind;
	while ((ind = address.find('/', pos)) != -1) {
		res.push_back(address.substr(pos, ind - pos));
		pos = ind + 1;
	}

	if (pos < address.size())
		res.push_back(address.substr(pos));

	return res;
}

int add_address (vector<string> & parsed, dirs_tree * tree, int ind = 0)
{
	 if (parsed.size() == ind)
		 return 0;

	 int res = 0;
	 dirs_tree::iterator it = tree->find(parsed[ind]);
	 if (it == tree->end()) {
		res = 1;
		(*tree)[parsed[ind]] = new dirs_tree;
		it = tree->find(parsed[ind]);
	 }

	 res += add_address(parsed, (dirs_tree*)it->second, ind + 1);

	 return res;

}

void free_trees (dirs_tree * tree, bool is_root = true)
{
	for (dirs_tree::iterator it = tree->begin(); it != tree->end(); ++it) {
		free_trees((dirs_tree*) it->second, false);
	}

	if (!is_root)
		delete tree;


}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests_count;
	cin >> tests_count;

for (int test = 1; test <= tests_count; ++test) 
{
	fprintf(stderr, "Test: #%d\n", test);
	printf("Case #%d: ", test);

	dirs_tree root;
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n ; i++)
	{
		string path;
		cin >> path;
		vector<string> parsed = parse_address(path);
		add_address(parsed, &root);
	}

	int res = 0;
	for (int i = 0; i < m ; i++)
	{
		string path;
		cin >> path;
		vector<string> parsed = parse_address(path);
		res += add_address(parsed, &root);
	}

	free_trees(&root);


	printf("%d\n", res);
}

}