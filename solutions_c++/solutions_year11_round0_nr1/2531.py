/*
 * BotTrust
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

vector<pair<char, int> > v;
vector<int> Bpos, Opos;
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	loop(id,t) {
		int n;
		scanf("%d", &n);
		v.clear(), v.resize(n);
		Bpos.clear(), Opos.clear();
		loop(i,n) {
			cin >> v[i].first >> v[i].second;
			if (v[i].first == 'O')
				Opos.push_back(v[i].second);
			else
				Bpos.push_back(v[i].second);
		}
		int idx = 0;
		int bidx = 0, oidx = 0;
		int b = 1, o = 1;
		int i = 0;
		for (i = 0;; i++) {
			if (idx >= n)
				break;
			if (bidx >= SZ(Bpos) && oidx >= SZ(Opos))
				break;
			char cur = v[idx].first;
			int dist = v[idx].second;
			if (cur == 'O') {
				if (dist > o)
					o++;
				else if (dist < o)
					o--;
				else
					oidx++, idx++;

				if (Bpos[bidx] > b)
					b++;
				else if (Bpos[bidx] < b)
					b--;

			} else {
				// B
				if (dist > b)
					b++;
				else if (dist < b)
					b--;
				else
					bidx++, idx++;

				if (Opos[oidx] > o)
					o++;
				else if (Opos[oidx] < o)
					o--;
			}
		}
		printf("Case #%d: %d\n", id + 1, i);
	}
	return 0;
}
