//#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <list>
#include <algorithm>
#include <math.h>


using namespace std;
using std::string;


ifstream fin("B-large.in");
ofstream fout("output.txt");

int numMaps;
int h;
int w;

typedef struct Basin
{
	int hh;
	int ww;
	int num;
};

int main()
{
	int i, j, k;
	
	int cells[100][100];
	Basin basins[100][100];
	
	fin >> numMaps;
	
	for (i = 0; i < numMaps; i++) {
		fin >> h >> w;
		
		for (j = 0; j < h; j++) {
			for (k = 0; k < w; k++) {
				fin >> cells[j][k];
				basins[j][k].hh = j;
				basins[j][k].ww = k;
				basins[j][k].num = 0;
				
				//cout << cells[j][k] << " ";
			}
			//cout << "\n";
		}
		
		int lat;
		Basin flowto;
		
		for (j = 0; j < h; j++) {
			for (k = 0; k < w; k++) {
				lat = cells[j][k] - 1;
				flowto.hh = j;
				flowto.ww = k;
				
				if (j < h-1) {	// south
					if (cells[j+1][k] <= lat) {
						flowto.hh = j+1;
						flowto.ww = k;
						lat = cells[j+1][k];
					}
				}
				if (k < w-1) {	// east
					if (cells[j][k+1] <= lat) {
						flowto.hh = j;
						flowto.ww = k+1;
						lat = cells[j][k+1];
					}
				}
				if (k > 0) {	// west
					if (cells[j][k-1] <= lat) {
						flowto.hh = j;
						flowto.ww = k-1;
						lat = cells[j][k-1];
					}
				}
				if (j > 0) {	// north
					if (cells[j-1][k] <= lat) {
						flowto.hh = j-1;
						flowto.ww = k;
						lat = cells[j-1][k];
					}
				}
				
				//cout << flowto.hh << " . " << flowto.ww << endl;
				
			
				
				basins[j][k] = flowto;
				basins[j][k].num = 0;
				
				
			}
		}
		
		int jj, kk, tempjj, tempkk;
		
		for (j = 0; j < h; j++) {
			for (k = 0; k < w; k++) {
				jj = j;
				kk = k;
				
				//if (j == 2 && k == 0) 
				//	cout << basins[j][k].hh << " . " << basins[j][k].ww << endl;
					
				while (jj != basins[jj][kk].hh || kk != basins[jj][kk].ww) {
					tempjj = basins[jj][kk].hh;
					tempkk = basins[jj][kk].ww;
					jj = tempjj;
					kk = tempkk;
				}
				
				basins[j][k].hh = jj;
				basins[j][k].ww = kk;
				
				//cout << jj << "-" << kk << "  ";
			}
			//cout << "\n";
		}
		
		int numbasins = 0;
		for (j = 0; j < h; j++) {
			for (k = 0; k < w; k++) {
				if (basins[basins[j][k].hh][basins[j][k].ww].num == 0) {
					numbasins++;
					basins[basins[j][k].hh][basins[j][k].ww].num = numbasins;
				}
			}
		}
		
		//cout << "# basins: " << numbasins << endl;
	
		for (j = 0; j < h; j++) {
			for (k = 0; k < w; k++) {
				basins[j][k].num = basins[basins[j][k].hh][basins[j][k].ww].num;
			}
		}
		
		fout << "Case #" << i+1 << ":" << endl;
		for (j = 0; j < h; j++) {
			for (k = 0; k < w; k++) {
				if (k > 0) {
					fout << " ";
				}
				fout << (char) (basins[j][k].num + 96);
			}
			fout << "\n";
		}
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
