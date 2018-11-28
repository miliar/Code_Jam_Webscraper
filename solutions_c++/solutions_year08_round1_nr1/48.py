
#include <algorithm>
#include <fstream>

using namespace std;

long long x[1000], y[1000];

int main() {
    ofstream fout("A-large.out");
    ifstream fin("A-large.in");
    
    int i, j, t, N, T;
    
    fin >> T;
    for (t = 1; t <= T; t++) {
        fin >> N;
        for (i = 0; i < N; i++) fin >> x[i];
        for (i = 0; i < N; i++) fin >> y[i];
        
        sort (x, x + N);
        sort (y, y + N);
        
        long long sum = 0;
        
        for (j = N - 1; j >= 0; j--) if (y[j] < 0) break;
        // yj < 0
        for (i = 0; i <= j; i++) sum += x[N-1-i] * y[i];
        // yj >= 0
        for (i = j + 1; i < N; i++) sum += x[N-1-i] * y[i];
        
        fout << "Case #" << t << ": " << sum << endl;
    }
  
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
