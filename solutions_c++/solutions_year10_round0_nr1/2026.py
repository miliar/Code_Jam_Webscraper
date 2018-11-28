#include <iostream>
#include <fstream>
using namespace std;

int T;
int N, K;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    fin >> T;
    for (int t = 1; t <= T; t++) {
        fin >> N >> K;
        fout << "Case #" << t << ": " << ((K % (1 << N) == (1 << N) - 1) ? "ON" : "OFF") << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}
