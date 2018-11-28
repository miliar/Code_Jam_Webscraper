#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

const int MAX_TT = 10;
const int MAX_NN = 2;
const int MIN_NN = 2;
const int MAX_MM = 10;
int TT;
int NN;
int MM;
int PPxx[MAX_NN];
int PPyy[MAX_NN];
int QQxx[MAX_MM];
int QQyy[MAX_MM];
int apx;
int apy;
long double len_pp;
long double r[MAX_NN];
int arx[MAX_NN];
int ary[MAX_NN];
long double theta[MAX_NN];
long double area[MAX_NN];

int main() {
    cout.precision(31);
    cin >> TT;
    for (int z = 1; z <= TT; z++) {
        cout << "Case #" << z << ": " << flush;
        cin >> NN >> MM;
        for (int i = 0; i < NN; i++) { 
            cin >> PPxx[i];
            cin >> PPyy[i];
        }
        apx = abs(PPxx[0] - PPxx[1]);
        apy = abs(PPyy[0] - PPyy[1]);
        len_pp = sqrt((apx * apx) + (apy * apy));
        for (int i = 0; i < MM; i++) { 
            cin >> QQxx[i];
            cin >> QQyy[i];
            for (int j = 0; j < NN; j++) {
                arx[j] = abs(PPxx[j] - QQxx[i]);
                ary[j] = abs(PPyy[j] - QQyy[i]);
                r[j] = sqrt((arx[j] * arx[j]) + (ary[j] * ary[j]));
            }
            theta[0] = 2.0dd * acos(((r[0] * r[0]) + (len_pp * len_pp) - (r[1] * r[1]))/(2.0dd * r[0] * len_pp));
            theta[1] = 2.0dd * acos(((r[1] * r[1]) + (len_pp * len_pp) - (r[0] * r[0]))/(2.0dd * r[1] * len_pp));
            area[0] = ((r[0] * r[0]) * (theta[0] - sin(theta[0])))/2.0dd;
            area[1] = ((r[1] * r[1]) * (theta[1] - sin(theta[1])))/2.0dd;
            cout << area[0] + area[1];
            if (i != MM - 1) { cout << " "; } else { cout << endl; };
        }
    }
}