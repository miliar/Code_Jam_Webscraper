
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int alt[100][100];
int label[100][100];

int main() {
    FILE *fin = fopen("B-large.in", "r"), *fout = fopen("B-large.out", "w");
    int T, H, W;
    fscanf(fin, "%d", &T);
    for(int k = 0; k < T; ++k) {
        fscanf(fin, "%d%d", &H, &W);
        for(int i = 0; i < H; ++i) {
            for(int j = 0; j < W; ++j) {
                fscanf(fin, "%d", &alt[i][j]);
                label[i][j] = -1;
            }
        }
    
        int cur = 0;
        for(int i = 0; i < H; ++i) {
            for(int j = 0; j < W; ++j) {
                if(label[i][j] != -1) continue;
                int fi = i, fj = j;
                while(true) {
                    int lowest = alt[fi][fj], di = 0, dj = 0;
                    
                    if(fi > 0 && alt[fi-1][fj] < lowest)
                        lowest = alt[fi-1][fj], di = -1, dj = 0;
                    if(fj > 0 && alt[fi][fj-1] < lowest)
                        lowest = alt[fi][fj-1], di = 0, dj = -1;
                    if(fj+1 < W && alt[fi][fj+1] < lowest)
                        lowest = alt[fi][fj+1], di = 0, dj = 1;
                    if(fi+1 < H && alt[fi+1][fj] < lowest)
                        lowest = alt[fi+1][fj], di = 1, dj = 0;

                    if(lowest == alt[fi][fj]) break;
                    fi += di, fj += dj;
                }
                if(label[fi][fj] == -1) label[fi][fj] = cur++;
                
                label[i][j] = label[fi][fj];
            }
        }
        
        fprintf(fout, "Case #%d:\n", k+1);
        for(int i = 0; i < H; ++i)
            for(int j = 0; j < W; ++j)
                fprintf(fout, "%c%c", 'a'+label[i][j], j+1==W?'\n':' ');
    }
    
    return 0;
}
