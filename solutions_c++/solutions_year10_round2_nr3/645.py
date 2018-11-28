#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

fstream in, out;

int t, n;

int binom[501][501];
int vals[501][501];

int ans;

int main() {
	in.open("prob3.in", fstream::in);
	out.open("prob3.out", fstream::out);

	in >> t;

	binom[0][0] = 1;
	for (int ii = 0; ii < 501; ii++) {
		binom[ii][0] = 1;
		binom[ii][ii] = 1;
		for (int jj = 1; jj < ii; jj++) {
			binom[ii][jj] = ((binom[ii-1][jj-1] + binom[ii-1][jj]) % 100003);
		}
	}

	for (int x = 0; x < 501; x++) {
		vals[x][0] = 0;
		vals[x][1] = 1;
		for (int y = 2; y < x; y++) {
			vals[x][y] = 0;
			for (int z = 0; z <= y-2; z++) {
				vals[x][y] = (vals[x][y] + vals[y][z+1] * binom[x - y - 1][y - z - 2]) % 100003;
			}
		}
	}

    for (int i = 0; i < t; i++) {
		in >> n;
		ans = 0; 
		
		for (int j = 1; j < n; j++) {
			ans = (ans + vals[n][j]) % 100003;
		}


		out << "Case #" << i + 1 << ": ";
		out << ans << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
