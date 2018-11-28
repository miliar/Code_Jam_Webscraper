#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int r,c;
char pic[100][100];


int main(int argc, char** argv)
{
    if(argc < 3) {
        cerr << "Usage: ./a input-file-name output-file-name" << endl;
        return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int case_num;
    fin >> case_num;
    for(int k=0; k<case_num; ++k){
        fin >> r >> c;
        for(int i=0; i<r; ++i)
            for(int j=0; j<c; ++j) fin >> pic[i][j];

        bool imp = true;
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                if(pic[i][j] == '#'){
                    int i1 = i+1;
                    int j1 = j+1;
                    if(i1 > r || j1 > c) {
                        imp = false;
                        break;
                    }
                    if(pic[i][j1] == '#' && pic[i1][j] == '#' && pic[i1][j1] == '#'){
                        pic[i][j] = '/';
                        pic[i1][j] = '\\';
                        pic[i][j1] = '\\';
                        pic[i1][j1] = '/';
                    }else{
                        imp = false;
                        break;
                    }
                }
            }
            if(imp == false) break;
        }
        
        fout << "Case #" << k+1 <<": " << endl;
        if(imp == false) fout << "Impossible" << endl;
        else{
            for(int i=0; i<r; ++i){
                for(int j=0; j<c; ++j)
                    fout << pic[i][j];
                fout << endl;
            }
        }
    }
    fout.close();
    fin.close();

    return 0;
}
    
