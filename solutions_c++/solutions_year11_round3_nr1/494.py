#include<iostream>
#include<fstream>
#include<vector>

using namespace std;  

int main(){
    ofstream fout ("out.out");
    ifstream fin ("in.in");
    int t;
    fin >> t;
    for (int caso = 1; caso <= t; caso++){
        int r, c;
        fin >> r >> c;
        vector<vector<char> > v (r, vector<char> (c));
        int ct = 0;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){ 
                fin >> v[i][j];
                if (v[i][j] == '#') ct++;
            }
        }
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                if (v[i][j] == '#'){
                    if (i < r-1 and j < c-1 and v[i+1][j] == '#' and v[i][j+1] == '#' and v[i+1][j+1] == '#'){
                        v[i][j] = '/';
                        v[i+1][j] = 92;
                        v[i][j+1] = 92;            
                        v[i+1][j+1] = '/';
                        ct-=4;
                    }
                }
            }
        }
        fout << "Case #" << caso << ":" << endl;
        if (ct != 0) fout << "Impossible" << endl;
        else{
            for (int i = 0; i < r; i++){
                for (int j = 0; j < c; j++){
                    fout << v[i][j];
                }
                fout << endl;
            }
        }
    }
}
