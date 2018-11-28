#include <iostream>
#include <cstdio>
#include <queue>
#include <fstream>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

const int dx[8]={-1,-1,-1,0,1,1,1,0}, dy[8]={-1,0,1,1,1,0,-1,-1};

bool inRange(int y, int x) {
    return (x>=0 && x<4 && y>=0 && y<4);
}
int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        queue<pair<int,int> > q;
        string b[5];
        string status = ""; //the final result
        for( int i=0; i<4; i++ ) {
            in >> b[i];
            cout << b[i] << endl;
        }

        for( int i=0; i<4; i++ ) {
            q.push( make_pair(i,0) );
            q.push( make_pair(0,i) );
            q.push( make_pair(3,i) );
            q.push( make_pair(i,3) );
        }
        while(!q.empty()) {
            pair<int,int> t = q.front(); q.pop();
            if( b[t.first][t.second] == '.' || b[t.first][t.second] == 'T' ) continue;

            for( int k=0; k<8; k++ ) {
                bool ok = true;
                for( int s=1; s<4; s++ ) {
                    int nX = t.second+dx[k]*s, nY = t.first+dy[k]*s;
                    if( !inRange(nY, nX) || (b[nY][nX] != b[t.first][t.second] && b[nY][nX] != 'T')) { ok=false; break; }
                }
                if(ok) { status = (b[t.first][t.second] == 'X') ? "X won":"O won"; break; }
            }
            if( status!="") break; //winner found
        }

        if(status == "") {
            bool draw = true;
            for( int i=0; i<4; i++ ) for( int j=0; j<4; j++ ) {
                if( b[i][j] == '.') draw = false;
            }
            status = draw ? "Draw":"Game has not completed";
         }

         out << "Case #" << test << ": " << status << endl;

    }
    return 0;
}
