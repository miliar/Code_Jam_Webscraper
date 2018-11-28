#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>


#define For(i,n) for(int i(0),_n(n);i<_n;++i)

using namespace std;

char checkLine(vector<char> v) {

    int numX=0, numO=0, checkFor = 4;

    For(i,4) {
        if(v[i] == 'X') numX++;
        if(v[i] == 'O') numO++;
        if(v[i] == 'T') checkFor = 3;
    }

    if(numX == checkFor) return 'X';
    else if(numO == checkFor) return 'O';
    else return 0;

}

int main(int argc, char const *argv[]) {
    long long T;
    fstream f("in.in");
    f >> T;
    For(t,T) {
        char c, w;
        bool emptyCell = false;
        vector<char> v;
        vector<vector<char> > map;
        For(i,4) {
            vector<char> vect;
            For(j,4){
                f >> c;
                if(c == '.') emptyCell = true;
                vect.push_back(c);
            }
            map.push_back(vect);
        }

        // Ver Lines
        For(i,4) {
            char w = checkLine(map[i]);
            if(w > 0 ) {
                cout << "Case #"<<t+1<<": "<<w<<" won"<<endl;
                goto stop;
            }
        }

        // Hor Lines
        For(j,4) {
            vector<char> v;
            v.push_back(map[0][j]);
            v.push_back(map[1][j]);
            v.push_back(map[2][j]);
            v.push_back(map[3][j]);
            char w = checkLine(v);
            if(w > 0 ) {
                cout << "Case #"<<t+1<<": "<<w<<" won"<<endl;
                goto stop;
            }
        }

        // \ Lines

        v.push_back(map[0][0]);
        v.push_back(map[1][1]);
        v.push_back(map[2][2]);
        v.push_back(map[3][3]);
        w = checkLine(v);
        if(w > 0 ) {
            cout << "Case #"<<t+1<<": "<<w<<" won"<<endl;
            goto stop;
        }

        // / Lines
        v.clear();
        v.push_back(map[0][3]);
        v.push_back(map[1][2]);
        v.push_back(map[2][1]);
        v.push_back(map[3][0]);
        w = checkLine(v);
        if(w > 0 ) {
            cout << "Case #"<<t+1<<": "<<w<<" won"<<endl;
            goto stop;
        }
        //cout << "Case #"<<t+1<< " Not solved" << endl;

        if(emptyCell) cout << "Case #"<<t+1<< ": Game has not completed" << endl;
        else cout << "Case #"<<t+1<< ": Draw" << endl;

        stop:;
    }
    f.close();
    return 0;
}
