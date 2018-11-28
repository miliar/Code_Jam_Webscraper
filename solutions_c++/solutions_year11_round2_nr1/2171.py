//
//  Round 1B Round 2011 - A
//
//  Diogo Tridapall
//

#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <queue>
#include <cmath>
#include "limits.h"

using namespace std;


int main (int argc, const char * argv[]){

    string inFileName;
    string outFileName;
    
    switch (argc) {
        case 2:
            inFileName = argv[1];
            outFileName.assign(inFileName, 0, inFileName.find_last_of(".in")-2);
            outFileName+=".out";
            break;
        default:
            cout << "Usage: " << argv[0] << " inputFile" << endl;
            exit(0);
            break;
    }
    
    fstream inFile(inFileName.c_str(),fstream::in);
    if (!inFile.is_open()) {
        cout << "File " << inFileName << " is not open!" << endl;
        exit(1);
    }
    fstream outFile(outFileName.c_str(),fstream::out);
    if (!outFile.is_open()) {
        cout << "File " << outFileName << " is not open!" << endl;
        exit(1);
    }
    
    
    int T;    
    
    if(!(inFile >> T)){
        cout << "Error, can't read T!" << endl;
        exit(1);
    }
    
    for (int iT = 0; iT < T; ++iT) {
        int N;
        inFile >> N;
        vector<string> play(N);
        double *WP = new double [N];
        double *OWP = new double [N];
        double *OOWP = new double [N];
        double *RPI = new double [N];

        double **WPWO = new double* [N];
        for (int i=0; i<N; ++i) {
            WPWO[i] = new double[N];
        }
        
        for (int i=0; i<N; ++i) {
            inFile >> play[i];
            double win=0;
            double tot=0;
            for (int j=0; j<N; ++j) {
                if (play[i][j]=='1') {
                    ++win;
                    ++tot;
                } else if (play[i][j]=='0')
                    ++tot;
            }
            
            WP[i] = win/tot;
        }

        for (int i=0; i<N; ++i) {
            for (int j=0; j<N; ++j) {
                double win=0;
                double tot=0;
                for (int k=0; k<N; ++k) {
                    if (k!=j){
                        if (play[i][k]=='1') {
                            ++win;
                            ++tot;
                        } else if (play[i][k]=='0')
                            ++tot;
                    }
                }
                WPWO[i][j] = win/tot;
            }
        }

        
        for (int i=0; i<N; ++i) {
            double tot=0;
            double n=0;
            for (int j=0; j<N; ++j) {
                if (play[i][j]!='.') {
                    tot+=WPWO[j][i];
                    ++n;
                }
            }
            OWP[i] = tot/n;
        }
        
        
        outFile << "Case #" << iT+1 << ":" << endl;
        for (int i=0; i<N; ++i) {
            double tot=0;
            double n=0;
            for (int j=0; j<N; ++j) {
                if (play[i][j]!='.') {
                    tot+=OWP[j];
                    ++n;
                }
            }
            OOWP[i] = tot/n;
            RPI[i] = 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i];
            outFile << RPI[i] << endl;
        }
        
        
        for (int i=0; i<N; ++i) {
            delete [] WPWO[i];
        }
        delete [] WP;
        delete [] WPWO;
        delete [] OWP;
        delete [] OOWP;
        delete [] RPI;
    }
    
    
    inFile.close();
    outFile.close();
    return 0;
}


















