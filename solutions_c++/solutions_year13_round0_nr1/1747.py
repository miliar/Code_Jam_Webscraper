#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
typedef long long ll;
using namespace std;

#define FORi(n) for(int i=0;i<n;++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())

string inttostr (int a) {
    string s;
    ostringstream os;
    os << a;
    s = os.str();
    return s;
}

bool CheckField (vector<string> s, string m) {
	for (int i = 0; i < 4; ++i)
		if (s[i] == m) return true;
	string r = "    ";
	for (int i = 0; i < 4; ++i) {
		r = "    ";
		for (int j = 0; j < 4; ++j)
			r[j] = s[j][i];
		if (r == m) return true;
	}
	if (s[0][0]==m[0] && s[1][1]==m[1] && s[2][2]==m[2] && s[3][3]==m[3]) return true;
	if (s[0][3]==m[0] && s[1][2]==m[1] && s[2][1]==m[2] && s[3][0]==m[3]) return true;
	return false;
}

void solve () {
	int Ntests = 0;
	cin >> Ntests;
	vector<string> s (4, "");
	for (int test_id = 1; test_id <= Ntests; test_id++) {
		string res = "";
		for (int i = 0; i < 4; ++i) cin >> s[i];

		bool isDot = false;
		bool isT = false;
		int tPosX, tPosY;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				if (s[i][j] == '.') isDot = true;
				if (s[i][j] == 'T') {
					isT = true;
					tPosX = i;
					tPosY = j;
				}
			}
		if (isT) s[tPosX][tPosY] = 'X';
		bool isX = CheckField (s, "XXXX");
		if (isT) s[tPosX][tPosY] = 'O';
		bool isO = CheckField (s, "OOOO");

		if (isO) res = "O won";
		if (isX) res = "X won";
		if (!isO && !isX && isDot)  res = "Game has not completed";
		if (!isO && !isX && !isDot) res = "Draw";

		cin.get();
		cout << "Case #" << test_id << ": " << res << endl;
	}
}

void main()
{
    #ifdef _DEBUG
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    solve();
}