#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

#define SIZE	500

char B[SIZE][SIZE];

int count()
{
	for (int i = 0; i < SIZE; ++i) {
		for (int j = 0; j < SIZE; ++j) {
			if (B[i][j]) return 1;
		}
	}
	return 0;
}

int solve()
{
	int R;
	int ret = 0;
	
	memset(B, 0, sizeof(B) );
	cin >> R;
	int x1, x2, y1, y2;
	int xx1, xx2, yy1, yy2;
	xx1 = yy1 = 1000000;
	xx2 = yy2 = 0;
	for (int i = 0; i < R; ++i) {
		cin >> x1 >> y1 >> x2 >> y2;
		xx1 = min(xx1, x1);
		xx2 = max(xx2, x2);
		yy1 = min(yy1, y1);
		yy2 = max(yy2, y2);
		for (int x = x1; x <= x2; ++x) {
			for (int y = y1; y <= y2; ++y) {
				B[x][y] = 1;
			}
		}
	}
	
	for (int ret = 0; ; ++ret) {
		if (count() == 0) return ret;
		++xx2;
		++yy2;
		if (xx2 >= SIZE || yy2 >= SIZE) break;
		for (int x = xx2; x >= xx1; --x) {
			for (int y = yy2; y >= yy1; --y) {
				if (B[x][y] && B[x - 1][y] == 0 && B[x][y - 1] == 0) B[x][y] = 0;
				else if (B[x][y] == 0 && B[x - 1][y] == 1 && B[x][y - 1] == 1) B[x][y] = 1;
			}
		}
	}
	
	fprintf(stderr, "ERROR>>>\n");
	return -1;
}

int main(int argc, char *argv[])
{
    int T;
    
    cin >> T;
    
    for (int i = 1; i <= T; ++i) {
		printf("Case #%d: %d\n", i, solve() );
	}
	
    return EXIT_SUCCESS;
}
