#include <iostream>
using namespace std;

int main() {
	int i, j, k;
	int c;
	int t;
	int r;
	int x1, y1, x2, y2;
	bool cell[101][101];
	int time;
	int n;
	int maxX, maxY;

	cin >>c;
	for (t=1; t<=c; t++) {
		cin >>r;
		for (i=0; i<101; i++) for (j=0; j<101; j++) cell[j][i] = 0;
		time = 0;
		n = 0;
		maxX = maxY = 0;

		for (k=0; k<r; k++) {
			cin >>x1 >>y1 >>x2 >>y2;
			for (j=y1; j<=y2; j++) {
				for (i=x1; i<=x2; i++) {
					cell[j][i] = 1;
					++n;
				}
			}
			if (x2 > maxX) maxX = x2;
			if (y2 > maxY) maxY = y2;
		}

		while (n != 0) {
			++time;
			for (j=maxY; j>0; j--) {
				for (i=maxX; i>0; i--) {
					if (cell[j][i] == 1) {
						if (cell[j-1][i] == 0 && cell[j][i-1] == 0) {
							cell[j][i] = 0;
							--n;
						}
					} else {
						if (cell[j-1][i] == 1 && cell[j][i-1] == 1) {
							cell[j][i] = 1;
							++n;
						}
					}
				}
			}
		}

		cout <<"Case #" <<t <<": " <<time <<endl;
	}

	return 0;
}