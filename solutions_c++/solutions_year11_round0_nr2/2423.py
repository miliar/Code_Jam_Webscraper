/*
 * Magicka
 * May 7, 2011,
 * Another buggy code by Khaled Samy;)
 */
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))
#define loop(i,n) 		        for(int i=0;i<(int)n;i++)
#define loop2(i,n,m)            for(int i=n;i<(int)(m);i++)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef long long ll;
typedef stringstream SS;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int OO = (int) 2e9;
const double PI = 2 * acos(0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int n, c, d;
struct Combine {
	char F, S, to;
	Combine(char f, char s, char t) {
		F = f, S = s, to = t;
	}
};
vector<Combine> comb;
vector<pair<char, char> > opp;
vector<char> ans;
int vis[30];
char FindForm(char cur, char lst) {
	loop(i,SZ(comb))
		if ((comb[i].F == cur && comb[i].S == lst) || (comb[i].S == cur
				&& comb[i].F == lst))
			return comb[i].to;
	return '#';
}
bool FindOpp(char cur) {
	loop(i,SZ(opp)) {
		if (cur == opp[i].first) {
			if (vis[opp[i].second - 'A'])
				return 1;
		}
		if (cur == opp[i].second)
			if (vis[opp[i].first - 'A'])
				return 1;
	}
	return 0;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	loop(id,t) {
		string tmp;
		comb.clear();
		opp.clear();
		scanf("%d", &c);
		loop(i,c) {
			cin >> tmp;
			comb.push_back(Combine(tmp[0], tmp[1], tmp[2]));
		}
		scanf("%d", &d);
		loop(i,d) {
			cin >> tmp;
			opp.push_back(MP(tmp[0], tmp[1]));
		}
		CLR(vis,0);
		ans.clear();
		scanf("%d", &n);
		loop(i,n) {
			char cur;
			cin >> cur;
			if (SZ(ans) == 0) {
				ans.push_back(cur);
				vis[cur - 'A']++;
				continue;
			}
			// check on form
			if (SZ(ans)) {
				char lst = ans[SZ(ans) - 1];
				char res = FindForm(cur, lst);
				if (res != '#') {
					ans.erase(ans.begin() + SZ(ans) - 1);
					ans.push_back(res);

					vis[lst - 'A'] = max(vis[lst - 'A'] - 1, 0);
					vis[res - 'A']++;
					continue;
				}
			}
			// check on opp;
			bool res = FindOpp(cur);
			if (res) {
				ans.clear(), CLR(vis,0);
				continue;
			}
			vis[cur - 'A']++;
			ans.push_back(cur);
		}
		printf("Case #%d: [", id + 1);
		loop(i,SZ(ans)) {
			cout << ans[i];
			if (i + 1 < SZ(ans))
				cout << ", ";
		}
		cout << "]";
		cout << endl;
	}
	return 0;
}
