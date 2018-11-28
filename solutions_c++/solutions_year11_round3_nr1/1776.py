#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#define MAX 100
using namespace std;

int main() {
	
	ifstream fin ("acinput.txt");
	ofstream fout ("acoutput.txt");
	
	int T, R, C, blue =0;
	char pic[MAX][MAX] = {0};
	int mx[] = {1, 1, 0}, my[] = {0, 1, 1};
	char temp;
	char p[] = {char(92), '/', char(92)};
	bool cont = true;
	
	fin >> T;
	
	for (int i=0; i<T; i++) {
		fin >> R >> C;
		for (int j=0; j<R; j++) {
			for (int k=0; k<C; k++) {
				fin >> temp;
				pic[j][k] = temp;
				if (int(temp) == 35)
					blue++;
			}
		}
		if (blue % 4 != 0){
			fout << "Case #" << i + 1 << ":" << endl;
			fout << "Impossible" << endl;
		}
		else if (blue == 0){
			fout << "Case #" << i + 1 << ":" << endl;
			for (int jj=0; jj<R; jj++) {
				for (int kk=0; kk<C; kk++) {
					fout << pic[jj][kk];
				}
				fout << endl;
			}
		}
		else {
			cont = true;
			for (int j=0; j<R && cont; j++) {
				for (int k=0; k<C && cont; k++) {
					if (pic[j][k] == '#'){
						pic[j][k] = '/';
						for (int ii=0; ii<3; ii++) {
							if (pic[j+my[ii]][k+mx[ii]] == '#'){
								pic[j+my[ii]][k+mx[ii]] = p[ii];
							}
							else {
								cont = false;
								break;
							}
						}
					}
				}
			}
			if (cont){
				fout << "Case #" << i + 1 << ":" << endl;
				for (int j=0; j<R; j++) {
					for (int k=0; k<C; k++) {
						fout << pic[j][k];
					}
					fout << endl;
				}
			}
			else {
				fout << "Case #" << i + 1 << ":" << endl;
				fout << "Impossible" << endl;
			}

		}

		blue = 0;
		char pic[MAX][MAX] = {0};
	}

	return 0;
}