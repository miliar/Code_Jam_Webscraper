#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

fstream in, out;

int t, r, n, k;

__int64 groups[1000];
__int64 start[1000];
__int64 end[1000];


int main() {
	in.open("prob3.in", fstream::in);
	out.open("prob3.out", fstream::out);

	in >> t;
	int temp;
    for (int i = 0; i < t; i++) {
		in >> r >> k >> n;
		for (int j = 0; j < n; j++) {
			in >> temp;
			groups[j] = temp;
		}
		int counter;
		for (int x = 0; x < n; x++) {
			start[x] = 0;
			counter = k;
			int up = 0;
			while (counter >= 0 && up <= n) {
				if (up == n) {
					end[x] = ((x + up + n) % n);
					counter = -1;
				} else if (groups[((x + up) % n)] <= counter) {
					counter -= groups[((x + up) % n)];
					start[x] += groups[((x + up) % n)];
					up++;
				} else {
					end[x] = ((x + up + n) % n);
					counter = -1;
				}
			}
		}
		
		__int64 ans = 0;
		int curr = 0;
		for (int y = 0; y < r; y++) {
			ans += start[curr];
			curr = end[curr];
		}

		char asdf[30];
		_i64toa( ans, asdf, 10 );


		out << "Case #" << i + 1 << ": ";
		out << asdf << endl;
	}
    
	in.close();
	out.close();

	return 0;
}
