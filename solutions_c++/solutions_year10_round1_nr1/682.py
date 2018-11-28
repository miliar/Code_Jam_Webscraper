#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#define pb push_back
using namespace std;


vector <string> board;
char line[200];


vector <string> rotate ( vector <string> &v){
        vector <string> ret;
        string tmp;

        for (int j=0;j<v.size();++j){
            tmp = "";
            for (int k=v.size()-1;k>=0;--k){
                    tmp.pb ( v[k][j] );
                }
                ret.push_back ( tmp );
            }
    return ret;
    }

vector <string> doGravity ( vector <string> &v ){
        vector <string> ret;
        for (int k=0;k<v.size();++k){
                string tmp;
                for (int j=0;j<v.size();++j) if ( v[k][j] == '.') tmp.pb ( '.');
                for (int j=0;j<v.size();++j) if ( v[k][j] != '.') tmp.pb ( v[k][j] );
                ret.pb ( tmp );
            }
    return ret;
    }


string checkState ( vector <string> &v , int toWin){
        bool blue = false, red = false;


        for (int row = 0; row < v.size();++row ){
            for (int col = 0; col < v.size();++col ){
                    if ( v[row][col] == '.' ) continue;
                    bool left = true, right = true, rdown = true, ldown = true, down = true;

                    for (int i =0;i<toWin;++i){
                            if ( col - i < 0 || v[row][col-i] != v[row][col]) left = false;
                            if ( col + i >= v.size() || v[row][col+i] != v[row][col] ) right = false;
                            if ( row + i >= v.size() || v[row+i][col] != v[row][col] ) down = false;

                            if ( col - i < 0 || row + i >= v.size() || v[row+i][col-i] != v[row][col] ) ldown = false;
                            if ( col + i >= v.size() || row + i >= v.size() || v[row+i][col+i] != v[row][col] ) rdown = false;
                        }

                    if ( left || right || down || ldown || rdown ){
                            if ( v[row][col] == 'R') red = true;
                            else blue = true;
                        }

                }
            }

        if ( red && blue ) return "Both";
        if ( red ) return "Red";
        if ( blue ) return "Blue";
        return "Neither";
    }


int main ( void ){
freopen ( "A-large.in", "r", stdin);
freopen ( "A-large.out", "w", stdout);
    int t, _t;

    scanf ("%d", &t);
    _t = t;

    while ( t--){
            int n, toWin;
            board.clear();
            scanf ("%d %d", &n, &toWin);

            for (int k=0;k<n;++k){
                    scanf ("%s", line);
                    board.push_back ( line );
                }

            board = doGravity ( board );
            board = rotate ( board);

            printf ("Case #%d: %s\n", _t - t , checkState ( board, toWin).c_str());;


        }



        return 0;
    }
