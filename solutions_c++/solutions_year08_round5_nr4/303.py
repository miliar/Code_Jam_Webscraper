
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

const int MOD = 10007;
int H, W, R, num[100][100];
bool ok[100][100];

void calc() {
    for (int j = 0; j < W; j++)
        num[0][j] = 0;
    num[0][0] = 1;
    
    for (int i = 1; i < H; i++) {
        for (int j = 0; j < W; j++) {
            num[i][j] = 0;
            if (!ok[i][j])
                continue;
            if (i >= 2 && j >= 1)
                num[i][j] = (num[i][j] + num[i-2][j-1]) % MOD;
            if (i >= 1 && j >= 2)
                num[i][j] = (num[i][j] + num[i-1][j-2]) % MOD;
        }    
    }
}

int main() {
    ofstream fout("D-small.out");
    ifstream fin("D-small.in");
    
    int T;
    fin >> T;
    
    for (int t = 1; t <= T; t++) {
        fin >> H >> W >> R;
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
                ok[i][j] = true;
        for (int i = 0; i < R; i++) {
            int r, c;
            fin >> r >> c;
            ok[r-1][c-1] = false;
        }
        
        calc();
        fout << "Case #" << t << ": " << num[H-1][W-1] << endl;
    }
    
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
