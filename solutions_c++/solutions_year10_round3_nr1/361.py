/*
 *	E-Mail : khaled.samy@fci-cu.edu.eg
 *	TopCoder Handle : Khaled91
 *	Another buggy code by Khaled Samy ;)
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

const int OO = (int) 1e9;
const double PI = 2 * acos(0);
const double EPS = 1e-9;

int dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a > b ? 1 : 2;
}

int DI[] = { -1, 0, 1, 0, 1, -1, -1, 1 };
int DJ[] = { 0, 1, 0, -1, 1, -1, 1, -1 };

int main() {
	freopen("a.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
	int T;
	cin >> T;
	loop2(ID,1,T+1) {
		int n;
		cin >> n;
		vector<pii> v;
		loop(i,n) {
			int f, t;
			cin >> f >> t;
			v.PB(MP(f, t));
		}
		int ret = 0;
		loop(i,n) {
			loop2(j,i+1,n) {
				if (i == j)
					continue;
				if ((v[i].first < v[j].first) + (v[i].second < v[j].second)
						== 1)
					ret++;
			}
		}
		printf("Case #%d: %d\n", ID, ret);
	}
	return 0;
}
