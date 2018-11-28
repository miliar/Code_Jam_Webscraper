
#include <fstream>

using namespace std;


int main() {
    ofstream fout("C-large.out");
    ifstream fin("C-large.in");
    
    int i, j, t, N, T;
    
    fin >> T;
    for (t = 1; t <= T; t++) {
        fin >> N;
        if (N == 1) {
            fout << "Case #" << t << ": 005" << endl;
            continue;
        }
        if (N == 2) {
            fout << "Case #" << t << ": 027" << endl;
            continue;
        }
        
        // a(n) = 6 * a(n-1) - 4 * a(n-2)
        // must be periodic mod 1000!!! period: 100
        if (N > 100) N = (N % 100) + 100;
        
        int x = 6, y = 28;
        for (i = 0; i < N - 2; i++) {
            int temp = y;
            y = (6 * y - 4 * x + 4000) % 1000;
            x = temp;
        }
        
        y = (y + 999) % 1000;
        fout << "Case #" << t << ": " << y/100 << (y/10) % 10 << y % 10 << endl;
    }
  
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
