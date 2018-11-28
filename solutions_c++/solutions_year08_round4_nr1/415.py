
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

int num[11000][2], G[11000], C[11000];
const int INF = 999999;

int main() {
    ofstream fout("A-large.out");
    ifstream fin("A-large.in");
    
    int i, j, t, T, M, V;
    
    fin >> T;
    for (t = 1; t <= T; t++) {
        fin >> M >> V;
        for (i = 1; i <= (M - 1) / 2; i++) {
            fin >> G[i] >> C[i];
            num[i][0] = num[i][1] = -1;
        }
        for (i = (M + 1) / 2; i <= M; i++) {
            int L; fin >> L;
            num[i][L] = 0;
            num[i][1-L] = -1;
        }
        
        for (i = (M - 1) / 2; i > 0; i--) {
            int k = 0;
            num[i][k] = num[i][1-k] = INF;
            if (G[i] == 1 || C[i] == 1) { // AND
                int c = 1;
                if (G[i] == 1) c = 0;
            
                if (num[2*i][0] != -1 && num[2*i+1][0] != -1) // 0 0
                    num[i][k] <?= (num[2*i][0] + num[2*i+1][0] + c);
                if (num[2*i][0] != -1 && num[2*i+1][1] != -1) // 0 1
                    num[i][k] <?= (num[2*i][0] + num[2*i+1][1] + c);
                if (num[2*i][1] != -1 && num[2*i+1][0] != -1) // 1 0
                    num[i][k] <?= (num[2*i][1] + num[2*i+1][0] + c);
                // if (i == 3) cout << num[i][k] << endl;
                
                if (num[2*i][1] != -1 && num[2*i+1][1] != -1) // 1 1
                    num[i][1-k] <?= (num[2*i][1] + num[2*i+1][1] + c);
                
            }
            if (G[i] == 0 || C[i] == 1) { // OR
                int c = 1;
                if (G[i] == 0) c = 0;
            
                if (num[2*i][0] != -1 && num[2*i+1][0] != -1) // 0 0
                    num[i][k] <?= (num[2*i][0] + num[2*i+1][0] + c);
                
                if (num[2*i][0] != -1 && num[2*i+1][1] != -1) // 0 1
                    num[i][1-k] <?= (num[2*i][0] + num[2*i+1][1] + c);
                if (num[2*i][1] != -1 && num[2*i+1][0] != -1) // 1 0
                    num[i][1-k] <?= (num[2*i][1] + num[2*i+1][0] + c);
                if (num[2*i][1] != -1 && num[2*i+1][1] != -1) // 1 1
                    num[i][1-k] <?= (num[2*i][1] + num[2*i+1][1] + c);
            }
            if (num[i][k] == INF)
                num[i][k] = -1;
            if (num[i][1-k] == INF)
                num[i][1-k] = -1;
        }
        // for (i = M; i > 0; i--)
            // fout << i << " " << num[i][0] << " " << num[i][1] << " : " << G[i] << " " << C[i] << endl;
        // M->1 plus order bug
        fout << "Case #" << t << ": ";
        if (num[1][V] == -1)
            fout << "IMPOSSIBLE" << endl;
        else
            fout << num[1][V] << endl;
    }
  
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
