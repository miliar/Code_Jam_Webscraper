#include <fstream>

using namespace std;

int main(int argc, char** argv) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int t = 1; t <= T; ++t) {
        fout << "Case #" << t << ':' << endl;
        int N;
        fin >> N;
        char schedule[100][100];
        double WP[100];
        double OWP[100];
        double OOWP[100];
        int played[100];
        int won[100];
        for (int i = 0; i < N; ++i) {
            WP[i] = 0;
            OWP[i] = 0;
            OOWP[i] = 0;
            played[i] = 0;
            won[i] = 0;
            fin.get();
            for (int j = 0; j < N; ++j) {
                fin.get(schedule[i][j]);
            }
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (schedule[i][j] != '.')
                    ++played[i];
                if (schedule[i][j] == '1')
                    ++won[i];
            }
            WP[i] = double(won[i])/played[i];
//            fout << WP[i] << endl;
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (schedule[i][j] == '1')
                    OWP[i] += (double(won[j])/(played[j]-1));
                if (schedule[i][j] == '0')
                    OWP[i] += (double(won[j]-1)/(played[j]-1));
            }
            OWP[i] /= played[i];
//            fout << OWP[i] << endl;
        }
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (schedule[i][j] != '.')
                    OOWP[i] += OWP[j];
            }
            OOWP[i] /= played[i];
        }
        for (int i = 0; i < N; ++i)
            fout << (0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]) << endl;
    }
}

