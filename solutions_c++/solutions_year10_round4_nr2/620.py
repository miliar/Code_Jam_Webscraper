#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int M[1024];
int C[10][1024];
int W[10][1024];
int V[10][1024];
int P;

int solve()
{
	cin >> P;
	
	int ret = 0;
	
	memset(M, 0, sizeof(M) );
	memset(C, 0, sizeof(C) );
	memset(V, 0, sizeof(V) );
	
	for (int i = 0; i < (1 << P); ++i) {
		cin >> M[i];
		M[i] = P - M[i];
		//printf("M[%d] = %d\n", i, M[i]);
	}
	for (int i = 0; i < P; ++i) {
		for (int j = 0; j < (1 << (P - i - 1) ); ++j) {
			cin >> C[i][j];
		}
	}
	
	bool ok;
	int maxw, maxj, maxx;
	while (1) {
		ok = true;
		memset(W, 0, sizeof(W) );
		maxw = 0;
		for (int i = 0; i < (1 << P); ++i) {
			if (M[i] > 0) {
				int x = i;
				for (int j = 0; j < P; ++j) {
					x >>= 1;
					++W[j][x];
					if (V[j][x] == 0 && maxw < W[j][x]) {
						maxw = W[j][x];
						maxj = j;
						maxx = x;
					}
				}
			}
		}
		if (maxw == 0) return ret;
		++ret;
		V[maxj][maxx] = 1;
		//printf("View - %d, %d, %d (%d, %d)\n", maxw, maxj, maxx, maxx << maxj, (maxx + 1) << maxj);
		
		for (int i = maxx << (maxj + 1); i < (maxx + 1) << (maxj + 1); ++i) {
			--M[i];
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
