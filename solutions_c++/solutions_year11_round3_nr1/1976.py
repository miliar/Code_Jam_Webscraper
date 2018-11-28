/*
 * SquareTiles
 * May 22, 2011,
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
const double PI = 2 * acos(0.0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { 0, 1, 1 };
int DJ[] = { 1, 0, 1 };

char g[51][51];
bool vis[51][51];
int r, c;
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.in", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	loop(id,t) {
		scanf("%d%d", &r, &c);
		CLR(vis,0);
		loop(i,r)
			loop(j,c) {
				cin >> g[i][j];
				if (g[i][j] == '.')
					vis[i][j] = 1;
			}

		printf("Case #%d:\n", id + 1);
		bool bad = 0;
		loop(i,r) {

			if (bad)
				break;

			loop(j,c) {
				if (bad)
					break;

				if (vis[i][j])
					continue;

				int cc = 0;
				g[i][j] = '/';
				vis[i][j] = 1;

				loop(k,3) {

					int ni = i + DI[k];
					int nj = j + DJ[k];

					if (ni >= r || ni < 0 || nj >= c || nj < 0) {
						bad = 1;
						break;
					}

					cc++;
					if (cc == 1)
						g[ni][nj] = '\\';
					else if (cc == 2)
						g[ni][nj] = '\\';
					else
						g[ni][nj] = '/';

					vis[ni][nj] = 1;

				}
			}
		}

		if (bad)
			printf("Impossible\n");
		else {
			loop(i,r) {
				loop(j,c)
					cout << g[i][j];
				cout << endl;

			}
		}

	}
	return 0;
}
