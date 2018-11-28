#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int tc = 0; tc < T; ++tc) {
		int N = 0, L = 0, H = 0;
		f >> N >> L >> H;

		vector<int> sounds (N);
		for (int i = 0; i < N; ++i) {
			f >> sounds[i];
		}

		int i = L;
		for (; i <= H; ++i) {
			bool isok = true;
			for (int j = 0; j < N; ++j) {
				if (sounds[j] % i != 0 && i % sounds[j] != 0) {
					isok = false;
					break;
				}
			}
			if (isok) break;
		}
	
		if (i == H+1) {
			cout << "Case #" << tc+1 << ": NO" << endl;
			of << "Case #" << tc+1 << ": NO" << endl;
		} else {
			cout << "Case #" << tc+1 << ": " << i << endl;
			of << "Case #" << tc+1 << ": " << i << endl;
		}
			 
	}
	f.close();
	of.close();
	cin.get();
}