#include <fstream>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int T, N, S, p, t, sum;

int main() {
    fin >> T;
    for (int i = 1; i <= T; i++) {
        sum = 0;
        fin >> N;
        fin >> S;
        fin >> p;
        for (int j = 1; j <= N; j++) {
            fin >> t;
            if (t % 3 == 1) {
                if ((t + 2) / 3 >= p)
                    sum++;
            }
            else if (t % 3 == 2) {
                if ((t + 1) / 3 >= p)
                    sum++;
                else if (p > 1 && (t + 1) / 3 == p - 1 && S > 0) {
                    sum++;
                    S--;
                }
            }
            else if (t % 3 == 0) {
                if (t / 3 >= p)
                    sum++;
                else if (p > 1 && t / 3 == p - 1 && S > 0) {
                    sum++;
                    S--;
                }
            }
        }
        fout << "Case #" << i << ": " << sum << endl;
    }
    return 0;
}
