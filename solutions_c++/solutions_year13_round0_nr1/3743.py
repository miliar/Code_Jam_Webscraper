#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

const int dx[] = {1, 1, 1, 0};
const int dy[] = {-1, 0, 1, 1};

const char symb[] = {'X', 'O'};

void testcase(int tst)
{
	VS a(4);
	REP(i, 4)
		getline(ifs, a[i]);

	string s;
	getline(ifs, s);

	int won = -1;
	REP(c, 2) {
		REP(z, 4) {
			REP(j, 4)
				REP(i, 4) {
					bool ok = true;
					REP(k, 4) {
						int y = j + dy[z]*k;
						int x = i + dx[z]*k;
						if (!(y >= 0 && y < 4 && x >= 0 && x < 4 && (a[y][x] == symb[c] || a[y][x] == 'T')))
							ok = false;
					}
					if (ok && won == -1)
						won = c;
				}
		}
	}

	bool empty = false;
	REP(j, 4)
		REP(i, 4)
			if (a[j][i] == '.')
				empty = true;

	if (won != -1) {
		ofs << "Case #" << tst+1 << ": " << symb[won] << " won" << endl;
	} else {
		if (empty) {
			ofs << "Case #" << tst+1 << ": " << "Game has not completed" << endl;
		} else {
			ofs << "Case #" << tst+1 << ": " << "Draw" << endl;
		}
	}
}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	string s;
	getline(ifs, s);

	sscanf(s.c_str(), "%d", &t);
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
