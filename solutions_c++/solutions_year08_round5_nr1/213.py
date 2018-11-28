#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#pragma comment(linker, "/STACK:64000000")

#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()

int ver[1000][1000] = {0};
int hor[1000][1000] = {0};

int solve() {
	int L;
	cin >> L;
	string s = "";
	while (L--) {
		string buf;
		int rep;
		cin >> buf >> rep;		
		while (rep--)
			s.append(buf);
	}
	const int INIT = 300;
	int x = INIT, y = INIT, dir = 0;
	int dx[] = {0, -1, 0, 1};
	int dy[] = {1, 0, -1, 0};
	memset(hor, 0, sizeof(hor));
	memset(ver, 0, sizeof(ver));		
	vector<int> X, Y;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == 'F') {
			if (dir == 0) ver[x][y] = 1;
			else if (dir == 1) hor[x - 1][y] = 1;
			else if (dir == 2) ver[x][y - 1] = 1;
			else if (dir == 3) hor[x][y] = 1;			
			X.pb(x);
			Y.pb(y);
			x += dx[dir];
			y += dy[dir];			
		}
		else if (s[i] == 'L') dir = (dir + 1) % 4;
		else dir = (dir + 3) % 4;
	}
	int res = 0;		
	for (int i = 0; i < X.size(); i++)		
		res += (X[(i + 1) % X.size()] - X[i]) * Y[i];
	if (res > 0) res = -res;
	for (int i = INIT-120; i <= INIT+120; i++)
		for (int j = INIT-120; j <= INIT+120; j++) {
			bool left = false, right = false, down = false, up = false;
			for (int ii = INIT-120; ii <= i; ii++)
				if (ver[ii][j]) left = true;
			for (int ii = i + 1; ii <= INIT+120; ii++)
				if (ver[ii][j]) right = true;		
			for (int jj = INIT-120; jj <= j; jj++)
				if (hor[i][jj]) down = true;
			for (int jj = j + 1; jj <= INIT+120; jj++)
				if (hor[i][jj]) up = true;		

			if ((left && right) || (up && down))
				res++;
		}
	return res;
}

int main () {
	freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int T = 1; T <= nTests; T++)
		printf("Case #%d: %d\n", T, solve());
	fclose(stdin); fclose(stdout);
	return 0;
}
