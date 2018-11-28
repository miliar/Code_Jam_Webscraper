
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

char c[10][10];
int M, N, num[10][1024], bits[1024], cb[10];

inline bool check(int n) {
    for (int i = 0; i + 1 < N; i++)
        if ((n & (1<<i)) != 0 && (n & (1<<(i+1))) != 0)
            return false;
    return true;    
}

inline bool checktwo(int a, int b) {
    for (int i = 0; i + 1 < N; i++) {
        if ((a&(1<<i)) != 0 && (b&(1<<(i+1))) != 0)
            return false;
        if ((b&(1<<i)) != 0 && (a&(1<<(i+1))) != 0)
            return false;  
    }
    return true;   
}

void calc() {
    int i, j, k;
    bits[0] = 0;
    for (i = 1; i < 1024; i++)
        bits[i] = bits[i / 2] + (i % 2);

    for (i = 0; i < M; i++) {
        cb[i] = 0;
        for (j = 0; j < N; j++)
            if (c[i][j] == 'x')
                cb[i] |= (1 << j);    
    }
    
    for (j = 0; j < (1 << N); j++) {
        num[0][j] = 0;
        if (check(j) && (j & cb[0]) == 0)
            num[0][j] = bits[j];
    }
    
    for (i = 1; i < M; i++)
        for (j = 0; j < (1 << N); j++) {
            num[i][j] = 0;
            if (check(j) && (j & cb[i]) == 0) {
                num[i][j] = bits[j];
                for (k = 0; k < (1 << N); k++)
                    if (check(k) && checktwo(k, j))
                        num[i][j] = max(num[i][j], bits[j] + num[i-1][k]);
            }
        }
}

int main() {
    ofstream fout("C-small.out");
    ifstream fin("C-small.in");
    
    int T;
    fin >> T;
    
    for (int t = 1; t <= T; t++) {
        fin >> M >> N;
        
        int i, j;
        for (i = 0; i < M; i++) {
            for (j = 0; j < N; j++) {
                char buf = ' ';
                while(buf != '.' && buf != 'x')
                    fin >> buf;
                
                c[i][j] = buf;
            }
        }
        
        calc();
        int best = 0;
        for (j = 0; j < (1 << N); j++)
            best = max(best, num[M-1][j]);
        fout << "Case #" << t << ": " << best << endl;
    }
    
    fin.close();
    fout.close();
    
    system("pause");
    
    return 0;
}
