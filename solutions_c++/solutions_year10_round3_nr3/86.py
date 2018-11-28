#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <vector>
#include <map>
#include <string>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

void openfiles()
{
#ifndef ONLINE_JUDGE
	string file = "C-large";
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

int todec(char c) {
	if (c >= '0' && c <= '9')
		return c - '0';
	return 10 + c - 'A';
}

const int MAX = 520;
bool grid[MAX][MAX];
int square[MAX][MAX];
int down[MAX][MAX];
int righ[MAX][MAX];
bool taken[MAX][MAX];

#define SOLVE_VOID
#ifdef SOLVE_VOID
void solve(int test)
{
	int n, m;
	scanf("%d %d ",&n,&m);
	
	memset(grid,0,sizeof(grid));
	for (int i = 0; i < n; i++) {
		char row[1000];
		gets(row);
		for (int j = 0; j < m/4; j++) {
			int dec = todec(row[j]);
			for (int b = 0; b < 4; b++) {
				if ( ( dec >> ( 3 - b ) ) & 1 ) {
					grid[i][j*4+b] = 1;
				}
				else {
					grid[i][j*4+b] = 0;
				}
			}
		}
	}


	memset(square,0,sizeof(square));
	memset(down,0,sizeof(down));
	memset(righ,0,sizeof(righ));
	memset(taken,0,sizeof(taken));
	vector<pair<int, int> > mp[MAX];

	for (int i = n - 1; i >= 0; i--) {
		for (int j = m - 1; j >= 0; j--) {
			down[i][j] = 1;
			righ[i][j] = 1;
			if (down[i+1][j] && grid[i][j] == !grid[i+1][j]) {
				down[i][j] = down[i+1][j] + 1;
			}
			if (righ[i][j+1] && grid[i][j] == !grid[i][j+1]) {
				righ[i][j] = righ[i][j+1] + 1;
			}
			if (grid[i][j] == grid[i+1][j+1])
				square[i][j] = min(square[i+1][j+1] + 1, min(righ[i][j], down[i][j]));
			else
				square[i][j] = 1;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			for (int k = 1; k <= square[i][j]; k++)
				mp[k].push_back(make_pair(i,j));
		}
	}
	vector<pair<int, int> > answers;
	for (int i = MAX - 1; i >= 0; i--) {
		int sum = 0;
		for (int j = 0; j < mp[i].size(); j++) {
			bool ok = true;
			for (int ii = 0; ii < i && ok; ii++) {
				for (int jj = 0; jj < i; jj++) {
					if (taken[mp[i][j].first + ii][mp[i][j].second + jj]) {
						ok = false; break;
					}
				}
			}
			if (ok) {
				sum++;
				for (int ii = 0; ii < i; ii++) {
					for (int jj = 0; jj < i; jj++) {
						taken[mp[i][j].first+ii][mp[i][j].second+jj] = true;
					}
				}
			}
		}
		if (sum) {
			answers.push_back(make_pair(i, sum));
		}
	}
	printf("Case #%d: %d\n", test + 1, answers.size());
	for (int i = 0; i < answers.size(); i++) {
		printf("%d %d\n", answers[i].first, answers[i].second);
	}
	cerr << test + 1 << endl;
}
#endif

int main()
{
	openfiles();
	#ifdef SOLVE_BOOL
		while(solve());
	#endif
	#ifdef SOLVE_VOID
		int n; scanf("%d ",&n); REP(i,n) solve(i);
	#endif
	
	return 0;
}