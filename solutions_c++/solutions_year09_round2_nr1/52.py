/* small-A.cc
 */
#include <boost/lexical_cast.hpp>
#include <iostream>
#include <string>
#include <cstdio>
#include <cassert>
#include <set>
using namespace std;
int T, L, A, F;
string tree, animal;
set<string> features;
struct Node
{
    double weight;
    string f;
    Node *l, *r;
    Node() : l(0), r(0)
    {
    }
    void clear()
    {
	if (l) l->clear();
	if (r) r->clear();
	delete l;
	delete r;
    }
    double run(double p)
    {
	p *= weight;
	if (l == 0) return p;
	assert(l && r);
	if (features.find(f) != features.end())
	    return l->run(p);
	else
	    return r->run(p);
    }
};
Node *root;
Node *make(size_t& p)
{
    while (tree[p] == ' ')
	++p;
    assert(tree[p]=='(');
    ++p;
    while (tree[p] == ' ')
	++p;
    size_t q = std::min(tree.find(' ', p), tree.find(')', p));
    Node ret;
    ret.weight = boost::lexical_cast<double>(tree.substr(p, q-p));
    p = q;
    while (tree[p] == ' ')
	++p;
    if (tree[p] != ')') {
	q = tree.find(' ', p);
	ret.f = tree.substr(p, q-p);
	p = q+1;
	ret.l = make(p);
	ret.r = make(p);
	while (tree[p] == ' ')
	    ++p;
    }
    assert(tree[p]==')');    
    ++p;
    return new Node(ret);
}
int main() {
    cin >> T;
    string line, tmp;
    getline(cin, line);
    for (int t=0; t<T; ++t) {
	cin >> L;
	getline(cin, line);
	tree.clear();
	for (int i=0; i<L; ++i) {
	    getline(cin, line);
	    tree += line + " ";
	}
	size_t p = 0;
	root = make(p);
	cin >> A;
	printf("Case #%d:\n", t+1);
	for (int i=0; i<A; ++i) {
	    features.clear();
	    cin >> animal >> F;
	    for (int j=0; j<F; ++j) {
		cin >> tmp;
		features.insert(tmp);
	    }
	    printf("%.7f\n", root->run(1.0));
	}
	root->clear();
	delete root;
	root = 0;
    }
}
// 1:38 ac
