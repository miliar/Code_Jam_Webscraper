
#include <iostream>
#include <fstream>

using namespace std;

inline int bits(int x) {
    if (x == 0) return 0;
    return 1 + bits(x & (x-1));
}

int main() {
    ofstream fout("B-small.out");
    ifstream fin("B-small.in");
    
    int i, j, t, T;
    int p[100], q[100];
    
    for (i = 0; i < 100; i++)
        cout << i << " " << bits(i) << endl;
    
    fin >> T;
    for (t = 1; t <= T; t++) {
        // brute force for small
        int N, M; fin >> N >> M;
        for (i = 0; i < M; i++) {
            p[i] = q[i] = 0;
            int tt; fin >> tt;
            for (j = 0; j < tt; j++) {
                int m, k; fin >> m >> k; 
                if (k == 0) p[i] |= (1 << (m-1));
                else q[i] |= (1 << (m-1));
            }
        }
        
        int best = -1, big = (1 << N) - 1;
        for (i = 0; i < (1 << N); i++) {
            for (j = 0; j < M; j++) if ((p[j] & (big-i)) == 0 && ((q[j] & i) == 0)) break;
            if (j < M) continue;
            if (best == -1 || bits(i) < bits(best)) best = i;
        }
        
        fout << "Case #" << t << ":";
        if (best == -1) fout << " IMPOSSIBLE" << endl;
        else {
            for (i = 0; i < N; i++) fout << " " << ((best & (1 << i)) ? "1" : "0");
            fout << endl;
        }
    }
  
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
