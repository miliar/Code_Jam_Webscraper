#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define pi 3.1415926535897932
#define ll long long
#define ld long double

using namespace std;

int m, n;
int u[2010];
int v[2010];
bool q = false;
int use[10], use1[10];
vector <int> help;
int sz1 = 0;
vector <int> a[10], b[10], a1[10];

void rest(int qqq, int sz){
	q = true;
	printf ("Case #%d: %d\n", qqq + 1, sz);
	forn(i, n)
		printf ("%d ", help[i] + 1);
	printf ("\n");
}

bool check(int sz){
	forn(i, sz1){
		memset(use1, false, sizeof(use1));
		int kol = 0;
		forn(j, a[i].size())
			if (!use1[help[a[i][j]]]){
				use1[help[a[i][j]]] = true;
				kol ++;
			}
		if (kol < sz) return false;
	}
	return true;
}

void calc(int v, int kol, int sz, int qqq){
	if (v == n){
		if (kol == sz && check(sz)) rest(qqq, sz);
		return;
	}
	forn(i, sz)
		if (!q){
			use[i] ++;
			help.pb(i);
			calc(v + 1, kol + (use[i] == 1), sz, qqq);
			use[i] --;
			help.pop_back();
		}
}

stack <int> st;

void gen(){
	sz1 = 1;
	forn(i, m){
		a1[u[i]].pb(v[i]);
		b[v[i]].pb(u[i]);
	}
	forn(i, n){
		sort(a1[i].begin(), a1[i].end());
		sort(b[i].begin(), b[i].end());
	}
	st.push(0);
	forn(i, n){
		forn(j, b[i].size()){
			int k = st.top();
			a[k].pb(i);
			st.pop();
		}
		if (!st.empty()){
			int k = st.top();
			a[k].pb(i);
		}
		forn(j, a1[i].size()){
			a[sz1 ++].pb(i);
			st.push(sz1 - 1);
		}
	}
	//forn(i, sz1){
	//	forn(j, a[i].size())
	//		printf ("%d ", a[i][j] + 1);
	//	printf ("\n");
	//}
}

int main(){
#ifndef ONLINE_JUDGE
	freopen ("input.txt","rt",stdin);
	freopen ("output.txt","wt",stdout);
#endif
	int t;
	cin >> t;
	forn(qqq, t){
		q = false;
		memset(use, false, sizeof(use));
		cin >> n >> m;
		forn(i, n){
			a[i].clear();
			b[i].clear();
			a1[i].clear();
		}
		forn(i, m){
			scanf("%d", &u[i]);
			u[i] --;
		}
		forn(i, m){
			scanf("%d", &v[i]);
			v[i] --;
		}
		gen();
		for (int i = n - 1; i >= 1; i --){
			calc(0, 0, i, qqq);
			if (q) break;
		}
	}
	return 0;
}