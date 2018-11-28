#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#define INF 1000000000
#define INFll 1000000000000000000ll
#define LD long double
#define LL long long
#define Vi vector<int>
#define VI Vi::iterator
#define Si set<int>
#define SI Si::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Li list<int>
#define LI Li::iterator
#define pb push_back
#define mp make_pair
using namespace std;

string a[4];

bool equal(char a, char b, char c, char d, char t){
	if (a != t && a != 'T') return 0;
	if (b != t && b != 'T') return 0;
	if (c != t && c != 'T') return 0;
	if (d != t && d != 'T') return 0;
	return 1;
}

string solve(){
	for (int i = 0; i < 4; i++)
		cin >> a[i];
	for (int i = 0; i < 4; i++){
		if (equal(a[i][0], a[i][1], a[i][2], a[i][3], 'X'))
			return "X won";
		if (equal(a[i][0], a[i][1], a[i][2], a[i][3], 'O'))
			return "O won";
		if (equal(a[0][i], a[1][i], a[2][i], a[3][i], 'X'))
			return "X won";
		if (equal(a[0][i], a[1][i], a[2][i], a[3][i], 'O'))
			return "O won";
	}
	if (equal(a[0][0], a[1][1], a[2][2], a[3][3], 'O'))
		return "O won";
	if (equal(a[0][0], a[1][1], a[2][2], a[3][3], 'X'))
		return "X won";
	if (equal(a[0][3], a[1][2], a[2][1], a[3][0], 'O'))
		return "O won";
	if (equal(a[0][3], a[1][2], a[2][1], a[3][0], 'X'))
		return "X won";
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (a[i][j] == '.') return "Game has not completed";
	return "Draw";
}

int main(){
	int n;
	cin >> n;
	for (int t = 1; t <= n; t++)
		cout << "Case #" << t << ": " << solve() << endl;
		
	return 0;
}






