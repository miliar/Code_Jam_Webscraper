#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

#include <math.h>

using namespace std;

int main(void)
{
	ifstream cin("RA-small-attempt2.in");
	ofstream ofs("RA-small-attempt2O.txt");
	//ifstream cin("R1Atest.txt");
	//ofstream ofs("R1AtestO.txt");

	int T, N, Pd, Pg, D;
	bool possible;
	cin >> T;
	for (int i = 0; i < T; i++) {
		N = 0;
		Pd = 0;
		Pg = 0;
		D = 0;
		possible = false;
		cin >> N >> Pd >> Pg;

		// Plausible Pd, N?
		for (int j = 0; j < N; j++) {
			double tmp = (j + 1) * Pd * 1.0 / 100.0;
			if (ceil(tmp) == floor(tmp)) {
				possible = true;
				D = (int)(tmp);
				break;
			}
			//else if (j = N - 1) break;
		}
		
		// Plausible Pg?
		//if (possible && (N * Pg * 1 / 100.0 > N * (int)(Pd * 1 / 100.0))) possible = false;//int E = N * (int)(Pd * 1 / 100.0);
		if (Pg == 100 && Pg > Pd) possible = false;
		else if (Pg  == 0 && Pg < Pd) possible = false;

		//if (i != T - 1) 
			ofs << "Case #" << i + 1 << ": " << (possible ? "Possible" : "Broken") /*<< D << "/"<<E*/ << endl;
		//else ofs << "Case #" << i + 1 << ": " << (possible ? "Possible" : "Broken") << flush;
		
	}


	return 0;
}