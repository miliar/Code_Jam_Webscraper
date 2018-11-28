#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; e<= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n, t) t *v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c, t) for(VAR(i, (c).begin() , t); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

int alt[102][102];
int basin[100][100];
int CurrB;
char basLBL[26];
int listX[10000], listY[10000], listCount, listPos;


bool isSink(int x, int y)
{
	if ((alt[x][y+1] < alt[x+1][y+1]) || (alt[x+2][y+1] < alt[x+1][y+1]) || (alt[x+1][y] < alt[x+1][y+1]) || (alt[x+1][y+2] < alt[x+1][y+1])) return false;
	return true;
}

int flowDir(int x, int y)
{
	int g = alt[x+1][y+1]-1;
	if (alt[x][y+1] < g) g = alt[x][y+1];
	if (alt[x+2][y+1] < g) g = alt[x+2][y+1];
	if (alt[x+1][y] < g) g = alt[x+1][y];
	if (alt[x+1][y+2] < g) g = alt[x+1][y+2];

	if (alt[x+1][y] == g) return 0;
	if (alt[x][y+1] == g) return 1;
	if (alt[x+2][y+1] == g) return 2;
	if (alt[x+1][y+2] == g) return 3;

	return -1;
}

int main()
{
	int cases, H, W;

	cin >> cases;

	REP(c, cases)
	{
		cin >> W >> H;
		REP(y, W)
			REP(x, H) cin >> alt[x+1][y+1];
		REP(x, H+2)
			alt[x][0] = alt[x][W+1] = 10001;
		REP(y, W+2)
			alt[0][y] = alt[H+1][y] = 10001;
		REP(x, H)
			REP(y, W) basin[x][y] = -1;
		
		CurrB = 0;

		REP(x, H)
			REP(y, W) {
				listCount = 0;
				listPos = 0;
				if ((basin[x][y] < 0) && isSink(x,y)) {
					listX[listPos] = x;
					listY[listPos] = y;
					listCount++;
				}
				while (listPos < listCount)
				{
					int ax = listX[listPos], ay = listY[listPos];
					basin[ax][ay] = CurrB;
				
					if (flowDir(ax, ay-1) == 3) {listX[listCount] = ax; listY[listCount] = ay-1; listCount++;};
					if (flowDir(ax-1, ay) == 2) {listX[listCount] = ax-1; listY[listCount] = ay; listCount++;};
					if (flowDir(ax+1, ay) == 1) {listX[listCount] = ax+1; listY[listCount] = ay; listCount++;};
					if (flowDir(ax, ay+1) == 0) {listX[listCount] = ax; listY[listCount] = ay+1; listCount++;};
					
					listPos++;
				}
				if (listCount > 0) CurrB++;
		}

		char chr = 'a';
		REP(asd, 26) basLBL[asd] = '0';
		REP(y, W)
			REP(x, H)	
				if (basLBL[basin[x][y]] == '0') {basLBL[basin[x][y]] = chr; chr++;};


		cout << "Case #" << c+1 << ":" << endl;
		REP(y, W) {
			REP(x, H) {if (x) cout << " "; cout << basLBL[basin[x][y]];};
			//REP(x, H) cout << basin[x][y] << " ";
			cout << endl;
		}

	}//case

	return 0;
};