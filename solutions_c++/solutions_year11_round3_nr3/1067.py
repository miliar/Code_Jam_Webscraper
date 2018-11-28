#include <iostream>
#include <fstream>

using namespace std;

int main() {
    fstream fin ("C-small-attempt1.in", fstream::in);
    int cases; fin >> cases;
    string answers[cases];
    fstream fout ("output.txt", fstream::out);
    for (int t = 0; t < cases; t++) {
        int N, L, H;
        fin >> N >> L >> H;
        int freq[N];
        for (int i = 0; i < N; i++) fin >> freq[i];
        int gcf = 0;
        fout << "Case #" << t+1 << ": ";
        for (int i = L; i <= H; i++) {
            bool find = true;
            for (int j = 0; j < N; j++) {
                if (freq[j] % i != 0 && i % freq[j] != 0) {
                    find = false;
                    break;
                }
            }
            if (find) {
                gcf = i;
                break;
            }
        }
        if (gcf != 0) {
            fout << gcf << endl;
            continue;
        }
        fout << "NO" << endl;
    }
    return 0;
}
