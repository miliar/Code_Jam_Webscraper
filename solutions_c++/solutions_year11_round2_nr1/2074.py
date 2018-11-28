//============================================================================
// Name        : rpi.cpp
// Author      : Aziz
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream> //Standard input/output
#include <fstream> //File input/output
#include <cstdlib> //C library
#include <cmath> //Math library
#include <algorithm> //Some algorithms like sorting
#include <vector> //Vectors (Array lists)
#include <string> //Strings
#include <map> //Maps

using namespace std;

ifstream fin ("rpi.in");
ofstream fout ("rpi.out");

int T, MAXN=100;
char tC;

int main() {
	fin >> T;
	for(int y = 0; y < T; y++){
            int N, B[MAXN][MAXN], G[MAXN][2];
            double WP[MAXN][MAXN], OWP[MAXN], OOWP[MAXN];
            fin >> N;
            for(int a = 0; a < N; a++){
                    int wins=0, tot=0;
                    for(int b = 0; b < N; b++){
                            fin >> tC;
                            if(tC == '.') B[a][b]=-1;
                            else B[a][b] = atoi(&tC);
                            if(B[a][b]>0) wins++;
                            if(B[a][b]>=0) tot++;
                    }
                    WP[a][a] = (double)wins/tot;
                    G[a][0] = wins, G[a][1] = tot;
            }
            for(int a = 0; a < N; a++)
                    for(int b = 0; b < N; b++)
                            if(B[a][b]>=0)
                                  WP[a][b] = ((double)G[a][0]-B[a][b])/(G[a][1]-1);
                                  
            for(int a = 0; a < N; a++){
                    double sum = 0, tot = 0;
                    for(int b = 0; b < N; b++)
                            if(B[a][b]>=0){
                                   sum += WP[b][a];
                                   tot++;       
                            }
                    OWP[a] = sum/tot;
            }
            
            
            for(int a = 0; a < N; a++){
                    double sum=0, tot=0;
                    for(int b = 0; b < N; b++)
                            if(B[a][b]>=0){
                                   sum += OWP[b];
                                   tot++;
                            }
                    OOWP[a] = sum/tot;
           }
           fout << "Case #" << y+1 << ":\n";
           for(int a = 0; a < N; a++)            
                   fout << (.25 * WP[a][a] + .5 * OWP[a] + .25 * OOWP[a]) << "\n";
   }         
return EXIT_SUCCESS;
}
