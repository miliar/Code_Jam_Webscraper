#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-9;

struct node{
	string name;
	ld p;
};

node tree[100000];

ld toD(string& s){
	stringstream st;
	st << s;
	ld ans;
	st >> ans;
	return ans;
}

void make_tree(string& s, int idx, int lf, int rg){
	lf++;
	rg--;
	string num;
	while(!isdigit(s[lf])) lf++;
	while(isdigit(s[lf]) || s[lf] == '.'){
		num += s[lf];
		lf++;
	}
	ld p = toD(num);
	node cur = {"", p};
	while(s[lf] == ' ') lf++;
	if(lf >= rg){
		tree[idx] = cur;
	}else{
		while(isalpha(s[lf]) && lf <= rg) cur.name += s[lf], lf++;
		while(s[lf] != '(') lf++;
		int lf1 = lf, rg1 = -1;
		int bal = 1;
		for(int i = lf1 + 1; i <= rg; ++i){
			if(s[i] == '(') bal++;
			if(s[i] == ')') bal--;
			if(bal == 0){
				rg1 = i;
				break;
			}
		}
		assert(rg1 != -1);
		tree[idx] = cur;
		make_tree(s, 2 * idx + 1, lf1, rg1);
		while(s[rg1] != '(') rg1++;
		while(s[rg] != ')') rg--;
		make_tree(s, 2 * idx + 2, rg1, rg);
	}
}

ld solve(set<string>& s, int idx){
	if(tree[idx].name.empty()) return tree[idx].p;
	if(s.count(tree[idx].name)){
		return tree[idx].p * solve(s, 2 * idx + 1);
	}else
		return tree[idx].p * solve(s, 2 * idx + 2);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T;
	scanf("%d\n", &T);
	for1(Q, T){
		printf("Case #%d:\n", Q);
		int L;
		scanf("%d\n", &L);
		string tmp, s;
		forn(i, L) getline(cin, tmp), s += tmp;
		make_tree(s, 0, 0, sz(s) - 1);

		int A;
		cin >> A;
		forn(i, A){
			string name;
			cin >> name;
			int cnt;
			cin >> cnt;
			set<string> cur;
			forn(i, cnt){
				cin >> name;
				cur.insert(name);
			}
			cout.precision(6);
			cout << fixed << solve(cur, 0) << endl;
		}
	}
    return 0;
}
