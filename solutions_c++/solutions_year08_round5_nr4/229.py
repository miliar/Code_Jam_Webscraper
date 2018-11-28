#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int P;
int N;
int W;
int H;
int R;
int K;
bool possible;

int maxH, maxW;

int** numTimes;

int main() {
	fstream in;
	fstream out;
	in.open("prob4.in", fstream::in);
	out.open("prob4.out",fstream::out);

	P = 10007;

	in >> N;
	for (int a = 0; a < N; a++) {
		in >> H;
		in >> W;
		in >> R;

		possible = true;
		if ((W + H - 2) % 3 != 0 || H > 2 * W - 1 || W > 2 * H - 1) {
			possible = false;
		}
	
		K = (W + H - 2)/3;
		int ans;
		
		if (possible) {
			maxH = (2*H - W - 1)/3;
			maxW = (2*W - H - 1)/3;
			maxH++;
			maxW++;

			numTimes = new int*[maxH];
			for (int c = 0; c < maxH; c++) {
				numTimes[c] = new int[maxW];
			}
			for (int d = 0; d < maxH; d++) {
				for (int e = 0; e < maxW; e++) {
					numTimes[d][e] = 0;
				}
			}

			int h1, w1, newH, newW;
			for (int b = 0; b < R; b++) {
				in >> h1 >> w1;
				if ((h1 + w1 - 2) % 3 == 0 && h1 <= 2 * w1 - 1 && w1 <= 2 * h1 - 1) {
					newH = (2*h1 - w1 - 1)/3;
					newW = (2*w1 - h1 - 1)/3;
					if (newH <maxH && newW < maxW) {
						numTimes[newH][newW] = -1;
					}
				}
			}

			numTimes[0][0] = 1;
			for (int i = 0; i < maxH; i++) {
				for (int j = 0; j < maxW; j++) {
					if (numTimes[i][j] != -1) {
						if (i > 0 && numTimes[i-1][j] != -1) {
							numTimes[i][j] += numTimes[i-1][j];
						}
						if (j > 0 && numTimes[i][j-1] != -1) {
							numTimes[i][j] += numTimes[i][j-1];
						}
						numTimes[i][j] = numTimes[i][j] % P;
					}
				}
			}
			ans = numTimes[maxH-1][maxW-1];
		} else {
			int x1, y1;
			for (int bb = 0; bb < R; bb++) {
				in >> x1 >> y1;
			}
		}

		if (possible) {
			out << "Case #" << a+1 << ": " << ans << endl;
		} else {
			out << "Case #" << a+1 << ": " << 0 << endl;
		}	
	}
	
	in.close();
	out.close();
	return 0;
}