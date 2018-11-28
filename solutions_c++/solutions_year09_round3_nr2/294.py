#include <iostream>
#include <string>
#include <math.h>

using namespace std;

void doCase(int caseNum) {
    int N;
    cin >> N;

    int X = 0, Y = 0, Z = 0;
    int DX = 0, DY = 0, DZ = 0;

    for (int i = 0; i < N; i++) {
        int x, y, z, vx, vy, vz;
        cin >> x >> y >> z >> vx >> vy >> vz;
        X += x;
        Y += y;
        Z += z;
        DX += vx;
        DY += vy;
        DZ += vz;
    }

    double denom = 2*DX*DX + 2*DY*DY + 2*DZ*DZ;
    double mint;
    if (denom == 0) {
        mint = 0;
    } else {
        //mint = -(2*X*DX + 2*Y*DY + 2*Z*DZ)/(2*DX*DX + 2*DY*DY + 2*DZ*DZ);
        mint = -(2*X*DX + 2*Y*DY + 2*Z*DZ)/denom;
    }
    if (mint < 0) {
        mint = 0;
    }

    float minx = (X + DX*mint);
    float miny = (Y + DY*mint);
    float minz = (Z + DZ*mint);
    double mindist = sqrt((minx*minx + miny*miny + minz*minz)/(N*N));
    //float mindist = sqrt(minx*minx + miny*miny + minz*minz)/N;

    cout << "Case #" << caseNum << ": ";
    printf("%0.8f %0.8f\n", mindist, mint);
    /*
    cout << "X = " << X << " Y = " << Y << " Z = " << Z << endl;
    cout << "DX = " << DX << " DY = " << DY << " DZ = " << DZ << endl;
    cout << "mint = " << mint << endl;
    cout << "mindist = " << mindist << endl;
    */
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
