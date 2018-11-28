#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

#define FORab(i,a,b) for(int i = (a); i < (b); i++)
#define FORn(i,n) FORab(i,0,n)
#define DBG(args...) /*fprintf(stderr, args)*/

void main2() {
	vector<int> O, B;
	vector<bool> turn; // true for O's, false for B's

	int N; cin >> N;
	while(N--) {
		char c; int x;
		cin >> c >> x;
		if(c == 'O')
			O.push_back(x);
		else
			B.push_back(x);
		turn.push_back(c == 'O');
	}

	for(int i = 0, oi = 0, bi = 0; i < turn.size(); i++)
		DBG("%c %d ", turn[i] ? 'O' : 'B', turn[i] ? O[oi++] : B[bi++]);

	int ox = 1, bx = 1, oi = 0, bi = 0, t = 0;

	DBG("\n ox  bx   t     O            B    \n");
	DBG(" %2d  %2d  %2d ", ox, bx, t);
	DBG("["); FORab(i,oi,O.size()) DBG("%d ", O[i]); DBG("] ");
	DBG("["); FORab(i,bi,B.size()) DBG("%d ", B[i]); DBG("] ");
	DBG("\n");

	for(vector<bool>::iterator it = turn.begin(); it != turn.end(); it++) {
		if(*it) {
			// Calculate time required
			int x = O[oi++], dx = x - ox;
			dx = (dx < 0 ? -dx : dx);
			int dt = dx + 1;
			ox = x;

			// Move B along, if required
			if(bi < B.size()) {
				int x2 = B[bi], dx2 = x2 - bx, dx3 = (dx2 < 0 ? -dx2 : dx2);
				int dt2 = dx3 + 1;
				if(dt2 > dt) {
					bx += (dx2 < 0 ? -dt : dt);
				} else {
					bx = x2;
				}
			}
			t += dt;
		} else {
			// Calculate time required
			int x = B[bi++], dx = x - bx;
			dx = (dx < 0 ? -dx : dx);
			int dt = dx + 1;
			bx = x;

			// Move O along, if required
			if(oi < O.size()) {
				int x2 = O[oi], dx2 = x2 - ox, dx3 = (dx2 < 0 ? -dx2 : dx2);
				int dt2 = dx3 + 1;
				DBG("x2 = %d, dx2 = %d, dx3 = %d dt2 = %d, dt = %d\n", x2, dx2, dx3, dt2, dt);
				if(dt2 > dt) {
					ox += (dx2 < 0 ? -dt : dt);
				} else {
					ox = x2;
				}
			}
			t += dt;
		}
		DBG(" %2d  %2d  %2d ", ox, bx, t);
		DBG("["); FORab(i,oi,O.size()) DBG("%d ", O[i]); DBG("] ");
		DBG("["); FORab(i,bi,B.size()) DBG("%d ", B[i]); DBG("] ");
		DBG("\n");
	}
	cout << t;
}

int main() {

	int T; cin >> T;

	for(int caseno = 1; caseno <= T; caseno++) {
		cout << "Case #" << caseno << ": ";
		main2();
		cout << endl;
	}

	return 0;
}
