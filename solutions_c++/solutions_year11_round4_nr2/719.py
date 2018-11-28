#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

typedef long long LL;
const int dx[4]={0,1,0,1}, dy[4]={0,0,1,1};
const int MAXR = 501, MAXC = 501;
const double EPS = 1E-7;
string grid[MAXR];
double mass[MAXR][MAXC];

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        int R, C, D;
        in >> R >> C >> D;
        for( int i=R-1; i>=0; i-- )
            in >> grid[i];
        for( int i=0; i<R; i++ ) {
            for( int j=0; j<C; j++ ) {
                mass[i][j] = (grid[i][j]-'0')+D;
            }
        }

        //brute force
        int ans = 0;
        bool gOK = false;
        for( int size = min(R,C); size >= 3; size-- ) {
            for( int i=0; i<R-size+1; i++ )
                for( int j=0; j<C-size+1; j++ ) {
                    //now go through and find theoretical centre
                    double cy, cx;
                    double numX=0, denX=0, numY=0, denY=0;
                    for( int y=i; y<i+size; y++ ) {
                        for( int x=j; x<j+size; x++ ) {
                            if( y==i && x == j ) continue;
                            if( y==i && x == j+size-1 ) continue;
                            if( y==i+size-1 && x == j ) continue;
                            if( y==i+size-1 && x == j+size-1 ) continue;
                            numY += (double(y)+0.5)*mass[y][x];
                            denY += mass[y][x];
                            numX += (double(x)+0.5)*mass[y][x];
                            denX += mass[y][x];
                            //cout << "proc:" << y << " " << x << endl;
                            //cout << (double(x)+0.5)*mass[y][x] << endl;
                            //cout << numY << endl;
                        }
                    }
                    cy = numY / denY;
                    cx = numX / denX;
                    //cout << numY << " " << denX << endl;
                    /*
                    if( cx >= j && cx < j+size && cy >= i && cy < i+size ) {
                        if( (cx <= j+1 && cy <= i+1) || (cx >= j+size-1 && cy <= 1 ) ||
                            (cx <= j+1 && cy >= i+size-1) || (cx >= j+size-1 && cy >= i+size-1) )
                            continue;
                        ans = max(ans,size);

                        cout << "Found! " << cy << " " << cx << endl;
                        cout << "Top left:" << i << " " << j << endl;
                        cout << "Size = " << size << endl;
                    }
                    */
                    if( fabs(cx-((double)j+(double)size/2.0)) < EPS && fabs(cy-((double)i+(double)size/2.0)) <EPS ) {
                        ans = max(ans,size);
                        gOK=true;
                        break;
                    }
                    if(gOK) break;
                }
                if(gOK) break;
        }



        out << "Case #" << test << ": ";
        if( ans == 0 ) out << "IMPOSSIBLE" << endl;
        else out << ans << endl;


    }

    return 0;
}



