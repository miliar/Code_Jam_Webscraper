/*
 * A.cpp
 *
 *  Created on: 12/09/2009
 *      Author: Hamzawy
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;

/*
 #include <ext/hash_set>
 #include <ext/hash_map>
 using namespace __gnu_cxx;
 */

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
const long double PI = (2.0 * acos(0.0));

char str[8100];
char temp[8100];

struct Node {
	long double p;
	string name;
	Node* l, *r;
	Node() {
		l = r = 0;
	}
	Node(long double p, string name, Node* l, Node* r) :
		p(p), name(name) {
		this->l = l;
		this->r = r;
	}
};

long double p;
string name;
int siz;
int last;
inline void getPN(int ind) {
	while (str[ind] < '0' && str[ind] >= '9' && str[ind] != '.')
		ind++;
	string s(str + ind);
	stringstream ss(s);
	ss >> p;
	int ind1, ind2;
	for (ind1 = ind; ind1 < last; ind1++)
		if (str[ind1] == '(')
			break;
	for (ind2 = ind; ind2 < last; ind2++)
		if (str[ind2] == ')')
			break;
	if(ind2<ind1)
		getline(ss, name, ')');
	else
		ss>>name;
	ss.clear();
}

Node* build(int ind) {
	getPN(ind + 1);
	string na=name;
	long double lp=p;
	if (name==""||name[0] <'a'||name[0]>'z') {
		return new Node(p, "", NULL, NULL);
	}
	int ind1 = -1, ind2 = -1;
	for (int i = ind + 1; i < last; i++) {
		if (str[i] == '(') {
			ind1 = i;
			break;
		}
	}
	int cnt = 1;
	for (int i = ind1 + 1; i < last; i++) {
		if (str[i] == ')')
			cnt--;
		if (str[i] == '(')
			cnt++;
		if (!cnt) {
			ind2 = i;
			break;
		}
	}
	for (; ind2 < last; ind2++)
		if (str[ind2] == '(')
			break;
	Node* l = build(ind1);
	Node* r = build(ind2);
	return new Node(lp, na, l, r);
}
inline void nadaf() {
	str[0] = temp[0];
	int j = 1;
	for (int i = 1; i < last; i++)
		if (temp[i] == ')' || temp[i] == '(')
			str[j++] = ' ', str[j++] = temp[i], str[j++] = ' ';
		else
			str[j++] = temp[i];
	last = strlen(str);
}
set<string> se;

long double DFS(Node* n) {
	if (n->name == "")
		return n->p;
	if (se.find(n->name) != se.end())
		return DFS(n->l) * n->p;
	return DFS(n->r) * n->p;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large(2).in", "rt", stdin);
	freopen("1.out","wt",stdout);
#endif
	int t, n, m, l;
	scanf("%d", &t);
	for (int K = 0; K < t; K++) {
		scanf("%d ", &n);
		last = 0;
		while (n--) {
			gets(temp + last);
			last = strlen(temp);
		}
		nadaf();
		Node * root = build(0);
		printf("Case #%d:\n", K + 1);
		scanf("%d", &m);
		while (m--) {
			scanf(" %s%d", str, &l);
			se.clear();
			while (l--)
				scanf(" %s", str), se.insert(string(str));
			long double d = DFS(root);
			printf("%.7lf\n", (double) d);
		}
	}
	return 0;
}
