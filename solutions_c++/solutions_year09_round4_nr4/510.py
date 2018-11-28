#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int C;
int N;
int X[10],Y[10],R[10];
double best;

double dist(int i, int j);

int main() {
    cin >> C;
    for (int c = 1; c <= C; c++) {
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> X[i] >> Y[i] >> R[i];
        if (N == 1)
            best = (double)R[0];
        if (N == 2)
            best = max((double)R[0],(double)R[1]);
        if (N == 3) {
            best = max((dist(0,1)+R[0]+R[1])/2,(double)R[2]);
            if (best > max((dist(0,2)+R[0]+R[2])/2,(double)R[1]))
                best = max((dist(0,2)+R[0]+R[2])/2,(double)R[1]);
            if (best > max((dist(1,2)+R[1]+R[2])/2,(double)R[0]))
                best = max((dist(1,2)+R[1]+R[2])/2,(double)R[0]);
        }
        cout.precision(6);
        cout << fixed << "Case #" << c << ": " << best << endl;
    }
    return 0;
}

double dist(int i, int j) {
    return sqrt((double)(Y[j]-Y[i])*(Y[j]-Y[i]) + (double)(X[j]-X[i])*(X[j]-X[i]));
}
