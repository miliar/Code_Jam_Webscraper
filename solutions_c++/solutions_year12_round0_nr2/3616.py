#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream ifs(argv[1]);
	ofstream ofs("output");

	int T, N, S, p, t, y;
	ifs >> T;

	int c, o, mx;

	for (int i = 1; i <= T; ++i) {
		y = 0;
		ifs >> N >> S >> p;

		for (int j = 0; j < N; ++j) {
			ifs >> t;
			mx = c = t / 3;
			o = t % 3;

			switch (o) {
			case 0: mx=c+1; break;
			case 1: c+=1; mx=c; break;
			case 2: c+=1; mx=c+1; break;
			}			
			 				
			if (c >= p) y++;
			else if (S>0 && mx>=p && t>1) { y++; S--; }
		}
            
		ofs << "Case #" << i << ": " << y << endl;
	}

	ifs.close();
	ofs.close();
	return 0;
}
