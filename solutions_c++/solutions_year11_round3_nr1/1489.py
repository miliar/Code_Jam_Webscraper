#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

#include <math.h>

using namespace std;

void Replace(int &j, int &k, vector<vector<string>> &t)
{
	t[j][k] = "/";
	t[j][k+1] = "\\";
	t[j+1][k] = "\\";
	t[j+1][k+1] = "/";
}

int main(void)
{
	ifstream cin("R1C-A-large.in");
	ofstream ofs("R1C-A-largeO.txt");
	//ifstream cin("R1test.txt");
	//ofstream ofs("R1testO.txt");
	int T, R, C;
	bool red;
	vector<vector<string>> tiles;
	
	cin >> T;
	for (int i = 0; i < T; i++) {
		R = 0;
		red = false;
		C = 0;
		tiles.clear();
		cin >> R >> C;
		cin.ignore();

		tiles.resize(R);
		for (int j = 0; j < R; j++)
			tiles[j].resize(C);

		// load
		for (int j = 0; j < R; j++) {
			string str;
			getline(cin, str);
			for (int k = 0; k < C; k++)
				tiles[j][k] = str[k];
		}

		for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++) {
				if (k != C - 1 && tiles[j][k] == "#" && tiles[j][k+1] == "#")
					if (j != R - 1 && tiles[j+1][k] == "#" && tiles[j+1][k+1] == "#") {
						Replace(j, k, tiles);
					}
			}
		}

		//for (int j = 0; j < R; j++) {
			/*vector<vector<string>>::iterator it = find(tiles.begin(), tiles.end(), "#");
			if (it != tiles.end()) red = false;
			else red = true;
		//}*/


		for (int j = 0; j < R; j++) {
			vector<string>::iterator it = find(tiles[j].begin(), tiles[j].end(), "#");
			if (it != tiles[j].end()) {
				red = false;
				break;
			}

			else red = true;
		}/**/
		/*for (int j = 0; j < R; j++) {
			for (int k = 0; k < C; k++)
				ofs << tiles[j][k] << flush;
			ofs << endl;
		}*/

		ofs << "Case #" << i + 1 << ":" << endl;
		if (!red) ofs << "Impossible" << endl;
		else {
			for (int j = 0; j < R; j++) {
				for (int k = 0; k < C; k++)
					ofs << tiles[j][k] << flush;
				ofs << endl;
			}
		}
	}

	return 0;
}