#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int alts[102][102];
int basins[102][102];

int nbasins = 0;

#define REP(i, N) for(int i=0; i<(N); i++)

int dirs[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

int find_basin(int i, int j) {
    if (basins[i][j] != 0)
        return basins[i][j];

    int mind = -1;
    {
        int minh = alts[i][j];
        REP(d, 4) {
            int a = alts[i+dirs[d][0]][j+dirs[d][1]];
            if (a < minh) {
                minh = a;
                mind = d;
            }
        }
    }

    if (mind == -1) {
        nbasins++;
        //printf("%d %d is a sink, assigning basin num %d\n", i, j, nbasins);
        basins[i][j] = nbasins;
        return nbasins;
    }

    int basin = find_basin(i+dirs[mind][0], j+dirs[mind][1]);
    basins[i][j] = basin;
    return basin;
}

int main(int argc, char **argv) {
    FILE* f = fopen(argv[1], "r");

    int t;
    fscanf(f, "%d", &t);

    REP(_t, t) {
        printf("Case #%d:\n", _t+1);
        int h,w;
        fscanf(f, "%d %d", &h, &w);

        REP(i, w+2) {
            alts[i][0] = 1000000;
            alts[i][h+1] = 1000000;
        }
        REP(j, h+2) {
            alts[0][j] = 1000000;
            alts[w+1][j] = 1000000;
        }

        REP(j, h) {
            REP(i, w) {
                //printf("%d %d\n", i, j);
                fscanf(f, "%d", &alts[i+1][j+1]);
            }
        }

        memset(basins, 0, sizeof(basins));
        nbasins = 0;

        REP(j, h) REP(i, w) find_basin(i+1, j+1);

        char nextbasin = 'a';
        char basin_letters[27];
        memset(basin_letters, 0, sizeof(basin_letters));
        REP(j, h) {
            REP(i, w) {
                if (i != 0)
                    printf(" ");

                int basin = basins[i+1][j+1];
                //printf("%d", basin);
                char b = basin_letters[basin];
                if (b == 0) {
                    //printf("basin %d has no letter, assigning %c\n", basin, nextbasin);
                    b = nextbasin;
                    basin_letters[basin] = nextbasin;
                    nextbasin++;
                }
                printf("%c", b);
            }
            printf("\n");
        }
        nbasins = 0;

        //break;
    }

    fclose(f);

    return 0;
}
