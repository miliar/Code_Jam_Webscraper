#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

char grid[102][102];

char oldgrid[102][102];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(t, T) {
	cout << "Case #"<<(t+1)<<": ";
	DBG(1,"CASE " << (t+1));
	ZERO(grid);
	int r; cin >> r;
	cin.getline(buf,sizeof buf);
	FOR(i, r) {
	    int x1,y1,x2,y2;
	    cin >> x1 >> y1 >> x2 >> y2;
	    cin.getline(buf,sizeof buf);
	    for(int x=x1; x<=x2; x++) for(int y=y1; y<=y2; y++) grid[y][x] = 1;
	}
	int t = 0, ok = 0;
	do {
	    memcpy(oldgrid, grid, sizeof grid);
	    ok = 0;
	    FOR(y, 101) FOR(x, 101) {
		bool up = y && oldgrid[y-1][x];
		bool left = x && oldgrid[y][x-1];
		if (up && left) grid[y][x] = 1;
		else if (!up && !left) grid[y][x] = 0;
		// else stay the same
		ok += grid[y][x];
	    }
	    t++;
	} while (ok);
	cout << t;
	cout << endl;
    }
    return 0;
}
