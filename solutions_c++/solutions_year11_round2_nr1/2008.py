/*
 * A.RPI.cpp
 *
 *  Created on: May 21, 2011
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;
const int mx = 101;
double m[mx], mo[mx], moo[mx], res[mx];
int cnt[mx], cnt1[mx];
int n;
vector<string> sc;

int main() {

	freopen("A-large (1).in", "rt", stdin);
	freopen("b.txt", "wt", stdout);

	int t;
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
		printf("Case #%d:\n", ii+1);
		scanf("%d", &n);
		sc = vector<string> ();
		string str;
		for (int i = 0; i < n; ++i) {
			cin >> str;
			sc.pb(str);
		}
		memset(m, 0, sizeof m);
		memset(mo, 0, sizeof mo);
		memset(moo, 0, sizeof moo);
		memset(cnt, 0, sizeof cnt);
		memset(cnt1, 0, sizeof cnt1);

		for (int i = 0; i < n; ++i) {
			int all = 0, w = 0;
			for (int j = 0; j < n; ++j) {
				if (i == j)
					continue;
				if (sc[i][j] == '.')
					continue;
				if (sc[i][j] == '1')
					w++;
				all++;
			}
			cnt[i] = all;
			m[i] = (double) w / (double) all;
		}

		for (int i = 0; i < n; ++i) {
			double nem = 0, dem = 0;
			for (int j = 0; j < n; ++j) {
				if (sc[i][j] != '.') {
					if(sc[j][i] == '0')
						nem += cnt[j] > 1 ? (m[j] * cnt[j]) / (cnt[j] - 1) : 0 , dem++;
					else
						nem += cnt[j] > 1 ? (m[j] * cnt[j] - 1 ) / (cnt[j] - 1) : 0 , dem++;
				}
			}
			cnt1[i] = dem;
//			cout << nem << " " << dem << endl;
			mo[i] = (nem) / dem;
		}


		for (int i = 0; i < n; ++i) {
			double nem = 0, dem = 0;
			for (int j = 0; j < n; ++j) {
				if (sc[i][j] != '.') {
					nem+=mo[j];
					dem++;
				}
			}
		//	cout << nem << " " << dem << endl;
			moo[i] = (nem) / dem;
		}


		for (int i = 0; i < n; ++i) {
			printf("%lf\n", 0.25 * m[i] + .5 * mo[i] + .25 * moo[i]);
		}

/*


		for (int i = 0; i < n; ++i) {
			cout << m[i] << "\t\t";
		}
		cout << endl;
		for (int i = 0; i < n; ++i) {
			cout << mo[i] << "\t\t";
		}
		cout << endl;
		for (int i = 0; i < n; ++i) {
			cout << moo[i] << "\t\t";
		}
		cout << endl;
*/
	}
	return 0;
}
/*



1
4
.11.
0.00
01.1
.10.


2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
 */
