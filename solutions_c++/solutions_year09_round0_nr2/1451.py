#include <iostream>
#include <fstream>
using namespace std;

#define MAX 101
#define oo 987654321
#define LL long
LL i,j,n,m;
LL in[MAX][MAX];
char out[MAX][MAX];
LL dx[4] = { -1,0,0,1};
LL dy[4] = {0,-1,1,0};
char now;
LL ni,nj,bi,bj,T;

ifstream fin("B.in");
ofstream fout("B.out");

bool ok(LL x, LL y) {
     return x >=0 && y >= 0 && x < n && y < m;
     }

char flood(LL i, LL j) {
     if (out[i][j] != '.') return out[i][j];
     
     LL idx = 0;
     for (LL k=1;k<4;k++) {
         ni = i + dx[k];
         nj = j + dy[k];
         if (!ok(ni,nj)) continue;
         bi = i + dx[idx];
         bj = j + dy[idx];
         if (!ok(bi,bj)) { idx = k; continue; }
         if (in[ni][nj] < in[bi][bj]) idx = k; 
         }
     bi = i + dx[idx];
     bj = j + dy[idx];
     if (in[bi][bj] >= in[i][j]) return out[i][j] = now++;
     return out[i][j] = flood(bi,bj);
     }

int main() {
    fin >> T;
    for (LL t=0;t<T;t++) {
        cout << "Case #" << t + 1 << ":" << endl;
        fin >> n >> m;
        for (i=0;i<n;i++)
            for (j=0;j<m;j++) {
                fin >> in[i][j];
                out[i][j] = '.';
                }
    
        now = 'a';
        for (i=0;i<n;i++)
            for (j=0;j<m;j++)
                if (out[i][j] == '.') flood(i,j);
        
        fout << "Case #" << t + 1 << ":" << endl;
        
        if (n==1 && m==1) { fout << 'a' << endl; continue; }
        
        for (i=0;i<n;i++) {
            for (j=0;j<m;j++) fout << out[i][j] << " ";
            fout << endl;
            }
        }
    cout << "Done!" << endl;
    system("pause");
}
