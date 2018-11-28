#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>


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
        int N, L, H;
        in >> N >> L >> H;
        vector<int> notes;
        for( int i=0; i<N; i++ ) {
            int t;
            in >> t;
            notes.push_back(t);
        }

        bool found=false;
        for( int i=L; i<=H; i++ ) {
            bool gOK = true;
            for( int j=0; j<notes.size(); j++ ) {
                bool ok=false;
                if( notes[j] > i && notes[j]%i==0 ) ok = true;
                if( notes[j] <= i && i%notes[j]==0 ) ok= true;
                if(!ok) {
                    gOK = false;
                    break;
                }
            }
            if(gOK) {
                out << "Case #" << test << ": " << i << endl;
                found = true;
                break;
            }
        }

        if( !found ) {
            out << "Case #" << test << ": NO" << endl;
        }
    }

    return 0;
}



