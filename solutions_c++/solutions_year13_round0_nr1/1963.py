#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <utility>
#include <set>
#include <functional>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
using namespace std;

#define FOR(_i,_n) for(int (_i)=0;(_i)<(_n);(_i)++)
#define iss istringstream
#define oss ostringstream
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pi 3.141592653589793
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int,int> Pair;

int dx[8] = { 0, 1,-1, 0, 1, 1,-1,-1};
int dy[8] = { 1, 0, 0,-1,-1, 1, 1,-1};
int hx[8] = {-2,-2,-1,-1, 1, 1, 2, 2};
int hy[8] = {-1, 1,-2, 2,-2, 2,-1, 1};

bool check(vector<string> v, char player) {
	int cnt = 0;
	FOR(i, 4) {
		cnt = 0;
		FOR(j, 4) if(v[i][j] == player) cnt ++;
		if(cnt == 4) return true;
	}
	FOR(j, 4) {
		cnt = 0;
		FOR(i, 4) if(v[i][j] ==  player) cnt ++;
		if(cnt == 4) return true;
	}
	cnt = 0;
	FOR(i, 4) if(v[i][i] == player) cnt ++;
	if(cnt == 4) return true;
	cnt = 0;
	FOR(i, 4) if(v[i][3-i] == player) cnt ++;
	if(cnt == 4) return true;
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) {
		vector<string> v(4);
		FOR(i, 4) cin >> v[i];
		
		int tx = -1;
		int ty = -1;
		FOR(i, 4) FOR(j, 4) if(v[i][j] == 'T') {
			tx = i;
			ty = j;
		}
		
		if(tx != -1 && ty != -1) {
			v[tx][ty] = 'X';
		}
		if(check(v, 'X')) {
			cout << "Case #" << t << ": X won" << endl;
			continue;
		}
		if(tx != -1 && ty != -1) {
			v[tx][ty] = 'O';
		}
		if(check(v, 'O')) {
			cout << "Case #" << t << ": O won" << endl;
			continue;
		}
		bool b = false;
		FOR(i, 4) FOR(j, 4) if(v[i][j] == '.') b = true;
		if(b) {
			cout << "Case #" << t << ": Game has not completed" << endl;
		} else {
			cout << "Case #" << t << ": Draw" << endl;
		}
	}
	
	return 0;
}
