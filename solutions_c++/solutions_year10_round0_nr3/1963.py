#include <iostream>
#include <fstream>
using namespace std;

int T;
int R, k, N;
int g[1005];
int end[1005], sum[1005];
long long y;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    fin >> T;
    for (int x = 1; x <= T; x++) {
        fout << "Case #" << x << ": ";
        y = 0;
        
        fin >> R >> k >> N;
        for (int n = 0; n < N; n++)
            fin >> g[n];

        for (int s = 0; s < N; s++) {
            sum[s] = 0;
            int e = s;
            do {
                if (sum[s] + g[e] > k)
                    break;
                sum[s] += g[e];
                e = (e+1) % N;
            } while (e != s);
            end[s] = e;
        }
        
        int start = 0;
        while (R--) {
            y += (long long)sum[start];
            start = end[start];
        }
        
        fout << y << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
