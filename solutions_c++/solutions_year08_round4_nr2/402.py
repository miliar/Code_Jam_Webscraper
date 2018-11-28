
#include <algorithm>
#include <fstream>

using namespace std;

int main() {
    ofstream fout("B-small.out");
    ifstream fin("B-small.in");
    
    int i, j, t, T, p, q;
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        int N, M, A;
        fin >> N >> M >> A;
        
        bool found = false;
        for (i = 0; i <= N; i++)
            for (j = 0; j <= M; j++)
                for (p = 0; p <= N; p++)
                    for (q = 0; q <= M; q++)
                        if (!found && abs(i * q - j * p) == A) {
                            fout << "Case #" << t << ": 0 0 " << i << " " << j << " " << p << " " << q << endl;
                            found = true;
                            break;
                        }
        
        if (!found)
            fout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
  
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
