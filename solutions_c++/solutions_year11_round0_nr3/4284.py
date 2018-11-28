#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int T,N;
vector<int> C;

int main(int argc, char *argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int c,x,s;
    
    fin >> T;
    for (int t = 1; t <= T; t++) {
        C.clear();
        x = 0;
        fin >> N;
        for (int n = 0; n < N; n++) {
            fin >> c;
            C.push_back(c);
            x ^= c;
        }
        
        fout << "Case #" << t << ": ";
        if (x != 0)
            fout << "NO";
        else {
            s = 0;
            sort(C.begin(), C.end());
            for (int i = 1; i < N; i++)
                s += C[i];
            fout << s;
        }
        fout << endl;
    }
    
    return 0;
}
