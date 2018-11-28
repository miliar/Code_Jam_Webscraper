#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <cmath>
using namespace std;
ifstream fin("2C-small.in");
ofstream fout("2C-small.out");

int cases, ships;
int main() {
    fin >> cases;
    for (int i=0;i<cases;i++) {
        long double maxdist=0;
        fin >> ships;
        long double ship[ships][4];
        for (int j=0;j<ships;j++) {
            fin >> ship[j][0] >> ship[j][1] >> ship[j][2] >> ship[j][3];
        }
        for (int k=0;k<ships;k++) {
            for (int l=k;l<ships;l++) {
                long double dist=abs(ship[k][0]-ship[l][0])+abs(ship[k][1]-ship[l][1])+abs(ship[k][2]-ship[l][2]);
                dist/=ship[k][3]+ship[l][3];
                if(dist>maxdist) {
                                 maxdist=dist;
                }
            }
        }
        fout << fixed << setprecision(6) << "Case #" << i+1 << ": " << maxdist << endl;
    }
    return 0;
}

