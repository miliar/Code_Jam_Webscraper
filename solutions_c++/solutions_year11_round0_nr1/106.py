#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open(argv[1]);
	int T;
	f >> T;
	for (int i=0; i<T; i++) {
		int N;
		f >> N;
		int* v = new int[N];
		for (int j=0; j<N; j++) {
			char c;
			int w;
			f >> c >> w;
			if (c == 'O')  v[j] = w;
			else v[j] = -w;
		}
		int x = 1;
		int y = 1;
		int tx = 0;
		while (tx <= N-1 && v[tx] < 0) tx++;		
		int ty = 0;
		while (ty <= N-1 && v[ty] > 0) ty++;		
		int b = 0;
		int step = 0;
		while (b < N) {
			bool p = (v[b] > 0);
			if (tx != N) {
				if (x < v[tx]) x++;
				else if (x > v[tx]) x--;
				else if (p) {
					b += 1;
					tx++;
					while (tx <= N-1 && v[tx] < 0) tx++;
				}
			}
			if (ty != N) {
				if (y < -v[ty]) y++;
				else if (y > -v[ty]) y--;
				else if (p == false) {
					b += 1;
					ty++;
					while (ty <= N-1 && v[ty] > 0) ty++;
				}
			}
			step++;
		}
		cout << "Case #" << i+1 << ": " << step << endl; 
	}
	f.close();
}
