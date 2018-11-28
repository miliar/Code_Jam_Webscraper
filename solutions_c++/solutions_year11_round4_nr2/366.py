#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

int mat[512][512];

int main() {
    int T;
    cin >> T; cin.getline(buf, sizeof buf);
    FOR(tt, T) {
    nextt:
	int R, C, D;
	cin >> R >> C >> D;
	cin.getline(buf, sizeof buf);

	FOR(y, R) {
	    cin.getline(buf, sizeof buf);
	    FOR(x, C) mat[y][x] = buf[x] - '0';
	}

	int ret = -1;
	
	FOR(y, R) FOR(x, C) {
	    int sx = 0, sy = 0; // sum x * w[y][x] and y * w[y][x]
	    int s = 0;		// sum w[y][x]
	    FOR(k, 500) { // add row/col # k (sz == k+1)
		if (y + k >= R || x + k >= C) break;

		FOR(yy, k)   sx +=  k * mat[y+yy][x+k] , sy += yy * mat[y+yy][x+k] , s += mat[y+yy][x+k];
		FOR(xx, k+1) sx += xx * mat[y+k] [x+xx], sy +=  k * mat[y+k] [x+xx], s += mat[y+k] [x+xx];

		//DBG(1, V(tt)<<V(y)<<V(x)<<V(k)<<V(sx)<<V(sy));

		int nsx = sx - k * mat[y][x+k] - k * mat[y+k][x+k];
		int nsy = sy - k * mat[y+k][x] - k * mat[y+k][x+k];
		int ns  = s - mat[y][x] - mat[y+k][x] - mat[y][x+k] - mat[y+k][x+k];
		//		DBG(1, V(tt)<<V(y)<<V(x)<<V(k)<<V(nsx)<<V(nsy));

		// avg should be (0 + k) / 2
		if (nsx * 2 == ns * k && nsy * 2 == ns * k) ret >?= k + 1;
	    }
	}

	cout << "Case #"<<(tt+1)<<": ";
	if (ret < 3) cout << "IMPOSSIBLE"; else cout << ret;
    end:
	cout<<endl;
    }
    return 0;
}
