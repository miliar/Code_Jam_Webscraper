#include <iostream>
using namespace std;

double getWP(string str, int me, int exclude) {
    int win = 0, lose = 0;
    for (int i = 0; i < (int)str.length(); i++) {
        if (i != me && i != exclude) {
            if (str[i] == '1') {
                win++;
            } else if (str[i] == '0') {
                lose++;
            }
        }
    }
    if (win + lose == 0) {
        return 0;
    } else {
        return (double)win / (win + lose);
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        string* rows = new string[N];
        for (int j = 0; j < N; j++) {
            cin >> rows[j];
        }
        double* WP = new double[N];
        double* OWP = new double[N];
        double* OOWP = new double[N];
        for (int j = 0; j < N; j++) {
            WP[j] = getWP(rows[j], j, j);
        }
        for (int j = 0; j < N; j++) {
            int opponent = 0;
            double sum = 0;
            for (int k = 0; k < N; k++) {
                if (j != k && (rows[j][k] == '1' || rows[j][k] == '0')) {
                    sum += getWP(rows[k], k, j);
                    opponent++;
                }
            }
            OWP[j] = sum / opponent;
        }
        for (int j = 0; j < N; j++) {
            int opponent = 0;
            double sum = 0;
            for (int k = 0; k < N; k++) {
                if (j != k && (rows[j][k] == '1' || rows[j][k] == '0')) {
                    sum += OWP[k];
                    opponent++;
                }
            }
            OOWP[j] = sum / opponent;
        }
        cout << "Case #" << i + 1 << ":" << endl;
        for (int j = 0; j < N; j++) {
            cout << WP[j] / 4 + OWP[j] / 2 + OOWP[j] / 4 << endl;
        }
        delete[] rows;
        delete[] WP;
        delete[] OWP;
        delete[] OOWP;
    }
}
