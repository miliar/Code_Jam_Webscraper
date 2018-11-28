/*
 * a.cpp
 *
 *  Created on: May 22, 2011
 *      Author: user1
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
#include <cstring>
#include <vector>
#include <set>
#include <complex>
#include <valarray>
#include <ctime>
#include <string.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(typeof(m) i=0;i<m;++i)
#define forin(i,a,b) for(typeof(a) i=a;i<=b;++i)
#define foreach(i,m) for(typeof((m).begin()) i=(m).begin();i!=(m).end();++i)
#define rrep(i,m) for(typeof(m) i=m-1;i>=0;--i)
#define rforin(i,a,b) for(typeof(b) i=b;i>=b;--i)
#define rforeach(i,m) for(typeof((m).rbegin()) i=(m).rbegin();i!=(m).rend();++i)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

char a[100][100];

int val(int i, int j) {
	bool aa = a[i][j] == '#' || a[i - 1][j] == '#' || a[i][j - 1] == '#' || a[i
			- 1][j - 1] == '#', b = a[i][j] == '#' && a[i - 1][j] == '#'
			&& a[i][j - 1] == '#' && a[i - 1][j - 1] == '#';
	if (b)
		return 1;
	if (aa)
		return 2;
	return 0;
}
int replace(int i, int j) {
	a[i][j] = a[i - 1][j - 1] = '/';
	a[i - 1][j] = a[i][j - 1] = '\\';
	return 0;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
#endif

	int t, r, c, K = 0, x;

	scanf("%d", &t);
	while (t--) {
		printf("Case #%d:\n", ++K);
		scanf("%d%d", &r, &c);

		rep(i,r)
			rep(j,c)
				scanf(" %c", a[i] + j);
		bool f = 0;
		for (int i = 1; i < r; ++i)
			for (int j = 1; j < c; ++j)
				if ((x = val(i, j)) == 1) {
					replace(i, j);
				}

		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (a[i][j] == '#') {
					f = 1;
					break;
				}

		if (f)
			printf("Impossible\n");
		else
			for (int i = 0; i < r; ++i)
				a[i][c] = 0, printf("%s\n", a[i]);

	}

	return 0;
}
