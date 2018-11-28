#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

unsigned long int g[1000], g2[1000];
int gnext[1000];

int main() {
	int T, caseno = 1;
	cin >> T;

	while(caseno <= T) {
		unsigned long int R, k, N, E = 0;

		cin >> R >> k >> N;

		for(int i=0; i < N; i++) {
			cin >> g[i];
		}

		for(int i = 0; i < N; i++) {
			int size = g[i], j;
			for(j = (i+1) % N; (j != i) && (size+g[j] <= k); j = (j+1) % N) {
				size += g[j];
			}
			gnext[i] = j;
			g2[i] = size;
		}
	
		int ig = 0;
		for(int i = 0; i < R; i++) {
			E += g2[ig];
			ig = gnext[ig];
		}

		cout << "Case #" << caseno << ": " << E << endl;

		caseno++;
	}
	return 0;
}
