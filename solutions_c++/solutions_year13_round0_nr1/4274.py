#include <iostream>
#include <string>
#include <fstream>
using namespace std;
string map[4];
int xRow[4], xColumn[4], xslap[2], yRow[4], yColumn[4], yslap[2];
int main(){
	int T, t = 0, flag1, flag2; string tmp;
	ifstream fin("A-large.in");
	fin >> T;
	ofstream os("data.txt");
	while (flag1 = flag2 = 0, ++t <= T){
		for (int i = 0; i < 4; ++i) xRow[i] = yRow[i] = xColumn[i] = yColumn[i] = 0;
		for (int i = 0; i < 2; ++i) xslap[i] = yslap[i] = 0;
		for (int i = 0; i < 4; ++i) fin >> map[i];
		fin.ignore(); getline(fin, tmp);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j){
				switch(map[i][j]){
				case 'X': ++xRow[j]; ++xColumn[i]; break;
				case 'O': ++yRow[j]; ++yColumn[i]; break;
				case 'T': ++xRow[j]; ++xColumn[i]; ++yRow[j]; ++yColumn[i]; break;
				case '.': flag1 = 1; break;
				}
				if (i == j && map[i][j] == 'X') ++xslap[0];
				if (i == j && map[i][j] == 'O') ++yslap[0];
				if (i == j && map[i][j] == 'T'){++xslap[0]; ++yslap[0];}
				if (((i == 0 && j == 3) || (i == 1 && j == 2) || (i == 2 && j == 1) || (i == 3 && j == 0)) && map[i][j] == 'X') ++xslap[1];
				if (((i == 0 && j == 3) || (i == 1 && j == 2) || (i == 2 && j == 1) || (i == 3 && j == 0)) && map[i][j] == 'O') ++yslap[1];
				if (((i == 0 && j == 3) || (i == 1 && j == 2) || (i == 2 && j == 1) || (i == 3 && j == 0)) && map[i][j] == 'T'){++xslap[1]; ++yslap[1];}
			} os << "Case #" << t << ": ";
			for (int i = 0; i < 4; ++i){
				if (xRow[i] == 4 || xColumn[i] == 4) {os << "X won" << endl; flag2 = 1; break;}
				else if (yRow[i] == 4 || yColumn[i] == 4) {os << "O won" << endl; flag2 = 1; break;}
			}
			if (!flag2){
				if (xslap[0] == 4 || xslap[1] == 4){os << "X won" << endl; flag2 = 1;}
				if (yslap[0] == 4 || yslap[1] == 4){os << "O won" << endl; flag2 = 1;}
			}
			if (!flag2 && flag1) os << "Game has not completed" << endl;
			if (!flag2 && !flag1) os << "Draw" << endl;
	}
	os.close();
	return 0;
}