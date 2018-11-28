#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

#include <math.h>

using namespace std;
int main(void)
{
	ifstream cin("R1C-C-small-attempt1.in");
	ofstream ofs("R1C-C-small-attempt1O.txt");
	//ifstream cin("R1test.txt");
	//ofstream ofs("R1testO.txt");
	int T, N, L, H, LOW;
	vector<double> notes;
	vector<int> ns;
	vector<bool> hr;
	bool can;
	vector<vector<string>> tiles;
	
	cin >> T;
	for (int i = 0; i < T; i++) {
		N = 0; L = 0; H =0;
		LOW = 0;
		notes.clear();
		hr.clear();
		ns.clear();
		cin >> N >> L >> H;

		notes.resize(N);
		hr.resize(N);
		ns.resize(N);
		for (int j = 0; j < N; j++) {
			//hr[j] = false;
			cin >> notes[j];
		}

		
		/*for (int k = L; k <= H; k++) {
			for (int j = 0; j < N; j++) {
				double tmp = 0;
				//double tmp2 = 0;
				// can devide other's note?
				if (notes[j] > j) tmp = notes[j] / (double)j;
				else tmp = (double)j / notes[j];

				if (ceil(tmp) == floor(tmp)) {
					hr[j] = true;
					continue;
				}
				// can be devided by other's note ?
				//if (ceil(tmp) == floor(tmp))
				//	hr[j] = true;
			}

		}*/
		for (int k = H; k >= L; k--) {
			for (int j = 0; j < N; j++) {
				double tmp = 0;
				//double tmp2 = 0;
				// can devide other's note?
				if (notes[j] > k) tmp = notes[j] / (double)k;
				else tmp = (double)k / notes[j];

				if (ceil(tmp) == floor(tmp)) {
					hr[j] = true;
					
				}
				else
					hr[j] = false;
			}

			vector<bool>::iterator it = find(hr.begin(), hr.end(), false);
			if (it == hr.end()) {// == all true
				can = true;
				LOW = k;
				//break;			// Ç±Ç±Ç≈breakÇµÇΩÇÁç≈í·Ç…Ç»ÇÁÇ»Ç¢Ç∂Ç·ÇÒÅBÅB
			}
			else 
				can = false;
		}
		if (LOW != 0) can = true;

		//for (int j = 0; j < N; j++) {
		
		//}
		// find lowest frequency

		ofs << "Case #" << i + 1 << ": " << flush;
		if (can) ofs << LOW << endl;
		else ofs << "NO" << endl;
	}

	return 0;
}