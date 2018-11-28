#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list>
#include <cassert>
#include <conio.h>
using namespace std; 

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 

bool isWinner(int num)
{
	int win[10] = {0xF000, 0x0F00, 0x00F0, 0x000F, 0x1111, 0x2222, 0x4444, 0x8888, 0x1248, 0x8421};
	REP(i, 10) if ((num & win[i]) == win[i]) return true;
	return false;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;	
	cin >> T;
	cin.get();
	REP(i, T)
	{
		int xline = 0, oline = 0;
		char ch;
		bool empty = false;
		REP(n, 4) 
		{
			REP(p, 4)
			{
				ch = cin.get();
				int d = (n-1)*p + p - 1;
				if (ch == 'X' || ch == 'T') xline |= (int(1) << (4*n + p));
				if (ch == 'O' || ch == 'T') oline |= (int(1) << (4*n + p));
				if (ch == '.') empty = true;
			}
			cin.get();
		}
		cin.get();
		cout << "Case #" << i+1 << ": ";
		if (isWinner(xline)) cout << "X won";
		else if (isWinner(oline)) cout << "O won";
		else if (empty) cout << "Game has not completed";
		else cout << "Draw";
		cout << endl;
	}
	return 0;
}