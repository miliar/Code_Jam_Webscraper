#include <cstdio>

const int MAXH =  100; // maximum height
const int MAXW =  100; // maximum width
const int MAXA = 9999; // maximum altitude
const int NDIR =    4; // number of directions

int land[MAXH + 2][MAXW + 2]; // elevation map of the land
char basins[MAXH + 2][MAXW + 2]; // drainage basins

              // N  W  E  S
int dy[NDIR] = {-1, 0, 0, 1};
int dx[NDIR] = { 0,-1, 1, 0};

char dir[NDIR] = {'N','W','E','S'};
char rev[NDIR] = {'S','E','W','N'};

// cardinal point
int iscardinal(int c) {
    return c == 'C' || c == 'N' || c == 'W' || c == 'E' || c == 'S';
}
// water flow direction
void flowdir(int height, int width) {
    int r, c, alt, lowest, d;

    for(r = 1; r < height; r++)
        for(c = 1; c < width; c++) {
            lowest = land[r][c]; // lowest altitude
            basins[r][c] = 'C'; // sink
            for(d = 0; d < NDIR; d++)
                if((alt = land[r + dy[d]][c + dx[d]]) < lowest) {
                    lowest = alt;
                    basins[r][c] = dir[d];
                }
        }
}
void label(int l, int r, int c) {
    for(int d = 0; d < NDIR; d++)
        if(basins[r + dy[d]][c + dx[d]] == rev[d]) // water flows from a neighbor cell to the current cell
            label(l, r + dy[d], c + dx[d]);

    switch(basins[r][c]) {
    case 'C': basins[r][c] = l; break;
    case 'N': label(basins[r][c] = l, r - 1, c); break;
    case 'W': label(basins[r][c] = l, r, c - 1); break;
    case 'E': label(basins[r][c] = l, r, c + 1); break;
    case 'S': label(basins[r][c] = l, r + 1, c); break;
    }
}
int main() {
    int maps, m, height, width, r, c, l;
    FILE *fin, *fout;

    fin  = fopen("B-large.in",  "r");
    fout = fopen("B-large.out", "w");

    fscanf(fin, "%d", &maps);

    for(m = 1; m <= maps; m++) {
        fscanf(fin, "%d%d", &height, &width);
        height++, width++;

        for(r = 0; r <= height; r++) {
            land[r][0] = land[r][width] = MAXA + 1;
            basins[r][0] = basins[r][width] = '\0';
        }
        for(c = 1; c < width; c++) {
            land[0][c] = land[height][c] = MAXA + 1;
            basins[0][c] = basins[height][c] = '\0';
        }

        for(r = 1; r < height; r++)
            for(c = 1; c < width; c++)
                fscanf(fin, "%d", &land[r][c]);

        fprintf(fout, "Case #%d:\n", m);

        flowdir(height, width);

        l = 'a'; // label
        for(r = 1; r < height; r++)
            for(c = 1; c < width; c++)
                if(iscardinal(basins[r][c]))
                    label(l++, r, c);

        for(r = 1; r < height; r++)
            for(c = 1; c < width; c++)
                fprintf(fout, "%c%c", basins[r][c], (c != width - 1) ? ' ' : '\n');
    }

    return 0;
}
