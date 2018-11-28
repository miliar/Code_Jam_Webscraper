#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<VB> VVB;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef tr1::unordered_set<vector<bool> > MB;
typedef set<VVB> MVVB;
typedef map<char, PII> MCPII;
ifstream fin("input.in");
ofstream fout("output");
int N;

bool e(char c1, char c2) {
	return (c1 == c2) || (c1 == 'T') || (c2 == 'T');
}

class Test {
public:
	VVC bd;
	bool hasEmpty = false;

	Test(int n) {
		bd.resize(4, VC(4));

		REP(i, 4) {
			REP(j, 4) {
				fin >> bd[i][j];
				if (bd[i][j] == '.') {
					hasEmpty = true;
				}
				cout << bd[i][j];
			}
			cout << endl;
		}

		cout << endl;

		fout << "Case #" << n << ": ";
		if (allSame('X')) {
			fout << "X won" << endl;
		} else if (allSame('O')) {
			fout << "O won" << endl;
		} else if (hasEmpty) {
			fout << "Game has not completed" << endl;
		} else {
			fout << "Draw" << endl;
		}
	}

	bool allSame(char c) {
		return ((e(bd[0][0], c) && e(bd[1][1], c) && e(bd[2][2], c) && e(bd[3][3], c)) ||
			(e(bd[0][3], c) && e(bd[1][2], c) && e(bd[2][1], c) && e(bd[3][0], c)) ||
			(e(bd[0][0], c) && e(bd[0][1], c) && e(bd[0][2], c) && e(bd[0][3], c)) ||
			(e(bd[1][0], c) && e(bd[1][1], c) && e(bd[1][2], c) && e(bd[1][3], c)) ||
			(e(bd[2][0], c) && e(bd[2][1], c) && e(bd[2][2], c) && e(bd[2][3], c)) ||
			(e(bd[3][0], c) && e(bd[3][1], c) && e(bd[3][2], c) && e(bd[3][3], c)) ||
			(e(bd[0][0], c) && e(bd[1][0], c) && e(bd[2][0], c) && e(bd[3][0], c)) ||
			(e(bd[0][1], c) && e(bd[1][1], c) && e(bd[2][1], c) && e(bd[3][1], c)) ||
			(e(bd[0][2], c) && e(bd[1][2], c) && e(bd[2][2], c) && e(bd[3][2], c)) ||
			(e(bd[0][3], c) && e(bd[1][3], c) && e(bd[2][3], c) && e(bd[3][3], c)));
	}
};

int main() {
	cout << "starting" << endl;
	fin >> N;
	REP(i, N) {
		Test(i+1);
	}
}
