#include <fstream>
using namespace std;

unsigned int T, N, K;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin >> T;
    for(int i = 1; i <= T; i++){
        fin >> N >> K;
        int ok = 1;
        for(int i = 0; i < N; i++){
            ok &= ((K >> i) & 1);
        }
        fout << "Case #" << i << ": " << (ok ? "ON" : "OFF") << endl;
    }
}
