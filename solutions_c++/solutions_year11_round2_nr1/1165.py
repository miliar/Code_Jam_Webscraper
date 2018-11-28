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
	string file = "A-large";
	//freopen("test.in", "rt", stdin);
	freopen((file + ".in").c_str(),"rt",stdin);
	freopen((file + ".out").c_str(),"wt",stdout);
#endif
}

double wp(vector<vector<char> >& board, int team) {
	int won = 0;
	int played = 0;
	for (int j = 0; j < board.size(); j++) {
		if (j != team && board[team][j] == '1')
			won++;
		if (board[team][j] == '0' || board[team][j] == '1')
			played++;
	}
	return won / (double)played;
}

double wpc(vector<vector<char> >& board, int team, int crossed) {
	int won = 0;
	int played = 0;
	for (int j = 0; j < board.size(); j++) {
		if (j == team) continue;
		if (j == crossed) continue;

		if (board[team][j] == '1') won++;
		if (board[team][j] == '0' || board[team][j] == '1')
			played++;
	}
	return won / (double)played;
}

void solve(int test)
{
	int teams; scanf("%d ", &teams);
	vector<vector<char> > board(teams, vector<char>(teams));
	for (int i = 0; i < teams; i++) {
		for (int j = 0; j < teams; j++) {
			scanf("%c ", &board[i][j]);
		}
	}

	vector<double> wps(teams);
	for (int i = 0; i < teams; i++) {
		wps[i] = wp(board, i);
	}

	vector<double> owp(teams);
	for (int i = 0; i < teams; i++) {
		double rollwp = 0.0;
		int count = 0;
		for (int j = 0; j < teams; j++) if (i != j) {
			if (board[i][j] != '.') {
				count++;
				rollwp += wpc(board, j, i);
			}
		}
		owp[i] = rollwp / count;
	}

	printf("Case #%d:\n", test);
	vector<double> oowp(teams);
	for (int i = 0; i < teams; i++) {
		double rollowp = 0.0;
		int count = 0;
		for (int j = 0; j < teams; j++) if (i != j) {
			if (board[i][j] != '.') {
				count++;
				rollowp += owp[j];
			}
		}
		double oowp = rollowp / count;
		//cout << wps[i] << " " << owp[i] << " " << oowp << endl;
		printf("%.10lf\n", wps[i] * 0.25 + owp[i] * 0.5 + oowp * 0.25);
	}
}

int main()
{
	openfiles();
	int n; scanf("%d ",&n); REP(i,n) solve(i + 1);
	
	return 0;
}