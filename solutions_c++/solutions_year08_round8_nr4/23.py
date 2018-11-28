# include <cstdio>
# include <cstdlib>
# include <set>
# include <map>
# include <vector>
# include <algorithm>
# include <cmath>
# include <fstream>
# include <iomanip>
# include <sstream>
# include <string>
# include <iostream>

using namespace std;

ifstream fin ("input.txt");
ofstream fout ("output.txt");

int cnt [2][1 << 10];

int main () {


	int tests;

	fin >> tests;

	for (int test = 1; test <= tests; ++ test) {
	
		int n, k, p;

		fin >> n >> k >> p;
	
		memset (cnt, 0, sizeof (cnt));

		cnt [0][(1 << (k)) - 1] = 1;

		int curr = 0;

		for (int i = 0; i < n - k; ++ i) {
		
			memset (cnt [1 - curr], 0, sizeof (cnt [1 - curr]));

			for (int j = 0; j < (1 << p) ; ++ j)
				if (j & 1)
					if (cnt [curr][j] != 0){
					
						for (int q = 0; q < p; ++ q)
							if (((j >> 1) & (1 << q)) == 0) {
							
								(cnt [1 - curr][(j >> 1) + (1 << q)] += cnt [curr][j]) %= 30031;

 							}
					}

			curr = 1 - curr;
		}

		int res = cnt [curr][(1 << (k)) - 1];
	
		fout << "Case #" << test << ": " << res << endl;
	}

	return 0;
}
