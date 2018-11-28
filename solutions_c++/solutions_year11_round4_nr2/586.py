#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

double Sum[500][500], SumX[500][500], SumY[500][500]; // For C
pair< double, double > Pmass[500][500], PmassX[500][500], PmassY[500][500]; // For P
int mass[500][500];

int getSolution(void) {
	int R, C, D;
	scanf("%d %d %d", &R, &C, &D);
	int maxK = min(R, C);
	int ret = -1;
	
	for (int i = 0; i < R; i++) {
		char tmp[510];
		scanf("%s", tmp);
		for (int j = 0; j < C; j++) {
			mass[i][j] = (int)(tmp[j] - '0') + D;
		}
	}
	
	
	for (int sy = 0; sy <= R - 1; sy++) {
		for (int sx = 0; sx <= C - 2; sx++) {
			SumX[sy][sx] = mass[sy][sx] + mass[sy][sx + 1];
			PmassX[sy][sx] = make_pair(mass[sy][sx] * sy + mass[sy][sx + 1] * sy,
				mass[sy][sx] * sx + mass[sy][sx + 1] * (sx + 1));
		}
	}
	for (int sy = 0; sy <= R - 2; sy++) {
		for (int sx = 0; sx <= C - 1; sx++) {
			SumY[sy][sx] = mass[sy][sx] + mass[sy + 1][sx];
			PmassY[sy][sx] = make_pair(mass[sy][sx] * sy + mass[sy + 1][sx] * (sy + 1),
				mass[sy + 1][sx] * sx + mass[sy][sx] * sx);
		}					
	}
	for (int sy = 0; sy <= R - 2; sy++) {
		for (int sx = 0; sx <= C - 2; sx++) {
			Pmass[sy][sx] = make_pair(PmassX[sy][sx].first + PmassX[sy + 1][sx].first,
				PmassX[sy][sx].second + PmassX[sy + 1][sx].second);
			Sum[sy][sx] = SumX[sy][sx] + SumX[sy + 1][ sx];
		}
	}

	for (int i = 3; i <= maxK; i++) {
		for (int sy = 0; sy <= R - 1; sy++) {
			for (int sx = 0; sx <= C - i; sx++) {
				SumX[sy][sx] += mass[sy][sx + i - 1];
				PmassX[sy][sx] = make_pair(PmassX[sy][sx].first + mass[sy][sx + i - 1] * sy,
					PmassX[sy][sx].second + mass[sy][sx + i - 1] * (sx + i - 1));
			}
		}
		for (int sy = 0; sy <= R - i; sy++) {
			for (int sx = 0; sx <= C - 1; sx++) {
				SumY[sy][sx] += mass[sy + i - 1][sx];
				PmassY[sy][sx] = make_pair(PmassY[sy][sx].first + mass[sy + i - 1][sx] * (sy + i - 1),
					PmassY[sy][sx].second + mass[sy + i - 1][sx] * sx);
			}				
		}
		for (int sy = 0; sy <= R - i; sy++) {
			for (int sx = 0; sx <= C - i; sx++) {
				int lx = sx, rx = sx + i - 1;
				int ly = sy, ry = sy + i - 1;
				double cx = (lx + rx) / 2.0;
				double cy = (ly + ry) / 2.0;

				Sum[sy][sx] += SumX[ry][sx] + SumY[sy][rx] - mass[ry][rx];
				Pmass[sy][sx] = make_pair(Pmass[sy][sx].first + PmassX[ry][sx].first 
					+ PmassY[sy][rx].first - (ry) * mass[ry][rx]
					, Pmass[sy][sx].second + PmassX[ry][sx].second 
					+ PmassY[sy][rx].second - (rx) * mass[ry][rx]);
					
					
				double pysum = Pmass[sy][sx].first - ly * mass[ly][lx] - ly * mass[ly][rx] - ry * mass[ry][lx] - ry * mass[ry][rx];
				double pxsum = Pmass[sy][sx].second - lx * mass[ly][lx] - rx * mass[ly][rx] - lx * mass[ry][lx] - rx * mass[ry][rx];
				double cysum = cy * (Sum[sy][sx] - mass[ly][lx] - mass[ly][rx] - mass[ry][rx] - mass[ry][lx]);
				double cxsum = cx * (Sum[sy][sx] - mass[ly][lx] - mass[ly][rx] - mass[ry][rx] - mass[ry][lx]);
/*
				double pysum_t = 0, pxsum_t = 0;
				double cysum_t = 0, cxsum_t = 0;
				for (int ty = sy + 1; ty < sy + i - 1; ty++) {
					for (int tx = sx; tx < sx + i; tx++) {
						pysum_t += ty * mass[ty][tx];
						pxsum_t += tx * mass[ty][tx];
						cysum_t += cy * mass[ty][tx];
						cxsum_t += cx * mass[ty][tx];
					}
				}
				for (int tx = sx + 1; tx < sx + i - 1; tx++) {
					pysum_t += sy * mass[sy][tx];
					pxsum_t += tx * mass[sy][tx];
					cysum_t += cy * mass[sy][tx];
					cxsum_t += cx * mass[sy][tx];
				}
				for (int tx = sx + 1; tx < sx + i - 1; tx++) {
					pysum_t += ry * mass[ry][tx];
					pxsum_t += tx * mass[ry][tx];
					cysum_t += cy * mass[ry][tx];
					cxsum_t += cx * mass[ry][tx];
				}

				if ( pysum != pysum_t || cysum != cysum_t || pxsum != pxsum_t || cxsum != cxsum_t) {
					fprintf(stderr, "(%lf %lf %lf %lf) (%lf %lf %lf %lf)\n", pysum, pxsum, cysum, cxsum,
						pysum_t, pxsum_t, cysum_t, cxsum_t);				
				}

*/
				if (pysum - cysum == 0 && pxsum - cxsum == 0) {
					ret = i;
				}				
			}
		}
	}
	return ret;
}

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
		int ans = getSolution();
		if (ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", testcase);
		else 
			printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}