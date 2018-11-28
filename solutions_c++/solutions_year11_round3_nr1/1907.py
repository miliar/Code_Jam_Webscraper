#include<iostream>
#include <cstdlib>
using namespace std;
#include <fstream>

/*
 * 
 */
int main(int argc, char** argv) {

    char buffer[51];
    ifstream in;
    ofstream out;
    in.open("A-large.in", ios_base::in);
    out.open("output.txt", ios_base::out);
    if (in && out) {
        int r, c;
        in >> buffer;
        int k = atoi(buffer);
        for (int i = 0; i < k; i++) {
            char **array;
            in >> buffer;
            r  = atoi(buffer);
            array = new char*[r];
            in >> buffer;
            c = atoi(buffer);
            for (int j = 0; j < r; j++) {
                array[j] = new char[c];
                in >> array[j];
            }
            for (int m = 0; m < r - 1; m++) {
                for (int l = 0; l < c - 1; l++) {
                    if ((array[m][l] == array[m][l + 1] && array[m][l] == '#') && (array[m + 1][l] == array[m + 1][l + 1] && array[m + 1][l + 1] == '#')) {
                        array[m][l] = '/';
                        array[m][l + 1] = '\\';
                        array[m + 1][l] = '\\';
                        array[m + 1][l + 1] = '/';
                        //cout<<"\\";
                    }
                }
            }
            bool t = false;
            for (int l = 0; l < r; l++) {
                for (int m = 0; m < c; m++) {
                    if (array[l][m] == '#') {
                        out << "Case #" << i + 1 << ":\nImpossible" << endl;
                        t = true;
                        break;
                    }                    
                }
                if(t)
                        break;
            }
            if (t == false) {
                out << "Case #" << i + 1 << ":" << endl;
                for (int l = 0; l < r; l++) {
                    out << array[l] << endl;
                }
            }

        }
    }
    in.close();
    out.close();
}


