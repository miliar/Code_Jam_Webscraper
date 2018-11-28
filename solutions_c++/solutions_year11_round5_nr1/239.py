
#include <iostream>
#include <cmath>
#include <vector>

#define MAXN 200

using namespace std;

int W, L, U, G;
int lx[MAXN], ly[MAXN], ux[MAXN], uy[MAXN];

int N;
int x[MAXN], y[MAXN];

double tx[MAXN], ty[MAXN];

double evaluateCut(double pos) {
    int li = 0;
    for(; li < L - 1; li++)
        if(lx[li] <= pos && pos < lx[li + 1])
            break;

    int ui = 0;
    for(; ui < U - 1; ui++)
        if(ux[ui] <= pos && pos < ux[ui + 1])
            break;

    int n = 0;
    double lambda;
    for(int i = 0; i <= li; i++)
        tx[n] = lx[i], ty[n] = ly[i], n++;

    lambda = (pos - lx[li]) / (lx[li + 1] - lx[li]);
    tx[n] = (1 - lambda) * lx[li] + lambda * lx[li + 1];
    ty[n] = (1 - lambda) * ly[li] + lambda * ly[li + 1];
    n++;

    lambda = (pos - ux[ui]) / (ux[ui + 1] - ux[ui]);
    tx[n] = (1 - lambda) * ux[ui] + lambda * ux[ui + 1];
    ty[n] = (1 - lambda) * uy[ui] + lambda * uy[ui + 1];
    n++;

    for(int i = ui; i >= 0; i--)
        tx[n] = ux[i], ty[n] = uy[i], n++;

    double area = 0;
    for(int i = 0; i < n; i++)
        area += tx[i] * ty[(i+1)%n] - tx[(i+1)%n] * ty[i];

    return fabs(0.5 * area);
}

double getCut(double area) {
    double low = 0, high = W;
    for(int i = 0; i < 100; i++) {
        double mid = 0.5 * (low + high);
        if(evaluateCut(mid) < area)
            low = mid;
        else
            high = mid;
    }
    return low;
}

vector <double> solve() {
    N = 0;
    for(int i = 0; i < L; i++)
        x[N] = lx[i], y[N] = ly[i], N++;
    for(int i = U-1; i >= 0; i--)
        x[N] = ux[i], y[N] = uy[i], N++;

    double total = 0;
    for(int i = 0; i < N; i++)
        total += x[i] * y[(i+1)%N] - x[(i+1)%N] * y[i];
    total = fabs(0.5 * total);

    vector <double> cuts(G - 1);
    for(int i = 0; i < G - 1; i++) {
        double area = (i + 1) * total / G;
        cuts[i] = getCut(area);
    }
    return cuts;
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i < T; i++) {
        cin >> W >> L >> U >> G;
        for(int j = 0; j < L; j++)
            cin >> lx[j] >> ly[j];
        for(int j = 0; j < U; j++)
            cin >> ux[j] >> uy[j];

        vector <double> cuts = solve();
        cout << "Case #" << i+1 << ":" << endl;
        for(int j = 0; j < G - 1; j++)
            printf("%.10lf\n", cuts[j]);
    }
}
