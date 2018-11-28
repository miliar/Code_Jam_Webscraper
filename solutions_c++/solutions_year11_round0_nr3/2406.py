#include <fstream>
#include <vector>
#include <math.h>
#include <stdlib.h>

using namespace std;

int main() {
	
	int T, N;
	
	long long digit, min, sum;
	long long count[20];

	fstream f, g;
	f.open("candies.in", fstream::in);
	g.open("candies.out", fstream::out);
	
	f >> T;
	
	for (int t = 1; t <= T;	t++) {
		f >> N;
		memset(count, 0, 20 * sizeof(long ));
		sum = 0;
		min = 2000000;
		for (int n = 0; n < N; n++) {
			f >> digit;
			if (digit < min) min = digit;
			sum += digit;
			int i = 0;
			while (i < 20) {
				if (digit % 2 == 1) count[i]++;
				digit /= 2;
				i++;
			}
		}
		bool answer = true;
		for (int i = 0; i < 20; i++)
			if (count[i] % 2 == 1) {
				answer = false;
				break;
			}
		if (answer == false) {
			g << "Case #" << t << ": NO" << endl;
		} else {
			g << "Case #" << t << ": " << sum - min << endl;
		}


	}

	f.close();
	g.close();
	
	return 0;
}