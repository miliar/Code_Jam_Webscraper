/*
Compiled and Tested using Visual C++ 2008 Express Edition.
ONLINE_JUDGE is a macro for the Sphere Online Judge (SPOJ), where G++
compilers are used.
*/

#define _CRT_SECURE_NO_WARNINGS
//#define TEST

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<list>
#include<deque>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<time.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include<hash_map>
using namespace stdext;
#else
#include<ext/hash_map>
using namespace __gnu_cxx;

namespace __gnu_cxx {
	template<> struct hash<string> {
		size_t operator()(const string& x) const {
			return hash<const char*>() (x.c_str());
		}
	};
}
#endif

hash_map<string, int> hm;
char buffer[1000];

struct treeNode{
	int id;
	vector<treeNode*> sons;
	static treeNode slab[1000000];
	static int nSlab;

	inline void init(int s) {
		id = s;
		sons.clear();
	}

	static treeNode *newNode(int s) {
		slab[nSlab].init(s);
		return &slab[nSlab++];
	}

	inline pair<bool, treeNode*> checkSon(int s) {
		int i;
		for(i = 0; i < sons.size(); i++)
			if(sons[i]->id == s)
				break;
		if(i < sons.size())
			return make_pair(true, sons[i]);
		else {
			sons.push_back(newNode(s));
			return make_pair(false, sons[sons.size() - 1]);
		}
	}
};

treeNode treeNode::slab[1000000];
int treeNode::nSlab;

treeNode root;

int main(void) {
#ifndef ONLINE_JUDGE
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	int t, it, result, i, k, n, m, nS;
	char *p, *q;
	scanf("%d", &t);
	for(it = 1; it <= t; it++) {
		scanf("%d %d", &n, &m);
		treeNode::nSlab = 0;
		hm.clear();
		nS = 0;
		root.init(-1);
		treeNode *current;

		for(i = 0; i < n; i++) {
			scanf("%s", buffer);
			p = buffer + 1;
			current = &root;
			while(*p != '\0') {
				q = p;
				while(*q != '/' && *q != '\0')
					q++;
				if(*q == '/')
					*q = '\0';
				else
					q--; // gambiarra...
				if(hm.find(p) != hm.end())
					k = hm[p];
				else {
					k = nS++;
					hm[p] = k;
				}
				pair<bool, treeNode*> pp = current->checkSon(k);
				current = pp.second;
				p = q + 1;
			}
		}
		result = 0;
		for(i = 0; i < m; i++) {
			scanf("%s", buffer);
			p = buffer + 1;
			current = &root;
			while(*p != '\0') {
				q = p;
				while(*q != '/' && *q != '\0')
					q++;
				if(*q == '/')
					*q = '\0';
				else
					q--; // gambiarra...
				if(hm.find(p) != hm.end())
					k = hm[p];
				else {
					k = nS++;
					hm[p] = k;
				}
				pair<bool, treeNode*> pp = current->checkSon(k);
				current = pp.second;
				if(!pp.first)
					result++;
				p = q + 1;
			}
		}
		printf("Case #%d: %d\n", it, result);



	}
}
