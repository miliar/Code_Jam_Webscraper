#include <cstdio>
#include <algorithm>
using namespace std;

int grid[102][102][102];
int fillg[102][102][102];
char numtolett[27];
bool seen[102][102][102];

int ncases;
int height, width;

int recurfill(int i, int x, int y, int filln) {
    if (seen[i][y][x] == 1) return fillg[i][y][x];
    seen[i][y][x] = 1;
    
    fillg[i][y][x] = filln;
    
    //check square to fill
    int minval=10033;
    if (y > 0) minval = min(minval, grid[i][y-1][x]); //N
    if (x > 0) minval = min(minval, grid[i][y][x-1]); //W
    if (x < width-1) minval = min(minval, grid[i][y][x+1]); //E
    if (y < height-1) minval = min(minval, grid[i][y+1][x]); //S
    
    if (minval >= grid[i][y][x]) {
        return fillg[i][y][x];
    }
    
    if (y > 0 && minval == grid[i][y-1][x]) {
        //fillg[i][y][x-1] = fillg[i][y][x];
        fillg[i][y][x] = recurfill(i, x, y-1, filln);
    }
    else if (x > 0 && minval == grid[i][y][x-1]) {
        //fillg[i][y-1][x] = fillg[i][y][x];
        fillg[i][y][x] = recurfill(i, x-1, y, filln);
    }
    else if (x < width-1 && minval == grid[i][y][x+1]) {
        fillg[i][y][x] = recurfill(i, x+1, y, filln);
    }
    else if (y < height-1 && minval == grid[i][y+1][x]) {
        fillg[i][y][x] = recurfill(i, x, y+1, filln);
    }
    
    
    return fillg[i][y][x];
}


int main() {
    FILE* in = fopen("B-small-attempt0.in", "r");
    FILE* out = fopen("B-small-attempt0.out", "w");
    
    fscanf(in, "%d", &ncases);
    
    for (int i=0; i<ncases; ++i) {
        fscanf(in, "%d %d", &height, &width);
        
        for (int j=0; j<height; ++j) {
            for (int k=0; k<width; ++k) {
                fscanf(in, "%d", &grid[i][j][k]);
                fillg[i][j][k] = 0;
            }
            
        }
        
        int highest = -1, highx=-1, highy=-1;
        //find highest unseen, fill
        for (int j=0; j<height; ++j) {
            for (int k=0; k<width; ++k) {
                if (grid[i][j][k] > highest && seen[i][j][k] == 0) {
                    highest = grid[i][j][k];
                    highx = k;
                    highy = j;
                }
            }
        }
        
        int seccount=1;
        recurfill(i, highx, highy, seccount);
        bool allfilled = 1;
        for (int j=0; j<height; ++j) {
            for (int k=0; k<width; ++k) {
                if (seen[i][j][k] == 0) allfilled = 0;
            }
        }
        
        while (!allfilled) {
            highest = -1;
            highx=-1;
            highy=-1;
            //find highest unseen, fill
            for (int j=0; j<height; ++j) {
                for (int k=0; k<width; ++k) {
                    if (grid[i][j][k] > highest && seen[i][j][k] == 0) {
                        highest = grid[i][j][k];
                        highx = k;
                        highy = j;
                    }
                }
            }
            
            seccount+= 1;
            recurfill(i, highx, highy, seccount);
            
            allfilled = 1;
            for (int j=0; j<height; ++j) {
                for (int k=0; k<width; ++k) {
                    if (seen[i][j][k] == 0) allfilled = 0;
                }
            }
        }
        
        for (int j=0; j<27; ++j) {
            numtolett[j] = 0;
        }
        
        fprintf(out, "Case #%d:\n", i+1);
        
        char currlett = 'a';
        for (int j=0; j<height; ++j) {
            for (int k=0; k<width; ++k) {
                if (numtolett[fillg[i][j][k]] == 0) {
                    numtolett[fillg[i][j][k]] = currlett;
                    currlett += 1;
                }
                fprintf(out, "%c ", numtolett[fillg[i][j][k]]);
            }
            fprintf(out, "\n");
        }
        
    }
    
    return 0;
}
