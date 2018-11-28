#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int tc = 0;tc < T; ++tc) {
		int R = 0, C = 0;
		f >> R >> C;
	
		vector<string> p (R);
		for (int i = 0; i < R; ++i)
			f >> p[i];

		bool isok = true;
		for (int i = 0; i < R; ++i) {
			for (int j = 0; j < C; ++j) {
				if (p[i][j] == '#') {
					if (i == R-1) { isok = false; break; }
					if (j == C-1) { isok = false; break; }
					if (p[i][j] == '#' && p[i][j+1] == '#' && p[i+1][j] == '#' && p[i+1][j+1] == '#') {
						p[i][j] = '/';
						p[i][j+1] = '\\';
						p[i+1][j] = '\\';
						p[i+1][j+1] = '/';
					} else {
						isok = false; break;
					}
				}
			}
			if (!isok) break;
		}
				
		cout << "Case #" << tc+1 << ": " << endl;
		of << "Case #" << tc+1 << ": " << endl;
		if (!isok) {
			cout << "Impossible" << endl;
			of <<  "Impossible" << endl;
		} else {
			for (int i = 0; i < R; ++i) {
				cout << p[i] << endl;
				of << p[i] << endl;
			}
		}
		//of << "Case #" << tc+1 << ": " << res << endl;
	}
	f.close();
	of.close();
	cin.get();
}