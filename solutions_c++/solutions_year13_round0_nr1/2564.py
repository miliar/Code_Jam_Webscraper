#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define Pair pair<int,int>
#define equal(a,b) (ABS(a-b)<eps)
using namespace std;

template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

/////////////////////////////////////////////////////////////////////////////////////////////////////

string fileName = "A-large";

bool check(string s, char c) {
	int cnt = 0;
	for (int i = 0; i < 4; i++)
		if (s[i] == c || s[i] == 'T') cnt++;
	return cnt == 4;
}

void solveSingle(int testNumber) {
	string s[4];
	for (int i = 0; i < 4; i++) {
		cin >> s[i];
	}

	int res = -1;

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (s[i][j] == '.') res = -2;

	for (int i = 0; i < 4; i++) {
		string x = "", y = "";
		for (int j = 0; j < 4; j++) {
			x += s[i][j];
			y += s[j][i];
		}
		if (check(x, 'X') || check(y, 'X')) res = 0;
		if (check(x, 'O') || check(y, 'O')) res = 1;
	}

	string x;
	x = x + s[0][0] + s[1][1] + s[2][2] + s[3][3];
	string y;
	y = y + s[0][3] + s[1][2] + s[2][1] + s[3][0];

//	cout << x << " " << y << endl;

	if (check(x, 'X') || check(y, 'X')) res = 0;
	if (check(x, 'O') || check(y, 'O')) res = 1;

	printf("Case #%d: ", testNumber);

	if (res == -2) printf("Game has not completed\n");
	else if (res == -1) printf("Draw\n");
	else if (res == 0) printf("X won\n");
	else printf("O won\n");
}

int main() {
	freopen((fileName + ".in").c_str(), "r", stdin);
	freopen((fileName + ".out").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		solveSingle(t);
		fflush(stdout);
	}
	return 0;
}
