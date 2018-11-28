#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>

using namespace std;

#define VI vector<int> 
#define VS vector<string> 
#define LL long long 
#define FOR(i,n,m) for(int i=n;i<=m;i++)
#define REP(i,n) for(int i = 0; i < n; i++)
#define REPD(i,n) for(int i = n - 1; i>=0; i--)
#define BE(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair
#define SI(a) sizeof(a)
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR_SET(it, type, ss) for (set<type>::iterator it = ss.begin(); it!= ss.end(); it++)

const int INFI = 2000000000;
const int goX[4] = {-1, 0, 1, 0};
const int goY[4] = {0, 1, 0, -1};

const string PROBLEM_NAME = "A-small-attempt0";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());
const int MAXN = 200;
int n, m, K, T;
char c[MAXN][MAXN];
char d[MAXN][MAXN];

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

bool check1(int x, int y, char ch){
	if (n - x < K) return false;
	int i = x;
	while (i < n && d[i][y] == ch) i++;
	return i - x >= K;
}

bool check2(int x, int y, char ch){
	if (n - y < K) return false;
	int j = y;
	while (j < n && d[x][j] == ch) j++;
	return j - y >= K;
}

bool check3(int x, int y, char ch){
	if (n - x < K || n - y < K) return false;
	int i = x, j = y;
	while (i < n && j < n && d[i][j] == ch) {
		i ++; j++;
	}
	return min(i - x, j - y) >= K;
}

bool check4(int x, int y, char ch){
	if (n - x < K || y + 1 < K) return false;
	int i = x, j = y;
	while (i < n && j >= 0 && d[i][j] == ch) {
		i++; j--;
	}
	return min(i - x, y - j) >= K;
}

void solve(int testNo){

	REP(i, n)REP(j, n) d[j][n - 1 - i] = c[i][j];

	//REP(i, n) {
	//	REP(j, n) cout << d[i][j];
	//	cout << endl;
	//}

	for (int i = n - 1; i > 0; i--){
		REP(j, n) if (d[i][j] == '.'){
			int k = i;
			while (k >= 0 && d[k][j] == '.') k--;
			if (k >= 0) swap(d[i][j], d[k][j]);
		}
	}

	//REP(i, n) {
	//	REP(j, n) cout << d[i][j];
	//	cout << endl;
	//}

	bool f1, f2;
	f1 = f2 = false;
	REP(i, n) REP(j, n){
		if (check1(i, j, 'B')) f1 = true;
		if (check1(i, j, 'R')) f2 = true;

		if (check2(i, j, 'B')) f1 = true;
		if (check2(i, j, 'R')) f2 = true;

		if (check3(i, j, 'B')) f1 = true;
		if (check3(i, j, 'R')) f2 = true;

		if (check4(i, j, 'B')) f1 = true;
		if (check4(i, j, 'R')) f2 = true;
	}

	cout << "Case #" << testNo << ": ";
	if (f1){
		if (f2) cout << "Both";
		else cout << "Blue";
	} else {
		if (f2) cout << "Red";
		else cout << "Neither";
	}
	cout << endl;
}

void m_main(){
	cin >> T;
	REP(k, T){
		cin >> n >> K;
		REP(i, n){
			string s;
			cin >> s;
			REP(j, n) c[i][j] = s[j];
		}
		solve(k + 1);
	}

}

int main(){
	read_input();
	m_main();

	return 0;
}