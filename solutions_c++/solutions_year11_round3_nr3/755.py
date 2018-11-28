#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int main() {

	int T, N, L, H;

	long long A[10000];
	long long d[10000];
	fstream f, g;

	f.open("harmony.in", fstream::in);
	g.open("harmony.out", fstream::out);
	
	f >> T;
	for (int t = 1; t <= T; t++) {
		
		f >> N >> L >> H;
		
		memset(A, 0, sizeof( A));
		memset(d, 0, sizeof( A));

		for (int i = 0; i < N; i++) {
			f >> A[i];
		}

		bool solved = false;
		for (int i = L; i <= H; i++) {
			bool answer = true;
			for (int j = 0; j < N; j++) {
				if (A[j] <= i && i % A[j] != 0) {
					answer = false;
					break;
				}
				if (A[j] > i && A[j] % i != 0) {
					answer = false;
					break;
				}
			}
			if (answer == true) {
				g << "Case #" << t << ": " << i << endl;  
				solved = true;
				break;
			}
		}
		if (solved == false) 
			g << "Case #" << t << ": NO" << endl;  
	}

	f.close();
	g.close();
}