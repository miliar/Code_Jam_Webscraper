/*******************************************************************************
* Program: file_fix-it;
* Copyright (c) 22 May 2010, Mateusz Kwiatek;
* email: <kwiatek.mateusz@gmail.com>
*******************************************************************************/
/*******************************************************************************
* Codejam 2010
* http://code.google.com
* ROUND: 1B;
* TASK: File Fix-it;
*******************************************************************************/

#define REP(i,n) for (int i = 0, _n = (n); i < _n; ++i)
#define REPD(i,n) for (int i = (n)-1; i >= 0; --i)
#define REPS(i,f,l) for (int i = (f), _l = (l); i < _l; ++i)
#define REPSD(i,f,l) for (int i = (l)-1, _f = (f); i >= _f; --i)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; ++i)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; --i)
#define FORE(it,c) for (__typeof((c).begin()) it = (c).begin(), _l = (c).end(); it != _l; ++it)
#define FORED(it,c) for (__typeof((c).rbegin()) it = (c).rbegin(), _l = (c).rend(); it != _l; ++it)
#define FOREACH(it,f,l) for (__typeof(f) it = (f), _l = (l); it != _l; ++it)
#define FOREACHD(it,f,l) for (__typeof(f) it = (l), _f = (f); it-- != _f; )
#define FORV(i,V) REP(i,(V).size())
#define ll long long

#include <cstdio>
#include <string>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

const int max_len = 10000000;
//------------------------------------------------------------------------------

namespace __gnu_cxx {

template<>
struct hash<string> {
    size_t operator () (const string &s) const {
		return __stl_hash_string(s.c_str());
	}
};

}

struct node {
	hash_map<string, node*> M;
	int add(char *f, char *l) {
		++f;
		if (f >= l)
			return 0;
		char *p = f+1;
		while (p < l && (*p != '/'))
			++p;
		*p = 0;
		string s(f);
		int res = 0;
		if (M.find(s) == M.end()) {
			++res;
			M[s] = new node();
		}
		res += M[s]->add(p, l);
		return res;
	}
};

void remove_node(node *u) {
	FORE(it,u->M) {
		remove_node(it->second);
	}
	delete u;
}

void testcase() {
	static char path[max_len+1];
	int n, m;
	scanf("%d %d\n", &n, &m);
	node *root = new node();
	REP(i,n) {
		scanf("%s", path);
		root->add(path, path+strlen(path));
	}
	int res = 0;
	REP(i,m) {
		scanf("%s", path);
		res += root->add(path, path+strlen(path));
	}
	printf("%d\n", res);
	remove_node(root);
}

int main()
{
	int z;
	scanf("%d\n", &z);
	REP(tid,z) {
		printf("Case #%d: ", tid+1);
		testcase();
	}
	return 0;
}
