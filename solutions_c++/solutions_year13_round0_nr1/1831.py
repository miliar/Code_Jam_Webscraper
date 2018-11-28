#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <cmath>
#include <stdio.h>
#include <vector>
#include <map>
#include <list>
#include <queue> 
#include <algorithm>
#include <bitset>
#include <set>

using namespace std;

#define REP(i,n) for(long long int i = 0; i < int(n); ++i)
#define REPV(i, n) for (long long int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(long long int i = (int)(a); i < (int)(b); ++i)

#define ALL(v) (v).begin(), (v).end()
#define PF push_front
#define PB push_back
#define MP make_pair
#define F first
#define S second

#define lli long long int

int sumX[4], sumY[4], diag1, diag2;
bool hasDot = false;

int main()
{
#ifdef FILE_IO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	char c;
	//cout << ((int)'.') << endl;
	//cout << ((int)'X') << endl;
	//cout << ((int)'O') << endl;
	//cout << ((int)'T') << endl;

	int Xwon1 = 4*((int)'X'), Xwon2 = 3*((int)'X') + ((int)'T');
	int Owon1 = 4*((int)'O'), Owon2 = 3*((int)'O') + ((int)'T');

	REP(i, T) {
		REP(j, 4) {
			sumX[j] = sumY[j] = 0;
		}
		hasDot = false;
		diag1 = diag2 = 0;
		REP(j, 4) {
			REP(k, 4) {
				cin >> c;
				if (c == '.') hasDot = true;
				sumX[j] += (int)c;
				sumY[k] += (int)c;
				if (k == j) diag1 += (int)c;
				if (j == (3 - k)) diag2 += (int)c;
			}
		}
		int won = -1;
		if (Xwon1 == diag1 || Xwon2 == diag1 ||Xwon1 == diag2 || Xwon2 == diag2) {
			won = 1;
		} else if (Owon1 == diag1 || Owon2 == diag1 || Owon1 == diag2 || Owon2 == diag2) {
			won = 2;
		} else {
			REP(j, 4) {
				if (Xwon1 == sumX[j] || Xwon2 == sumX[j] || Xwon1 == sumY[j] || Xwon2 == sumY[j]) {
					won = 1; break;
				} else if (Owon1 == sumX[j] || Owon2 == sumX[j] || Owon1 == sumY[j] || Owon2 == sumY[j]) {
					won = 2; break;
				}
			}
		}
		if (won == -1 && hasDot) won = 0;
		cout << "Case #" << (i + 1) << ": ";
		switch (won)
		{
		case -1:
			cout << "Draw" << endl;
			break;
		case 0:
			cout << "Game has not completed" << endl;
			break;
		case 1:
			cout << "X won" << endl;
			break;
		case 2:
			cout << "O won" << endl;
			break;
		}
	}
    return 0;
}