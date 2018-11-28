#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("B-large.out");

int main() {
    int cases;
    fin >> cases;
    for (int i=0;i<cases;i++) {
      int x, y;
      fin >> x >> y;
      int alts[x][y];
      char basins[x][y];
      char curbasin = 'a';
      queue<int> dijk;
      for (int ix=0;ix<x;ix++) {
        for (int iy=0;iy<y;iy++) {
          fin >> alts[ix][iy];
          basins[ix][iy] = '0';
        }
      }
      
      for (int ix=0;ix<x;ix++) {
        for (int iy=0;iy<y;iy++) {
          if (basins[ix][iy] == '0') {
            basins[ix][iy] = curbasin;
            // flow into
            int minx = ix;
            int miny = iy;
            int myalt = alts[ix][iy];
            if (ix > 0 && alts[ix-1][iy] < myalt && alts[ix-1][iy] < alts[minx][miny]) {
              minx = ix-1;
              miny = iy;
            }
            if (iy > 0 && alts[ix][iy-1] < myalt && alts[ix][iy-1] < alts[minx][miny]) {
              minx = ix;
              miny = iy-1;
            }
            if (iy < y-1 && alts[ix][iy+1] < myalt && alts[ix][iy+1] < alts[minx][miny]) {
              minx = ix;
              miny = iy+1;
            }
            if (ix < x-1 && alts[ix+1][iy] < myalt && alts[ix+1][iy] < alts[minx][miny]) {
              minx = ix+1;
              miny = iy;
            }
            if (minx != ix || miny != iy) {
              basins[minx][miny] = curbasin;
              dijk.push(minx);
              dijk.push(miny);
            }
            
            //flow into me
            if (ix > 0 && alts[ix-1][iy] > myalt && basins[ix-1][iy] == '0') {
              dijk.push(ix-1);
              dijk.push(iy);
            }
            if (iy > 0 && alts[ix][iy-1] > myalt && basins[ix][iy-1] == '0') {
              dijk.push(ix);
              dijk.push(iy-1);
            }
            if (ix < x-1 && alts[ix+1][iy] > myalt && basins[ix+1][iy] == '0') {
              dijk.push(ix+1);
              dijk.push(iy);
            }
            if (iy < y-1 && alts[ix][iy+1] > myalt && basins[ix][iy+1] == '0') {
              dijk.push(ix);
              dijk.push(iy+1);
            }
            
            //check all possibilities
            while(!dijk.empty()) {
              int testx = dijk.front();
              dijk.pop();
              int testy = dijk.front();
              dijk.pop();
              // flow into
              minx = testx;
              miny = testy;
              myalt = alts[testx][testy];
              if (testx > 0 && alts[testx-1][testy] < myalt && alts[testx-1][testy] < alts[minx][miny]) {
                minx = testx-1;
                miny = testy;
              }
              if (testy > 0 && alts[testx][testy-1] < myalt && alts[testx][testy-1] < alts[minx][miny]) {
                minx = testx;
                miny = testy-1;
              }
              if (testy < y-1 && alts[testx][testy+1] < myalt && alts[testx][testy+1] < alts[minx][miny]) {
                minx = testx;
                miny = testy+1;
              }
              if (testx < x-1 && alts[testx+1][testy] < myalt && alts[testx+1][testy] < alts[minx][miny]) {
                minx = testx+1;
                miny = testy;
              }
              if (minx != testx || miny != testy) {
                if (basins[minx][miny] == curbasin) {
                  basins[testx][testy] = curbasin;
                } else if (basins[testx][testy] == curbasin) {
                  basins[minx][miny] = curbasin;
                  dijk.push(minx);
                  dijk.push(miny);
                }
              }
              if (basins[testx][testy] == curbasin) {
                //flow into me
                if (testx < x-1 && alts[testx+1][testy] > myalt && basins[testx+1][testy] == '0') {
                  dijk.push(testx+1);
                  dijk.push(testy);
                }
                if (testy > 0 && alts[testx][testy-1] > myalt && basins[testx][testy-1] == '0') {
                  dijk.push(testx);
                  dijk.push(testy-1);
                }
                if (testy < y-1 && alts[testx][testy+1] > myalt && basins[testx][testy+1] == '0') {
                  dijk.push(testx);
                  dijk.push(testy+1);
                }
                if (testx > 0 && alts[testx-1][testy] > myalt && basins[testx-1][testy] == '0') {
                  dijk.push(testx-1);
                  dijk.push(testy);
                }
              }
            }
            curbasin++;
          }
        }
      }
			fout << "Case #" << i+1 << ":\n";
			
			for (int ix=0;ix<x;ix++) {
				fout << basins[ix][0];
				for (int iy=1;iy<y;iy++) {
					fout << " " << basins[ix][iy];
				}
				fout << endl;
			}
    }
    return 0;
}

