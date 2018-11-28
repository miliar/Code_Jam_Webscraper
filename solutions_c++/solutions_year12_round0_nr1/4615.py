/*
 ID: conan.d1
 PROG: A
 LANG: C++
 */
#include <cstring>
#include <iterator>
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
#define SZ(v)                   (int)v.size()
#define all(v)					v.begin(), v.end()
typedef long long ll;
const int OO = 1 << 28;

int di[] = { 1, 0, -1, 0 };
int dj[] = { 0, 1, 0, -1 };

char eng[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
		'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

int main() {
//	freopen("A.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	int t;
	string g, to;
	cin >> t;
	getline(cin, g);
	for (int i = 1; i <= t; ++i) {
		getline(cin, g);
		to = "";
		for (int j = 0; j < SZ(g); j++) {
			if (g[j] == ' ') {
				to += ' ';
				continue;
			}
			to += eng[g[j] - 'a'];
		}
		cout <<"Case #" << i << ": " <<  to << endl;
	}
	return 0;
}

