#include <cstdlib>
#include <iostream>
#include <fstream>
#include <list>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{
	int i, j, k;
	ifstream inputfile("data.in");
	ofstream outputfile("data.out");
	int casesCount;
	inputfile >> casesCount;
	char picture[50][50];
	int R = 1, C = 1;
	for(i = 0; i < casesCount; i++) {
		inputfile >> R >> C;
		for(int r = 0; r < R; r++){
			for(int c = 0; c < C; c++){
				inputfile >> picture[r][c];
			}
			if((r > 0) && (C > 0)){
				for(j = 1; j < C; j++){
					if((picture[r-1][j-1] == '#') && (picture[r-1][j] == '#') &&
						(picture[r][j-1] == '#') && (picture[r][j] == '#')){
							picture[r-1][j-1] = '/';
							picture[r-1][j] = '\\';
							picture[r][j-1] = '\\';
							picture[r][j] = '/';
					}
				}
			}
		}
		outputfile << "Case #" << i + 1 << ":" << endl;
		bool impossible = false;
		for(int r = 0; r < R; r++){
			for(int c = 0; c < C; c++){
				if(picture[r][c] == '#'){
					impossible = true;
					break;
				}
			}
		}
		if(!impossible)
		for(int r = 0; r < R; r++){
			for(int c = 0; c < C; c++){
				outputfile << picture[r][c];
			}
			outputfile << endl;
		}
		else
			outputfile << "Impossible" << endl;
	}
	inputfile.close();
	outputfile.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
