#include <vector>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

typedef vector<double> vd;
typedef vector<int> vi;
typedef vector<string> vs;

int main() {
    int T;
    cin >> T;
    for (int cs=1; cs<=T; ++cs) {
        int N;
        cin >> N;
        vs s(N);
        vd w(N);
        vd n(N);
        vd owp(N);
        for (int i=0; i<N; ++i) {
            cin >> s[i];
            for (int j=0; j<N; ++j) {
                switch (s[i][j]) {
                    case '.': break;
                    case '0': n[i]++; break;
                    case '1': n[i]++; w[i]++; break;
                }
            }
        }
        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j) {
                if (i==j) continue;
                switch (s[i][j]) {
                    case '.': break;
                    case '0': owp[i] += (w[j]-1)/(n[j]-1.0); break;
                    case '1': owp[i] += w[j]/(n[j]-1.0); break;
                }
            }
            owp[i] /= n[i];
        }
        cout << "Case #" << cs << ":\n";
        for (int i=0; i<N; ++i) {
            double rpi=0.25*w[i]/n[i] + 0.5*owp[i];
            double oowp=0.0;
            for (int j=0; j<N; ++j) {
                if (i==j) continue;
                switch (s[i][j]) {
                    case '.': break;
                    default: oowp += owp[j];
                }
            }
            oowp /= n[i];
            rpi += 0.25*oowp;
            cout << setprecision(12) << rpi << "\n";
        }
    }
}
