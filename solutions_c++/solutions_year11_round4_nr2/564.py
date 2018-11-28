#include <cstdio>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <sstream>
using namespace std;

#define MP make_pair
#define SS size()
#define PB push_back
#define ff(a, b) for (int a = 0; a < (b); ++a)
#define f1(a, b) for (int a = 1; a < (b); ++a)
#define ii(n)    ff(i, n)
#define FF first
#define CC second
#define BB begin()
#define EE end()
#define all(x)  (x).BB, (x).EE
#define ite(v)   typeof((v).BB)
#define fe(i, v) for(ite(v) i = (v).BB; i != (v).EE; ++i)


typedef long long LL;
typedef pair<int, int> pii;

#define EPS (1e-10)


struct xy {
    double x, y;
    xy(double x, double y) : x(x), y(y) { }
    xy() : x(0), y(0) { }
};

xy operator+ (xy a, xy b) { return xy(a.x + b.x,
                                      a.y + b.y); }
xy operator- (xy a, xy b) { return xy(a.x - b.x,
                                      a.y - b.y); }
xy operator* (double a, xy b) { return xy(b.x*a, b.y*a); }
xy operator* (xy b, double a) { return xy(b.x*a, b.y*a); }

int w, h, D;
int grid[555][555];
double dgrid[555][555];
xy centre_of_mass[555][555];
double mass[555][555];

int main() {
    int T;
    cin >> T;

    ff (tcase, T) {
        cin >> w >> h >> D;

        ff (row, w) {
            ff (column, h) {
                //cin >> grid[row+1][column+1];
                char c;
                cin >> c;
                //printf("%c", c);
                grid[row+1][column+1] = (int)(c - '0');
                dgrid[row+1][column+1] = grid[row+1][column+1];
            }
            //printf("\n");
        }

        ff (x, w+1) {
            centre_of_mass[x][0] = xy(x+0.5, 0.5);
            mass[x][0] = 0;
        }
        ff (y, h+1) {
            centre_of_mass[0][y] = xy(0.5, y+0.5);
            mass[0][y] = 0;
        }
        
        ff (x0, w) {
            ff (y0, h) {
                int x = x0 + 1;
                int y = y0 + 1;
                mass[x][y] = dgrid[x][y] + mass[x-1][y] + mass[x][y-1]
                                - mass[x-1][y-1];
                double mult = 1;
                if (abs(mass[x][y]) > EPS)
                    mult = 1.0 / mass[x][y];
                centre_of_mass[x][y] = mult* 
                                        (dgrid[x][y]*xy(x+0.5, y+0.5)
                                    + mass[x-1][y]*centre_of_mass[x-1][y]
                                    + mass[x][y-1]*centre_of_mass[x][y-1]
                                    - mass[x-1][y-1]*centre_of_mass[x-1][y-1]);
                
            }
        }

        /*
        ff (x, w) {
            ff (y, h)
                printf("%g,%g ", centre_of_mass[x][y].x, centre_of_mass[x][y].y);
            printf("\n");
        }
        */

        int k = min(w, h);
        bool found = false;
        int best_k = 0;
        for (; k >= 3; --k) {
            ff (x, w-k+1) {
                ff (y, h-k+1) {
                    int ex = x + k;
                    int ey = y + k;
                    int xc = x+1;
                    int yc = y+1;
                    double hmass = mass[ex][ey]
                                    - mass[ex][y]
                                    - mass[x][ey]
                                    + mass[x][y]
                                    - dgrid[ex][ey]
                                    - dgrid[xc][ey]
                                    - dgrid[ex][yc]
                                    - dgrid[xc][yc];
                    double mult = 1.0;
                    if (abs(hmass) > EPS)
                        mult = 1.0 / hmass;
                    xy com = mult*(
                             centre_of_mass[ex][ey]*mass[ex][ey]
                            -centre_of_mass[x][ey] *mass[x][ey]
                            -centre_of_mass[ex][y] *mass[ex][y]
                            +centre_of_mass[x][y]  *mass[x][y]
                            -xy(ex+0.5, ey+0.5)*dgrid[ex][ey]
                            -xy(xc+0.5, ey+0.5)*dgrid[xc][ey]
                            -xy(ex+0.5, yc+0.5)*dgrid[ex][yc]
                            -xy(xc+0.5, yc+0.5)*dgrid[xc][yc]);

                    //printf("%lg %lg  %g %g\n", com.x, com.y,
                    //        0.5*(ex + xc), 0.5*(ey + yc));
                    
                    if (abs(com.x - 0.5 - 0.5*(ex + xc)) < EPS
                    &&  abs(com.y - 0.5 - 0.5*(ey + yc)) < EPS
                    || abs(hmass) < EPS) {
                        best_k = k;
                        found = true;
                        break;
                    }
                    
                }
                //printf("\n");
                if (found) break;
            }
            //printf("\n");
            if (found) break;
        }

        if (found) {
            printf("Case #%d: %d\n", tcase+1, best_k);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", tcase+1);
        }
    }


    return 0;
}





