#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int main() {

	int T, N, M;
	char c;
	
	char A[50][50];

	fstream f, g;

	f.open("sqtiles.in", fstream::in);
	g.open("sqtiles.out", fstream::out);
	
	f >> T;
	for (int t = 1; t <= T; t++) {
		f >> N >> M;
		memset(A, 0, sizeof( A));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				f >> c;
				A[i][j] = c;
			}
		}

		bool answer;
		
		answer = true;
		for (int i = 0; i < N && answer; i++) {
			for (int j = 0; j < M && answer; j++) {
				if (A[i][j] == '#') {
					if (i + 1 >= N || j + 1 >= M) {
						answer = false;
						break;	
					}

					if (A[i + 1][j] != '#' || A[i + 1][j + 1] != '#' || A[i][j + 1] != '#') {
						answer = false;
						break;
					}

					A[i][j] = '/';
					A[i][j + 1] = '\\';
					A[i + 1][j] = '\\';
					A[i + 1][j + 1] = '/';				
				}
			}
		}

		if (answer == false) {
			g << "Case #" << t << ":" << endl; 
			g << "Impossible" << endl;
		} else {
			g << "Case #" << t << ":" << endl; 
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					g << A[i][j];
				}
				g << endl;
			}
		}
	}
	return 0;
}