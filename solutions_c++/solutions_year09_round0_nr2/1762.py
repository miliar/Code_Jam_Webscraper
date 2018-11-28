#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int codeType = 1;

const int MAXN = 256;

int inc[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

char v[MAXN][MAXN];
int a[MAXN][MAXN], R, C, use;
pair<int, int> s[MAXN][MAXN];

inline pair<int, int> findF(const int& x, const int& y) {
	if(s[x][y] == make_pair(x, y))
		return s[x][y];
	else {
		s[x][y] = findF(s[x][y].first, s[x][y].second);
		return s[x][y];
	} 
}

inline void comb(const int& x1, const int& y1, const int& x2, const int& y2) {
	pair<int, int> r1 = findF(x1, y1);
	pair<int, int> r2 = findF(x2, y2);
	s[r1.first][r1.second] = r2;
}

inline bool valid(const int& x, const int& y) {
	return x >= 0 && x < R && y >= 0 && y < C;
}

void flood(const int& curx, const int& cury) {
	int x, y, id = -1, mini = 1000000000;

	v[curx][cury] = '!';
	for(int i = 0; i < 4; i ++) {
		x = curx + inc[i][0];
		y = cury + inc[i][1];
		if(valid(x, y) && a[x][y] < a[curx][cury]) {
			if(a[x][y] < mini) {
				id = i;
				mini = a[x][y];
			}
		}
	}

	if(id >= 0) {
		x = curx + inc[id][0];
		y = cury + inc[id][1];
		comb(curx, cury, x, y);
		
		if(v[x][y] == '?')
			flood(x, y);
	}
}

int main()
{
	int cas;

	if(codeType == 0) {
		freopen("B-small-attempt3.in", "r", stdin);
		freopen("B-small.out", "w", stdout);
	}
	else if(codeType == 1) {
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);
	}
	else {
		freopen("input.txt", "r", stdin);
	}

	scanf("%d", &cas);
	for(int c = 1; c <= cas; c ++) {
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i ++) {
			for(int j = 0; j < C; j ++) {
				scanf("%d", &a[i][j]);

				v[i][j] = '?';		
				s[i][j] = make_pair(i, j);	
			}
		}
	
		for(int i = 0; i < R; i ++) {
			for(int j = 0; j < C; j ++) {
				if(v[i][j] == '?') {
					flood(i, j);
				}
			}
		}

		for(int i = 0; i < R; i ++)
			for(int j = 0; j < C; j ++)
				v[i][j] = '?';
		use = 'a';
		for(int i = 0;i < R; i ++) {
			for(int j = 0; j < C; j ++) {
				pair<int, int> id = findF(i, j);
				if(v[id.first][id.second] == '?')
					v[id.first][id.second] = use ++;
			}
		}

		printf("Case #%d:\n", c);
		for(int i = 0; i < R; i ++) {
			for(int j = 0; j < C; j ++) {
				if(j) putchar(' ');
				pair<int, int> id = findF(i, j);
				putchar(v[id.first][id.second]);
			}
			putchar('\n');
		}
	}

	return 0;
}