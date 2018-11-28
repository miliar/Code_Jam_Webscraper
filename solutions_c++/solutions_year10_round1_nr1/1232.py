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
	string file = "A-small-attempt0";
	//string file = "test";
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

bool won(char M[55][55], int n, int k, char c) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			int cnt = 0;
			for (int k = i; k < n; k++) {
				if (M[k][j] == c) cnt++;
				else break;
			}
			if (cnt >= k) return true;
			cnt = 0;
			for (int k = j; k < n; k++) {
				if (M[i][k] == c) cnt++;
				else break;
			}
			if (cnt >= k) return true;
			cnt = 0;
			for (int k = 0; i + k < n && j + k < n; k++) {
				if (M[i+k][j+k] == c) cnt++;
				else break;
			}
			if (cnt >= k) return true;
			cnt = 0;
			for (int k = 0; i - k >= 0 && j - k >= 0; k++) {
				if (M[i-k][j-k] == c) cnt++;
				else break;
			}
			if (cnt >= k) return true;
		}
	}
	return false;
}

#define SOLVE_VOID
#ifdef SOLVE_VOID
void solve(int test)
{
	char M[55][55];
	int n, k; scanf("%d %d ",&n,&k);
	for (int i = 0; i < n; i++) {
		gets(M[i]);
	}
	char MC[55][55];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			MC[j][n-i-1] = M[i][j];
		}
	}
	for (int i = n - 1; i >= 0; i--) {
		for (int j = n - 1; j >= 0; j--) {
			if (MC[i][j] == '.') {
				for (int k = i - 1; k >= 0; k--) {
					if (MC[k][j] != '.') {
						MC[i][j] = MC[k][j];
						MC[k][j] = '.';
						break;
					}
				}
			}
		}
	}

	bool blue = won(MC, n, k, 'B');
	bool red  = won(MC, n, k, 'R');
	string answer;
	if (blue && red)
		answer = "Both";
	else if (blue)
		answer = "Blue";
	else if (red)
		answer = "Red";
	else
		answer = "Neither";
	printf("Case #%d: %s\n", test + 1, answer.c_str());

	/*cout << "k = " << k << endl;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << MC[i][j] << " ";
		}
		cout << endl;
	}*/
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