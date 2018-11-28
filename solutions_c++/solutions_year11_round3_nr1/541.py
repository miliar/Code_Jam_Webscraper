#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

typedef long long LL;
string grid[100];
const int dx[4]={0,1,0,1}, dy[4]={0,0,1,1};
char foo[4]={'/', '\\', '\\', '/'};
int R, C;

bool inRange( int y, int x ) {
    return (y>=0&&y<R&&x>=0&&x<C);
}

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        in >> R >> C;
        bool impos = false;
        for( int i=0; i<R; i++ ) in >> grid[i];

        for( int i=0; i<R; i++ ) {
            for( int j=0; j<C; j++ ) {
                if( grid[i][j] == '#' ) {
                    //try and place
                    bool ok=true;
                    for( int k=0; k<4; k++ ) {
                        if( !inRange(i+dy[k],j+dx[k]) || grid[i+dy[k]][j+dx[k]] != '#' ) ok=false;
                    }
                    if(ok) {
                        for( int k=0; k<4; k++ ) {
                            grid[i+dy[k]][j+dx[k]] = foo[k];
                        }
                    }
                }
                if( grid[i][j] == '#' ) {
                    impos = true;
                    break;
                }
            }
        }

        out << "Case #" << test << ":" << endl;

        if( impos ) {
            out << "Impossible" << endl;
        }
        else {
            for( int i=0; i<R; i++ ) {
                out << grid[i] << endl;
            }
        }
    }

    return 0;
}



